---
id: concept-api-security
type: concept
module: 5
title: API 安全：為什麼 API 成為攻擊熱區（OWASP API Top 10 2023 與臺灣官方觀察）
tags: [API, OWASP, 授權, 速率限制, BOLA]
related: [incident-a-ai-agent-attacks, incident-e-forgot-account-auth-flaw, concept-authentication-logic-flaw, concept-vulnerability-management]
sources: [S17, S05, S01]
last_verified: "2026-11-21"
stability: long-term
---
> 標記：[事實]=來源明確載明；[推論]；[待確認]。S17 只讀到十項風險總表，未讀各風險子頁，故本頁不引用子頁的攻擊範例與防護細節。

## 主題與概念介紹
API（Application Programming Interface）是程式之間交換資料的入口，網站與 App 的資料多半經由 API 取得。入口一旦授權不嚴，攻擊者不必攻破整台系統，就能用「正常呼叫」大量取資料。

## 基本原理
- [事實] 臺灣官方觀察：API 成為攻擊熱區，因為透過 API 取得大量資料相對容易，且部分 API 具有較高權限，一旦受駭容易造成重大衝擊（S05）。
- [事實] 資安署也指出攻擊者透過「高權限、可大量存取資料的 API」取得大量個資（S01）。

## 技術分析：OWASP API Security Top 10（2023）
| 編號 | 風險 | 一句話 |
|---|---|---|
| API1 | Broken Object Level Authorization | 凡是用使用者給的 ID 去存取資料的功能，都要檢查「這個人能不能碰這個物件」 |
| API2 | Broken Authentication | 驗證機制實作不當，攻擊者可竊取權杖或冒用他人身分 |
| API3 | Broken Object Property Level Authorization | 沒有在「欄位層級」做授權，導致資訊外露或被竄改（合併了 2019 年的過度資料暴露與大量賦值） |
| API4 | Unrestricted Resource Consumption | 沒限制資源用量，可能造成服務中斷或營運成本暴增（含按次付費的簡訊、電話等） |
| API5 | Broken Function Level Authorization | 管理功能與一般功能分界不清，使用者可取得他人資源或管理功能 |
| API6 | Unrestricted Access to Sensitive Business Flows | 業務流程（如買票、發文）被自動化濫用 |
| API7 | Server Side Request Forgery | 伺服器抓取使用者提供的網址卻不驗證，被誘導向非預期目的地發請求 |
| API8 | Security Misconfiguration | 設定複雜，容易漏設或未依最佳實務 |
| API9 | Improper Inventory Management | 端點多、版本多，若沒有最新清單，舊版與除錯端點會暴露 |
| API10 | Unsafe Consumption of APIs | 對第三方 API 回傳的資料過度信任，攻擊者轉攻整合的第三方服務 |
（以上皆為 S17 對各風險的描述，用中文改寫。）

## 相關真實案例
- [[incident-a-ai-agent-attacks]]：官方指出高權限、可大量存取資料的 API 被用來取得大量個資（S01、S05）。
- [推論] 這類情境可能對應 API1、API3、API4、API5 等類型，但官方未說明各案實際屬於哪一類。依據：S01 的「高權限、可大量存取」描述與 S17 的風險定義；此為教學對照，不是官方分類。
- [[incident-e-forgot-account-auth-flaw]]：驗證邏輯被繞過，對應 API2 的「驗證機制實作不當」概念（推論）。

## 可能造成的影響
- [事實] 大量個資外洩、營運成本增加或服務中斷（S17 對 API4、API1 的描述）。

## 對應防禦措施
- [事實] 月報建議：依各 API 的業務特性與敏感層級設定請求頻率、連線流量或數量限制，可針對使用者、帳號、來源 IP 或 API Key 控管；短時間內暴增的異常查詢，建立自動阻擋或告警（S05）。
- [事實] 月報建議：重要功能由後端伺服器驗證，不得僅依前端參數或流程狀態放行（S05）。
- [事實] 官方要求加強系統權限及資料存取管理（S01）。
- [推論] 資料回傳應只含必要欄位，並建立 API 資產清單（對應 API3、API9）。依據：S17 的風險定義與 S01 的個資最小化原則。

## 組織管理及改善建議
- [推論] 把 API 清單、各 API 的敏感等級與權限範圍納入資產盤點與定期稽核。依據：S05 以資產盤點為縮小攻擊面的起點，S17 API9 強調清單的重要性。

## 相關知識連結
[[concept-authentication-logic-flaw]]、[[concept-vulnerability-management]]、[[concept-ai-assisted-attack]]、[[incident-a-ai-agent-attacks]]

## 參考資料與來源
S17（OWASP API Security Top 10 2023）、S05、S01；另見 S07 專案頁；擷取日 2026-11-21。
