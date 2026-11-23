---
id: concept-credential-attack
type: concept
module: 3
title: 帳號憑證攻擊：竊取、猜測與濫用帳號
tags: [帳號憑證, 弱密碼, 釣魚, 多因子驗證, 特權帳號]
related: [concept-social-engineering, concept-authentication-logic-flaw, incident-d-hospital-ransomware]
sources: [S05, S01]
supplementary_sources: [M02, M12]
last_verified: "2026-11-21"
stability: long-term
---
> 標記：[事實]=來源明確載明；[媒體轉述官方]；[推論]；[待確認]。

## 主題與概念介紹
憑證攻擊的目標是取得「合法身分」：用偷來的、猜中的或被繞過的帳號登入，而不是破壞系統本身。

## 基本原理
- [事實] 官方指出攻擊者未必需要全新技術，只要取得有效帳號或掌握可利用的弱點，就能進一步入侵（S05）。

## 技術分析（三條常見路徑）
1. 釣魚竊取：偽裝 SharePoint 通知的釣魚頁面，誘騙輸入 Microsoft 帳密（S05）。[事實]
2. 猜測弱密碼：馬偕事件中，攻擊者從 AD 下手，以弱密碼嘗試取得帳號權限，再大範圍發動加密。[媒體轉述官方] M12（轉述衛福部資訊處）；H-ISAC 原始警訊未取得。
3. 驗證邏輯被繞過：未完成憑證驗證即取得帳號維護權限（見 [[incident-e-forgot-account-auth-flaw]]）。[事實] S05

## 相關真實案例
[[incident-d-hospital-ransomware]]、[[incident-e-forgot-account-auth-flaw]]、[[incident-f-spoofed-legal-affairs-phishing]]。

## 可能造成的影響
- [事實] 事件 E 中，攻擊者以取得的帳號維護權限新增了帳號；這些帳號嘗試存取其他功能但被既有權限控管攔阻，未造成資料外洩（S05）。
- [媒體轉述官方] 取得網域管理權限後可派送惡意程式、大範圍加密（M02、M12）。

## 對應防禦措施
- [事實] 嚴密帳號管理：最小權限原則；遠端連線、電子郵件與管理員帳號優先導入多因子驗證或通行密鑰；定期清理閒置帳號；特權帳號與日常辦公帳號分開；盤點應用程式、服務帳號與存取憑證等「非人類身分」，定期檢視權限與憑證有效性，異常立即撤銷（S05）。
- [事實] 受駭後全面換發或廢止可能洩漏的金鑰、密碼與存取權杖，改用短時效憑證（S01）。

## 組織管理及改善建議
- [推論] 把「特權帳號清單、非人類身分清單、閒置帳號清理」做成定期審查項目，比事後換密碼更能縮小損害。依據：S05 與 S01 的建議均指向權限縮小與憑證時效縮短。

## 相關知識連結
[[concept-social-engineering]]、[[concept-authentication-logic-flaw]]、[[concept-ransomware]]

## 參考資料與來源
S05、S01；補充 M02、M12；擷取日 2026-11-21。
