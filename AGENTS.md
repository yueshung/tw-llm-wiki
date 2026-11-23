# AGENTS.md：臺灣資安事件 LLM Wiki 專案規則

本檔是專案的長期規則。任何 AI 在新增來源、事件、概念頁或簡報前，必須先讀完本檔。
規則來源：本專案第一次實際執行中發現的問題都已寫回這裡（見 tests/run-log.md）。

## 1. 專案目標
- 以臺灣近期或具代表性的資安事件為切入點，建立可追溯的 Wiki，再產生給資訊管理系學生的教學簡報。
- 內容分層：`wiki/concepts/` 是長期有效的技術知識；`wiki/incidents/` 是會變動的事件資料。新增事件不得改動概念頁的結構，只能在概念頁的「相關真實案例」加連結。

## 2. 目錄
raw/sources.yaml（來源索引）｜wiki/_templates｜wiki/concepts｜wiki/incidents｜wiki/index.md｜wiki/log.md｜slides/index.html｜workflow/（graph.mmd、DESIGN.md、checks/）｜tests/｜docs/

## 3. 來源規則（最高優先）
1. 優先順序：政府與主管機關官方 → 標準機構（NIST、MITRE、OWASP、CISA）→ 受影響機構自身公告 → 媒體（僅補充）。
2. 每筆來源必填：id、title、url、publisher、publish_date、retrieved_date、source_type、read_status、usage。官方日期不明寫 `unknown`，不得猜。
3. `usage: fact_basis` 只給 `official` 或 `standard` 且 `read_status: full` 的來源。媒體一律 `supplementary`，id 用 M 開頭，不得作為 [事實] 依據。
4. `read_status: full` 的意思是「該頁面本身全文讀過」。只讀到搜尋摘錄者標 `partial`。只讀過專案頁、沒讀 PDF 或子頁者，不得引用本文或子頁細節，並在 notes 寫明。
5. 取得原文：必須先 web_search 取得網址，再 web_fetch 讀全文（直接 fetch 未出現過的網址會被拒）。讀不到就標「未取得」，不得用搜尋摘要或記憶補寫。
6. 引用外國文件時註明版本與日期；二手文章與官方現況不同時以官方為準，並把差異寫進 Wiki（例：ATT&CK 官方 15 個戰術，二手常寫 14 個）。

## 4. 事實／推論標記（每個陳述句都要有）
- `[事實]`：來源明確載明。**同一行必須有官方來源 id（S 開頭）**。
- `[媒體轉述官方]`：媒體或簡報轉述官方說法，尚無一手書面來源；附 M 來源 id。
- `[推論]`：自己推導；必須寫「依據：…」。
- `[技術研究]`：資安廠商或研究單位的技術分析（M 來源，非官方）；各家說法不一時並列。
- `[待確認]`：來源沒說或說法不一；並列各來源說法，不自行裁決。簡報內不顯示此標籤，但 Wiki 保留。
- 教學分類（如「對應 CIA 要素」「對應 ATT&CK 戰術」）一律標推論，並註明「不是官方定性」。
- 計量單位照原文（例：領務局公告是「檔案」，不得改寫成人數）。數字不得自行加總或推算。
- 法律與政策分層標示：現行有效／已公布未施行／草案／政策呼籲，不得混為「法定要求」。

## 5. 頁面格式
- 概念頁依 wiki/_templates/concept.md；事件頁依 incident.md；frontmatter 的 id 必須等於檔名。
- 事件頁必須有因果鏈：事件 → 攻擊手法 → 技術原理 → 系統弱點 → 事件影響 → 防禦措施，每格標狀態。
- 事件頁「尚待確認事項」**必填兩項，官方沒說也要寫「未載」**：攻擊者身分、調查進度（含司法、賠償、是否結案）。
- 概念頁的 `sources` 只列事實依據；補充來源放 `supplementary_sources`。
- 寫每一頁之前，必須在同一輪重新讀取該頁要用的來源全文；不得憑先前印象或摘要撰寫。

## 6. 新增一個事件的流程（SOP）
1. 使用者提供事件關鍵字或網址。
2. 搜尋並讀官方一手來源全文；登錄到 raw/sources.yaml（先官方，後補充媒體）。
3. 以 incident.md 建立 `wiki/incidents/incident-<代號>-<短名>.md`，逐句標記。
4. 在相關概念頁的「相關真實案例」加一行連結；若出現新手法，建立或更新概念頁。
5. 更新 wiki/index.md 與 wiki/log.md（一行：日期｜動作｜對象｜說明）。
6. 執行檢查（見 §8）；任何失敗先修 Wiki，再碰簡報。
7. 簡報：新增或修改 slide，標 data-wiki 與 data-src，再跑 G4/G5。

## 7. 簡報規則
- 單一 slides/index.html，不依賴外部資源，桌面與手機皆可。
- 每頁必須有：教學目的（.goal）、data-wiki（至少一個 Wiki id，概覽頁可用 index）、data-src（只能是事實依據來源）。
- 簡報中的數字必須出現在該頁引用的 Wiki 頁內。
- 簡報頁面不顯示「推論」「待確認」等標籤，以自然語句呈現：官方說法寫出說話者與時點（例：數發部長 11/18 在立法院說明），尚未公布的資訊不寫或寫「尚未公布」；Wiki 內仍保留完整標記。
- `data-src` 只放事實依據來源；頁面使用的媒體轉述官方說法、廠商技術分析，放在 `data-sup`（補充來源），頁尾會顯示，check_slides.py 會驗證它們確實是補充來源。
- 簡報中的事件頁必須有「攻擊路徑」（依序說明攻擊者做了什麼）、為什麼沒擋住、怎麼改善。
- 每個攻擊手法必須對應到防禦；不得為美觀犧牲正確性。

## 8. 檢查指令（在專案根目錄）
```
pip install -r requirements.txt
python3 workflow/checks/check_sources.py     # G1 來源
python3 workflow/checks/check_wiki.py        # G2/G3 標記、連結、事件頁必填項
python3 workflow/checks/check_slides.py      # G4/G5 簡報對應 Wiki（靜態）
node workflow/checks/test_nav.js             # G5 導覽邏輯
python3 tests/run_qa.py                      # G6 問答（檢索層）
```
機械檢查看不出語意錯誤（例如「嘗試存取但被攔阻」被寫成「可存取」）。每次新增頁面後，須人工抽查至少 3 個 [事實] 句對照原文。

## 9. 禁止事項
- 不得捏造事件、數字、來源、測試結果；不得把推論寫成事實；不得讓簡報內容脫離 Wiki。
- 不得把環境限制說成已完成（例：沒有真實瀏覽器就不能寫「手機畫面已測試」）。
- 測試紀錄只寫實際執行的結果，包含失敗與修正；沒跑的寫「未執行」。

## 10. 使用的 AI
本專案第一次完整執行使用 Claude Sonnet 5.5（claude.ai 對話介面；API 模型字串 claude-sonnet-5-5）。更換模型時，在 workflow/DESIGN.md 記錄並重跑 G6。
