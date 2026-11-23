#!/usr/bin/env python3
r"""G4（簡報對應 Wiki）與 G5 的靜態部分。
通過條件：
 1. 每張 section.s 都有 data-wiki、data-src 與 .goal（教學目的）
 2. data-sup（補充來源，如媒體轉述官方說法、廠商技術分析）只能放 usage=supplementary 的來源；
    data-wiki 的每個 id 都有對應 wiki 頁（index 除外）；data-src 的 id 都在 sources.yaml，
    且不得引用 usage=supplementary 的來源作為頁面來源（媒體補充只能在內文以「媒體轉述」標示）
 3. 簡報內文的重要數字（含逗號、百分比、或 3 位數以上）必須出現在該頁引用的 Wiki 頁文字中
 4. 每個 wiki 事件頁與概念頁至少被一張簡報引用（未引用者列為警告）
 5. 導覽控制項存在（prev/next/toc/num/bar）、viewport meta 存在、無外部資源（http/https 的 src/href）
不檢查：視覺排版（需真實瀏覽器）、數字的語意是否正確。
"""
import re, sys, glob, os, yaml
from bs4 import BeautifulSoup
html = open("slides/index.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
src = {s["id"]: s for s in yaml.safe_load(open("raw/sources.yaml", encoding="utf-8"))["sources"]}
pages = {}
for p in glob.glob("wiki/**/*.md", recursive=True):
    if "_templates" in p: continue
    pages[os.path.splitext(os.path.basename(p))[0]] = open(p, encoding="utf-8").read()
errors, warns, used = [], [], set()
slides = soup.select("section.s")
print(f"簡報頁數：{len(slides)}")
for i, s in enumerate(slides, 1):
    wid = [x.strip() for x in (s.get("data-wiki") or "").split(",") if x.strip()]
    sid = [x.strip() for x in (s.get("data-src") or "").split(",") if x.strip()]
    if not wid: errors.append(f"第{i}頁：缺 data-wiki")
    if not sid: errors.append(f"第{i}頁：缺 data-src")
    if not s.select_one(".goal"): errors.append(f"第{i}頁：缺教學目的 .goal")
    for w in wid:
        used.add(w)
        if w != "index" and w not in pages: errors.append(f"第{i}頁：data-wiki {w} 沒有對應頁面")
    for x in [y.strip() for y in (s.get("data-sup") or "").split(",") if y.strip()]:
        if x not in src: errors.append(f"第{i}頁：data-sup {x} 不在 sources.yaml")
        elif src[x]["usage"] != "supplementary": errors.append(f"第{i}頁：data-sup 只能放補充來源，{x} 不是")
    for x in sid:
        if x not in src: errors.append(f"第{i}頁：data-src {x} 不在 sources.yaml")
        elif src[x]["usage"] != "fact_basis": errors.append(f"第{i}頁：data-src 引用非事實依據來源 {x}")
    text = s.get_text(" ")
    wiki_text = " ".join(pages.get(w, "") for w in wid if w != "index") + " " + " ".join(pages.values()) * 0
    if all(w == "index" for w in wid):
        wiki_text = " ".join(pages.values())   # 概覽頁：任一 wiki 頁出現即可
    for num in set(re.findall(r"\d[\d,]*\.?\d*%?", text)):
        core = num.rstrip(".")
        if (("," in core) or core.endswith("%") or len(re.sub(r"\D", "", core)) >= 3) and core not in wiki_text:
            errors.append(f"第{i}頁：數字 {core} 沒有出現在引用的 Wiki 頁")
for pid in pages:
    if pid.startswith(("concept-", "incident-")) and pid not in used:
        warns.append(f"Wiki 頁 {pid} 沒有被任何簡報頁引用")
for need in ["prev", "next", "toc", "num"]:
    if not soup.find(id=need): errors.append(f"缺導覽控制項 #{need}")
if not soup.select_one("#bar"): errors.append("缺進度條 #bar")
if not soup.find("meta", attrs={"name": "viewport"}): errors.append("缺 viewport meta")
for t in soup.find_all(True):
    for a in ("src", "href"):
        v = t.get(a, "")
        if v.startswith(("http://", "https://")): errors.append(f"外部資源：<{t.name}> {a}={v}")
for w in warns: print("警告:", w)
if errors:
    print("未通過："); [print(" -", e) for e in errors]; sys.exit(1)
print("G4/G5（靜態部分）通過")
