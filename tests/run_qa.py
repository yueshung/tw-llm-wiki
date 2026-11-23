#!/usr/bin/env python3
"""G6 知識問答測試（檢索層）。
做法：對每一題，只從 wiki/ 內檢索，列出命中的行；再檢查預期關鍵字是否在命中內容中，
或（對「知識庫沒有」的題目）檢查 Wiki 是否明確寫出「未載／待確認」而不是沉默。
限制：這只驗證「Wiki 內容夠不夠回答」，不驗證 AI 回答時有沒有照 Wiki 說；回答階段由人工對照記錄在 run-log.md。
用法：python3 tests/run_qa.py
"""
import glob, re, sys, os
pages = {os.path.basename(p)[:-3]: open(p, encoding="utf-8").read() for p in glob.glob("wiki/**/*.md", recursive=True) if "_templates" not in p}
def hits(pid, *kw):
    return [l.strip() for l in pages[pid].splitlines() if all(k in l for k in kw)]
Q = [
 ("Q1 領務局護照大頭照外洩的檔案數與日期範圍？", "incident-b-boca-website-breach", [("72,702",), ("2026-09-03", "11-02")], "answer"),
 ("Q2 新聞稿的「72 小時」是個資法現行法定期限嗎？", "incident-a-ai-agent-attacks", [("72 小時", "政策呼籲")], "answer"),
 ("Q3 對外曝露、已知被利用、可自動化、完全控制的弱點，處置期限多久？", "concept-vulnerability-management", [("| 1 |", "3 天")], "answer"),
 ("Q4 MITRE ATT&CK 官方企業矩陣目前有幾個戰術？", "concept-attack-lifecycle", [("15 個戰術",)], "answer"),
 ("Q5 永豐銀行 11/3 公告對原因用什麼詞？後續說法是否有一手書面來源？", "incident-c-sinopac-abnormal-transfer", [("程式異常",), ("媒體轉述官方",)], "answer"),
 ("Q6（Wiki 沒有）領務局事件的攻擊者是哪個駭客組織？", "incident-b-boca-website-breach", [("攻擊者", "未載")], "must_state_unknown"),
 ("Q7（Wiki 沒有）永豐事件最後的賠償總額與是否已結案？", "incident-c-sinopac-abnormal-transfer", [("賠償", "未")], "must_state_unknown"),
]
fail = 0
for q, pid, conds, mode in Q:
    ok = True; detail = []
    for kw in conds:
        h = hits(pid, *kw)
        detail.append((kw, len(h)))
        if not h: ok = False
    status = "PASS" if ok else "FAIL"
    if not ok: fail += 1
    print(f"{status} | {q} | 頁面 {pid} | 關鍵字命中 {detail}")
sys.exit(1 if fail else 0)
