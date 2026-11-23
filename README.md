# 臺灣資安事件 LLM Wiki（TW Security Wiki）

以臺灣近期、具代表性的資安事件為切入點，建立**可追溯來源、逐句標記事實與推論**的知識庫（Wiki），再依 Wiki 產生給資訊管理系學生的**教學簡報**。

> 本專案由ㄒ「規則 → 來源 → Wiki → 檢查 → 簡報 → 測試」的流程下產出，所有規則寫在 [`AGENTS.md`](AGENTS.md)，所有實際執行結果記錄在 [`tests/run-log.md`](tests/run-log.md)。

---

## 1. 專案目的

| 目標 | 說明 |
|---|---|
| 可追溯 | 每個陳述句都能對應到來源編號（S／M 開頭），並標明是事實、推論或待確認 |
| 知識分層 | 長期有效的技術知識（概念頁）與會變動的事件資料（事件頁）分開維護 |
| 防止 AI 幻覺 | 以腳本自動檢查來源與標記，再以人工抽查語意 |
| 教學應用 | 簡報每一頁都必須對應到 Wiki 頁與事實依據來源，不得脫離 Wiki |

---

## 2. 目錄結構

```
.
├── CLAUDE.md                  # 入口檔：指示 AI 先讀 AGENTS.md，一切以其為準
├── AGENTS.md                  # 專案長期規則（來源、標記、格式、SOP、禁止事項）
├── requirements.txt           # Python 套件：pyyaml、beautifulsoup4
│
├── raw/
│   └── sources.yaml           # 來源索引（Source Registry），目前共 50 筆（S 官方／標準、M 媒體補充）
│
├── wiki/
│   ├── index.md               # 總目錄（八大模組、概念頁、事件頁）
│   ├── log.md                 # 變更日誌（日期｜動作｜對象｜說明）
│   ├── _templates/            # 頁面模板：concept.md、incident.md、source.md
│   ├── concepts/              # 長期知識：14 個概念頁
│   └── incidents/             # 易變事件：6 個事件頁（A～F）
│
├── slides/
│   └── index.html             # 單檔教學簡報（無外部資源，桌面與手機皆可）
│
├── workflow/
│   ├── DESIGN.md              # Loop／Graph 設計說明與 v1→v2 修改原因
│   ├── graph.mmd              # 工作流程圖（Mermaid）
│   └── checks/                # 自動檢查腳本（見第 5 節）
│
└── tests/
    ├── run_qa.py              # G6 知識問答測試（檢索層）
    └── run-log.md             # 實際執行紀錄（含失敗與修正）
```

---

## 3. 內容概覽

### 3.1 概念頁（`wiki/concepts/`）— 長期知識

依八個教學模組分類：

| 模組 | 概念頁 |
|---|---|
| 1 臺灣資安威脅現況 | `concept-taiwan-threat-landscape` |
| 2 攻擊原理與生命週期 | `concept-security-fundamentals`、`concept-attack-lifecycle`、`concept-ai-assisted-attack` |
| 3 社交工程與憑證攻擊 | `concept-social-engineering`、`concept-credential-attack` |
| 4 勒索軟體與個資外洩 | `concept-ransomware` |
| 5 Web、API 與系統漏洞 | `concept-authentication-logic-flaw`、`concept-api-security`、`concept-vulnerability-management`、`concept-web-system-vulnerability` |
| 6 供應鏈與關鍵基礎設施 | `concept-third-party-risk` |
| 8 治理與事件應變 | `concept-incident-response`、`concept-breach-notification` |

> 模組 7（防禦與威脅偵測）目前尚無獨立概念頁，防禦內容分散於各事件頁與概念頁。

### 3.2 事件頁（`wiki/incidents/`）— 易變事件

| 代號 | 事件 | 狀態 |
|---|---|---|
| A | 境外駭客運用 AI 代理工具的網攻浪潮與企業個資外洩 | 進行中 |
| B | 外交部領事事務局部分網站遭駭 | 進行中 |
| C | 永豐銀行新網銀異常轉帳 | 進行中 |
| D | 馬偕與彰基 CrazyHunter 勒索軟體 | 較早的代表性事件 |
| E | 「忘記帳號」身分驗證漏洞 | 補充小案例 |
| F | 偽冒行政院法規會社交工程郵件 | 補充小案例 |

每個事件頁都有完整**因果鏈**：事件 → 攻擊手法 → 技術原理 → 系統弱點 → 事件影響 → 防禦措施；並**必須**寫明「攻擊者身分」與「調查進度」（官方沒說也要寫「未載」）。

### 3.3 簡報（`slides/index.html`）

- 單一 HTML 檔，共 13 頁，分章節：開場、基礎、案例、防禦、應變、總結
- 功能：上一頁／下一頁、目錄跳頁、進度條、鍵盤（←、→、End 等）、觸控滑動、網址 hash 定位
- 每頁都有：教學目的（`.goal`）、`data-wiki`（對應的 Wiki 頁）、`data-src`（事實依據來源）、`data-sup`（補充來源，選填）
- 簡報頁面以自然語句呈現，不顯示「推論」「待確認」標籤；完整標記保留在 Wiki

---

## 4. 核心規則摘要（完整版見 `AGENTS.md`）

### 4.1 來源分級

1. 政府與主管機關官方 → 2. 標準機構（NIST、MITRE、OWASP、CISA）→ 3. 受影響機構公告 → 4. 媒體（僅補充）

