---
id: concept-security-fundamentals
type: concept
module: 2
title: 資安基礎：資訊安全的定義、CIA 三要素與弱點
tags: [基礎, CIA, 機密性, 完整性, 可用性, 弱點]
related: [concept-attack-lifecycle, concept-vulnerability-management, concept-ransomware, concept-breach-notification]
sources: [S20, S21]
last_verified: "2026-11-21"
stability: long-term
---
> 標記：[事實]=來源明確載明；[推論]；[待確認]。本頁的定義來自 NIST 術語表（原文為英文，此處改寫為中文）；「威脅」「風險」的 NIST 定義尚未讀取，本頁先不寫。

## 主題與概念介紹
本頁是整份簡報的起點：先搞清楚「資安到底在保護什麼」，後面的事件才有共同的語言。

## 基本原理
- [事實] 資訊安全（information security）是保護資訊與資訊系統，避免未經授權的存取、使用、揭露、中斷、修改或破壞，以提供機密性、完整性與可用性（S20）。
- [事實] 三要素（S20 所載法定定義的改寫）：
  - 機密性（Confidentiality）：維持對存取與揭露的授權限制，包括保護個人隱私與專有資訊。
  - 完整性（Integrity）：防止資訊被不當修改或破壞，並確保不可否認性與真實性。
  - 可用性（Availability）：確保能及時且可靠地存取與使用資訊。
- [事實] 弱點（vulnerability）是資訊系統、安全程序、內部控制或實作上的缺陷，可能被威脅來源利用或觸發（S21）。NIST 術語表亦收錄其他來源的說法：弱點是「使威脅事件得以發生的條件」，也有軟體層面的定義：軟體中的錯誤或缺陷，會導致非預期行為；CVE 是列舉弱點的常用方式（S21）。

## 技術分析：用 CIA 看本 Wiki 的案例（教學對照）
下表是本專案的教學分類（推論），不是官方對事件的定性。

| 案例 | 最直接受影響的要素 | 依據 |
|---|---|---|
| 事件 A、B：個資與檔案外洩 | 機密性 | 官方描述為個資或檔案被取得（S01、S02） |
| 事件 C：款項被轉出 | 完整性（帳務被不當變更）＋機密性（帳戶權限被濫用）［推論］ | 銀行公告為「部分帳戶不明轉出款項」（S03） |
| 事件 D：勒索軟體加密 | 可用性（系統與檔案無法使用）；若同時竊資則連帶機密性 | 馬偕、彰基為勒索軟體攻擊（S04） |
| 事件 E：異常帳號被建立 | 完整性（帳號資料被不當新增） | 月報：影響限於異常帳號建立（S05） |

## 相關真實案例
[[incident-a-ai-agent-attacks]]、[[incident-b-boca-website-breach]]、[[incident-c-sinopac-abnormal-transfer]]、[[incident-d-hospital-ransomware]]、[[incident-e-forgot-account-auth-flaw]]。

## 可能造成的影響
- [推論] 同一個事件常同時影響多個要素；判斷時先問「最先壞掉的是哪一個」，再看後續連鎖。依據：事件 D 可能同時有加密（可用性）與竊資（機密性）疑慮（S04 並未說明是否竊資）。

## 對應防禦措施
- 對應要素的防禦：機密性（存取控制、加密、最小化蒐集）、完整性（驗證流程、日誌稽核）、可用性（備份備援、還原演練）。以上對照為教學歸納，具體做法見各概念頁：[[concept-credential-attack]]、[[concept-api-security]]、[[concept-incident-response]]、[[concept-ransomware]]。

## 組織管理及改善建議
- [推論] 盤點資產時，替每個資產標註「最在意哪一個 CIA 要素」，有助於決定備份、加密與存取控制的優先順序。依據：S20 把三者列為資訊安全要保護的目標。

## 相關知識連結
[[concept-attack-lifecycle]]、[[concept-vulnerability-management]]、[[concept-breach-notification]]

## 參考資料與來源
S20、S21（NIST CSRC 術語表）；案例依據 S01–S05；擷取日 2026-11-21。「威脅」「風險」的定義待補。
