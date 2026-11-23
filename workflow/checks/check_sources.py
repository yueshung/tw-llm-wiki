#!/usr/bin/env python3
"""G1 來源檢查：驗證 raw/sources.yaml。
通過條件：
 1. 每筆具備必要欄位 (id,title,url,publisher,publish_date,retrieved_date,source_type,read_status,usage)
 2. id 不重複；url 以 http(s):// 開頭
 3. usage=fact_basis 者：source_type 必須是 official/standard，且 read_status 必須是 full
 4. M 開頭（補充來源）不得 usage=fact_basis
用法：python3 workflow/checks/check_sources.py raw/sources.yaml
"""
import sys
try:
    import yaml
except ImportError:
    sys.exit("需要 PyYAML：pip install pyyaml")

REQ = ["id","title","url","publisher","publish_date","retrieved_date","source_type","read_status","usage"]
path = sys.argv[1] if len(sys.argv) > 1 else "raw/sources.yaml"
data = yaml.safe_load(open(path, encoding="utf-8"))["sources"]
errors, seen = [], set()
for s in data:
    sid = s.get("id", "?")
    for k in REQ:
        if k not in s or s[k] in (None, ""):
            errors.append(f"{sid}: 缺少欄位 {k}")
    if sid in seen: errors.append(f"{sid}: id 重複")
    seen.add(sid)
    if not str(s.get("url","")).startswith(("http://","https://")):
        errors.append(f"{sid}: url 格式錯誤")
    if s.get("usage") == "fact_basis":
        if s.get("source_type") not in ("official","standard"):
            errors.append(f"{sid}: fact_basis 必須是 official/standard，目前 {s.get('source_type')}")
        if s.get("read_status") != "full":
            errors.append(f"{sid}: fact_basis 必須 read_status=full，目前 {s.get('read_status')}")
    if str(sid).startswith("M") and s.get("usage") == "fact_basis":
        errors.append(f"{sid}: 補充來源不得作為事實依據")
print(f"檢查 {len(data)} 筆來源")
if errors:
    print("未通過："); [print(" -", e) for e in errors]; sys.exit(1)
print("G1 通過")
