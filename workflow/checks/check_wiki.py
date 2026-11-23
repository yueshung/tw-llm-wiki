#!/usr/bin/env python3
r"""G2/G3 Wiki 檢查（機械可驗證的部分）。
通過條件：
 1. 每頁 frontmatter 有 id/type/sources/last_verified，且 id 等於檔名
 2. frontmatter 的 sources / supplementary(_sources) 都存在於 raw/sources.yaml
 3. 事實依據欄位 sources 內不得出現 usage=supplementary 或 M 開頭來源
 4. 正文中引用的來源 id（S\d\d、M\d\d）都存在於 sources.yaml
 5. 正文 [[連結]] 指向存在的頁面（缺頁以警告列出，不算失敗，因為允許先佔位）
 7. 事件頁（type=incident）的「尚待確認事項」必須明確出現「攻擊者身分」與「調查進度」兩個詞，
    官方沒說也要寫「未載」，不可沉默（此規則由 G6 測試 Q6、Q7 失敗後新增）
 6. 作為標籤使用的 [事實]（出現在項目符號開頭 "- [事實]" 或表格儲存格開頭 "| [事實]"）必須同行有來源 id（S\d\d）；
    圖例列（> 開頭）與「本節沒有可標為 [事實] 的內容」這類說明文字不算標籤
不檢查：語意是否正確、來源內容是否真的支持該句（需人工或 G4 抽查）。
用法：python3 workflow/checks/check_wiki.py
"""
import re, sys, glob, os
import yaml

src = {s["id"]: s for s in yaml.safe_load(open("raw/sources.yaml", encoding="utf-8"))["sources"]}
pages = {}
errors, warns = [], []

for path in glob.glob("wiki/**/*.md", recursive=True):
    if "_templates" in path or os.path.basename(path) in ("index.md", "log.md"):
        continue
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        errors.append(f"{path}: 缺少 frontmatter"); continue
    fm = yaml.safe_load(m.group(1))
    body = txt[m.end():]
    pid = fm.get("id")
    pages[pid] = path
    if pid != os.path.splitext(os.path.basename(path))[0]:
        errors.append(f"{path}: id({pid}) 與檔名不符")
    for k in ("id", "type", "sources", "last_verified"):
        if k not in fm: errors.append(f"{path}: frontmatter 缺 {k}")
    for sid in fm.get("sources", []):
        if sid not in src: errors.append(f"{path}: sources 內 {sid} 不在 sources.yaml")
        elif src[sid]["usage"] != "fact_basis" or sid.startswith("M"):
            errors.append(f"{path}: sources 欄含非事實依據來源 {sid}")
    for k in ("supplementary", "supplementary_sources"):
        for sid in fm.get(k, []) or []:
            if sid not in src: errors.append(f"{path}: {k} 內 {sid} 不在 sources.yaml")
    for sid in set(re.findall(r"\b([SM]\d{2})\b", body)):
        if sid not in src: errors.append(f"{path}: 正文引用不存在的來源 {sid}")
    if fm.get("type") == "incident":
        for must in ("攻擊者身分", "調查進度"):
            if must not in body:
                errors.append(f"{path}: 事件頁缺少必填的未知項說明「{must}」")
    for i, line in enumerate(body.splitlines(), 1):
        is_tag = re.search(r"(^\s*-\s|\|\s)\[事實\]", line) is not None
        if is_tag and not line.lstrip().startswith(">") and not re.search(r"\bS\d{2}\b", line):
            errors.append(f"{path}:{i}: [事實] 行沒有來源 id → {line[:40]}")
    pages[pid] = (path, body)

for pid, (path, body) in pages.items():
    for link in set(re.findall(r"\[\[([a-z0-9\-]+)\]\]", body)):
        if link not in pages: warns.append(f"{path}: 連結 [[{link}]] 尚無頁面")
    # 純文字 id 引用（相關知識連結段）
    for link in set(re.findall(r"\b((?:concept|incident)-[a-z0-9\-]+)\b", body)):
        if link not in pages: warns.append(f"{path}: 引用 {link} 尚無頁面")

print(f"檢查 {len(pages)} 頁")
for w in sorted(set(warns)): print("警告:", w)
if errors:
    print("未通過："); [print(" -", e) for e in errors]; sys.exit(1)
print("G2/G3（機械檢查部分）通過")