- `S` 開頭：官方／標準來源，且全文已讀，才可作為事實依據（`usage: fact_basis`）
- `M` 開頭：媒體或廠商分析，一律為補充（`usage: supplementary`），不得作為事實依據
- `read_status`：`full`（頁面全文讀過）／`partial`（只讀到摘錄）／`unread`

### 4.2 陳述標記

| 標記 | 意義 | 要求 |
|---|---|---|
| `[事實]` | 來源明確載明 | 同一行必須有官方來源 id（S 開頭） |
| `[媒體轉述官方]` | 媒體轉述官方說法，尚無一手書面來源 | 附 M 來源 id |
| `[推論]` | 自行推導 | 必須寫「依據：…」 |
| `[技術研究]` | 資安廠商或研究單位的分析 | M 來源；各家說法不一時並列 |
| `[待確認]` | 來源沒說或說法不一 | 並列各來源說法，不自行裁決 |

### 4.3 禁止事項

- 不得捏造事件、數字、來源、測試結果
- 不得把推論寫成事實，不得讓簡報內容脫離 Wiki
- 不得把環境限制說成已完成（沒有真實瀏覽器就不能寫「手機畫面已測試」）

---

## 5. 品質檢查（Gate）

| 節點 | 指令 | 檢查內容 |
|---|---|---|
| G1 來源 | `python3 workflow/checks/check_sources.py` | 必填欄位、id 不重複、事實依據須為官方／標準且全文已讀、媒體不得為事實依據 |
| G2/G3 Wiki | `python3 workflow/checks/check_wiki.py` | frontmatter、來源 id 存在、`[事實]` 行有來源 id、事件頁含「攻擊者身分」「調查進度」 |
| G4/G5 簡報（靜態） | `python3 workflow/checks/check_slides.py` | 每頁有目的／data-wiki／data-src；數字須出現在引用的 Wiki 頁；無外部資源 |
| G5 導覽邏輯 | `node workflow/checks/test_nav.js` | 換頁、邊界、進度條、目錄、hash、鍵盤、滑動 |
| G6 知識問答 | `python3 tests/run_qa.py` | 有答案的題目能檢索到內容；Wiki 沒有的資訊必須明寫「未載」 |
| 人工抽查 | — | 隨機抽 3 個 `[事實]` 句對照原文（機械檢查看不出語意錯誤） |
| G7 真實瀏覽器 | — | 桌面與手機畫面檢查（**目前尚未執行**） |

---

## 6. 快速開始

### 環境需求

- Python 3.8+
- Node.js（執行 `test_nav.js`）

### 安裝與執行

```bash
pip install -r requirements.txt

# 依序執行所有檢查（於專案根目錄）
python3 workflow/checks/check_sources.py
python3 workflow/checks/check_wiki.py
python3 workflow/checks/check_slides.py
node workflow/checks/test_nav.js
python3 tests/run_qa.py
```

### 檢視簡報

直接以瀏覽器開啟 `slides/index.html`，不需伺服器或網路。

---

## 7. 新增事件的流程（SOP）

```
提供事件關鍵字／網址
   ↓
web_search 找官方一手來源 → web_fetch 讀全文
   ↓
登錄 raw/sources.yaml（先官方，後補充媒體）        ← G1
   ↓
依 incident.md 建立事件頁，逐句標記                  ← G2/G3
   ↓
在相關概念頁「相關真實案例」加連結；新手法則新增概念頁
   ↓
更新 wiki/index.md 與 wiki/log.md
   ↓
人工抽查 3 個 [事實] 句
   ↓
新增或修改簡報頁（標 data-wiki / data-src）          ← G4/G5/G6
```

任何一關失敗，**問題在哪一層就回哪一層修**：簡報數字錯先查 Wiki，不在簡報表面直接改數字。流程圖見 [`workflow/graph.mmd`](workflow/graph.mmd)，設計理由見 [`workflow/DESIGN.md`](workflow/DESIGN.md)。

---

## 8. 已知限制

- **單一模型**：撰寫、檢查與驗證皆由同一模型完成，沒有獨立的第二個驗證者
- **未做真實瀏覽器測試**：簡報排版與觸控操作僅驗證導覽邏輯（G7 未執行）
- **機械檢查有盲區**：無法偵測語意錯誤，需靠人工抽查
- **部分來源待複核**：例如全國法規資料庫條文細節（S12）因讀取失敗，相關內容標示「待複核」
- **未部署**：GitHub Pages 需自行建立
- **內容有時效性**：事件頁狀態為「進行中」者，需依官方後續公告更新

---

## 9. 檔案用途速查

| 檔案 | 用途 |
|---|---|
| `CLAUDE.md` | AI 的入口指示，導向 `AGENTS.md` |
| `AGENTS.md` | 專案規則總綱（單一事實來源） |
| `raw/sources.yaml` | 所有來源的登錄與可信度分級 |
| `wiki/index.md` | Wiki 導覽目錄 |
| `wiki/log.md` | 變更歷史與待辦（含修正紀錄） |
| `wiki/_templates/*` | 概念／事件／來源頁的標準格式 |
| `workflow/DESIGN.md` | 檢查節點、回退規則、版本修改說明 |
| `workflow/graph.mmd` | 流程圖（綠＝已執行、灰虛線＝未執行） |
| `tests/run-log.md` | 真實測試紀錄，含失敗與修正過程 |

---

## 10. 授權與使用

本專案內容引用政府機關與標準機構公開資料，請以各來源的原始頁面為準。教學使用時請標註來源，並留意事件狀態可能已更新。