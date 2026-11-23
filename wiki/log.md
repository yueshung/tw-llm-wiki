# Wiki 變更日誌
格式：日期 | 動作 | 對象 | 說明

2026-11-21 | init | raw/sources.yaml | 建立來源索引（S01–S16、M01–M04）；G1 檢查通過（19 筆）
2026-11-21 | init | wiki/_templates | 建立概念頁、事件頁、來源頁模板
2026-11-21 | create | incidents/incident-a-ai-agent-attacks.md | 依 S01 全文重讀後撰寫；72 小時標示為政策呼籲
2026-11-21 | fix | incidents/incident-a-ai-agent-attacks.md | 移除對 S12 的引用（S12 第二次讀取失敗無法覆核），改以 S01 轉述文字為據
2026-11-21 | create | concepts/concept-breach-notification.md | 四層分辨表；條文細節待複核（S12 於同日第二次讀取回傳伺服器錯誤）
2026-11-21 | todo | 待查 | 媒體標題曾出現「8,800 萬筆」，尚未取得原始依據，不採用；需找其出處或確認為誤植
2026-11-21 | todo | 待查 | S13 GitLab 新聞稿發布日期與全文；S14 六月月報全文；S15 本文；金管會書面新聞稿；H-ISAC 原始警訊
2026-11-21 | create | incidents/incident-b-boca-website-breach.md | 依 S02 全文（本次讀取版本含 ABTC 至 11/10）撰寫；M05–M07 為版本交叉比對用補充來源
2026-11-21 | add | raw/sources.yaml | 新增 M05–M07（領務局事件媒體報導，搜尋摘錄）
2026-11-21 | create | incidents/incident-c-sinopac-abnormal-transfer.md | 一手來源僅 S03（三句公告）；金管會與銀行後續說法標為「媒體轉述官方」
2026-11-21 | add | raw/sources.yaml | 新增 M08–M10（永豐事件媒體報導，搜尋摘錄）
2026-11-21 | tool | workflow/checks/check_wiki.py | 第一次執行出現 6 筆誤報（圖例列與「沒有可標為[事實]」說明文字被誤判）；修正檢查規則後通過。事件頁本身無需修改
2026-11-21 | create | incidents/incident-d-hospital-ransomware.md | 一手來源 S04 僅涵蓋彰基與全國應變；馬偕細節全部標「媒體轉述官方」；教戰守則與 H-ISAC 指南本文未取得
2026-11-21 | add | raw/sources.yaml | 新增 M11–M14（醫院勒索事件媒體報導，搜尋摘錄）
2026-11-21 | create | incidents/incident-e-forgot-account-auth-flaw.md | 依 S05（10 月月報）全文重讀後撰寫
2026-11-21 | create | incidents/incident-f-spoofed-legal-affairs-phishing.md | 依 S06（2 月月報）全文重讀後撰寫；月報未說明有機關被入侵
2026-11-21 | update | incidents/incident-a-ai-agent-attacks.md | 納入 S05 官方論述（KEV、API 熱區、AI 改變速度與成本）；sources 加入 S05
2026-11-21 | note | S06 | 首次嘗試直接 fetch 被拒（網址不在先前結果中），需先搜尋再取；已改以搜尋後 fetch 取得全文
2026-11-21 | fix | wiki/index.md | 先前更新索引的腳本因路徑錯誤（index.md 應為 wiki/index.md）失敗，事件 A 的 S05 補充已寫入但索引未更新；已補更新
2026-11-21 | create | concepts/concept-ai-assisted-attack.md, concept-authentication-logic-flaw.md, concept-social-engineering.md, concept-credential-attack.md | 皆只用已讀全文的官方來源（S01、S05、S06）；一般性定義待標準來源
2026-11-21 | fix | concepts/concept-credential-attack.md | 自行覆核時發現一句過度陳述（寫成「可存取其他功能」，S05 實為「嘗試存取但被攔阻」），已更正。機械檢查（check_wiki.py）無法偵測此類語意錯誤，需人工或 G4 抽查
2026-11-21 | add | raw/sources.yaml | 新增 S17（OWASP API Top 10 2023 總表，全文）
2026-11-21 | create | concepts/concept-vulnerability-management.md | 依 S11 PDF 全文重讀後撰寫，含 16 類型期限表
2026-11-21 | create | concepts/concept-api-security.md | 依 S17 全文與 S05、S01 撰寫；事件 A 與 OWASP 類型的對照標為推論
2026-11-21 | add | raw/sources.yaml | 新增 S18（ATT&CK 企業戰術總表 v20.1，全文）
2026-11-21 | create | concepts/concept-attack-lifecycle.md | 只用戰術層級；案例對照欄標為教學分類（推論）；記錄官方 15 戰術 vs 二手 14 戰術之差異
2026-11-21 | create | concepts/concept-incident-response.md | NIST 部分只引專案頁與公告可見內容；Detect/Respond/Recover 逐項定義標待確認；應變階段表標為教學整理，每格官方案例附來源
2026-11-21 | add | raw/sources.yaml | 新增 S19（CISA #StopRansomware Guide 官方頁，全文；外國官方文件，2023-09 版）
2026-11-21 | create | concepts/concept-ransomware.md, concept-third-party-risk.md | 一般原理用 S19；馬偕路徑仍為媒體轉述；責任歸屬不下結論
2026-11-21 | fix | concepts/concept-third-party-risk.md | check_wiki.py 抓到一行把媒體轉述標成 [事實]（來源只有 M04）；改標「媒體轉述官方」，並刪除 M03 不支持的「資安署亦強調」說法。這是機械檢查實際攔下的第一個錯誤標記
2026-11-21 | add | raw/sources.yaml | 新增 S20、S21（NIST CSRC 術語表：information security、vulnerability，全文）
2026-11-21 | create | concepts/concept-security-fundamentals.md, concept-taiwan-threat-landscape.md, concept-web-system-vulnerability.md | 基礎科普、模組1 現況、模組5 漏洞；「威脅」「風險」定義尚未取得來源，未寫
2026-11-21 | update | wiki/index.md | 補全 13 個概念頁索引
2026-11-21 | rule | workflow/checks/check_wiki.py、wiki/_templates/incident.md | G6 問答 Q6、Q7（Wiki 沒有的資訊）第一次跑失敗：事件頁對「攻擊者身分」「賠償與結案」沉默。新增規則：事件頁「尚待確認事項」必須明確寫出「攻擊者身分」「調查進度」；6 個事件頁補寫
2026-11-21 | fix | tests/run_qa.py | Q1 第一次失敗是測試期望過嚴（Wiki 寫 11-02 非 2026-11-02），修正測試而非 Wiki
2026-11-21 | add | raw/sources.yaml | 新增 M15–M30（領務局原因說明、永豐記者會與手法、ARTEX 與規模說法、GitLab 漏洞、CrazyHunter 廠商技術分析），皆為補充來源
2026-11-21 | update | incidents/incident-a|b|c|d | 新增「第二輪補充查證」區塊；原「待確認」條目保留，說明哪些已由補充來源回答、哪些仍缺一手書面來源
2026-11-21 | rule | AGENTS.md、check_slides.py | 簡報不顯示推論／待確認標籤；補充來源改放 data-sup 並由腳本驗證
