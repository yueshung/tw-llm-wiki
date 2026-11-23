---
id: concept-attack-lifecycle
type: concept
module: 2
title: 攻擊生命週期：用 MITRE ATT&CK 戰術理解一次入侵的各階段
tags: [MITRE ATT&CK, 戰術, Cyber Kill Chain, 橫向移動, 攻擊路徑]
related: [concept-social-engineering, concept-credential-attack, concept-ransomware, concept-ai-assisted-attack, concept-incident-response]
sources: [S18, S08, S11]
last_verified: "2026-11-21"
stability: long-term
---
> 標記：[事實]=來源明確載明；[推論]；[待確認]。S18、S08 只讀到戰術總表／矩陣頁，未讀各技術子頁，因此本頁只談「戰術層級」，不引用技術編號或具體技術細節。

## 主題與概念介紹
一次入侵通常不是一個動作，而是一連串階段：先探查、取得立足點、擴大權限、移動、取資料或破壞。把階段拆開，才能看出「在哪一格可以擋、可以偵測」。

## 基本原理
- [事實] ATT&CK 的「戰術（Tactic）」代表攻擊技術背後的「為什麼」，即攻擊者的戰術目標（S18）。
- [事實] 截至本次讀取（ATT&CK content v20.1），官方企業矩陣列出 15 個戰術：Reconnaissance、Resource Development、Initial Access、Execution、Persistence、Privilege Escalation、Stealth、Defense Impairment、Credential Access、Discovery、Lateral Movement、Collection、Command and Control、Exfiltration、Impact（S18）。
- [事實] 其中 Stealth（隱藏與偽裝成正常行為）與 Defense Impairment（破壞安全機制與工具，使防守方看不見或無法信任所見）是官方現行分類；許多二手介紹仍寫成 14 個戰術且含 Defense Evasion，與官方現況不同，本 Wiki 以官方為準（S18、S08）。
- [事實] 臺灣資安署的弱點處置指引另用「網路狙殺鏈（Cyber Kill Chain）」的偵察、武器化、傳遞、利用等階段，來判斷弱點能否被自動化利用（S11）。

## 技術分析：戰術對照表（含臺灣案例，皆為教學對照）
| 戰術 | 官方描述（改寫） | 本 Wiki 案例中的對照（推論） |
|---|---|---|
| Reconnaissance | 蒐集資訊以規劃行動 | A：AI 加速漏洞搜尋（S05 稱 AI 加速漏洞搜尋與攻擊） |
| Initial Access | 進入網路 | A：利用已知漏洞（S01）；F：釣魚信（S06） |
| Execution | 執行惡意程式碼 | F：誘導下載惡意附檔（S06） |
| Persistence | 維持立足點 | F：植入後門（S06） |
| Privilege Escalation | 取得更高權限 | D：媒體轉述 BYOVD 提權（M02） |
| Stealth | 隱藏行動、偽裝成正常行為 | 10 月釣魚信利用合法雲端服務降低被偵測機率（S05） |
| Credential Access | 竊取帳號與密碼 | 10 月偽 SharePoint 釣魚（S05）；D 弱密碼（M12） |
| Lateral Movement | 在環境中移動 | S11 的網段劃分、網路隔離即為防範橫向移動 |
| Collection／Exfiltration | 蒐集並竊取資料 | A：經高權限 API 大量取資料（S01） |
| Command and Control | 與被控系統通訊 | F：Cobalt Strike 遠端控制（S06） |
| Impact | 操縱、中斷或破壞 | D：勒索軟體大量加密（M12） |
- 注意：上表「案例對照」欄為本專案的教學分類，不是官方把案例歸入該戰術；官方事件描述多數沒有細到戰術層級。

## 相關真實案例
[[incident-a-ai-agent-attacks]]、[[incident-d-hospital-ransomware]]、[[incident-f-spoofed-legal-affairs-phishing]]。

## 可能造成的影響
- [推論] 越早在鏈上攔下，損害越小：在 Initial Access 擋下釣魚信，就不會走到後門與遠端控制。依據：F 案例鏈（釣魚 → 附檔 → 後門 → 遠端控制，S06）。

## 對應防禦措施（按階段）
- 入口階段：補漏洞、縮小對外暴露、郵件防護（S01、S05、S11）。
- 立足與擴張階段：最小權限、MFA、特權帳號分開、網段劃分（S05、S11）。
- 後段階段：EDR、日誌集中保存、備份備援與還原演練（S05）。

## 組織管理及改善建議
- [推論] 以戰術清單盤點「我們在每一階段有哪些偵測與阻擋」，缺口一目了然。依據：S18 以戰術為欄位組織攻擊行為。

## 相關知識連結
[[concept-social-engineering]]、[[concept-credential-attack]]、[[concept-ai-assisted-attack]]、[[concept-vulnerability-management]]

## 參考資料與來源
S18、S08、S11、S05、S06、S01；補充 M02、M12；擷取日 2026-11-21。
