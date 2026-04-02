---
name: pms-erpnext-integration-context
description: Domain context for BA analysis of PMS ↔ ERPNext/Frappe CRM synchronization. Covers hotel PMS business logic, ERPNext business architecture, integration intersection points, document types for BA review, clarification questions, and common sync risks. Use when the user needs to analyze, review, or produce integration documentation between a hotel PMS and ERPNext.
---

# PMS ↔ ERPNext Integration Analysis Context

> Tài liệu này cung cấp kiến thức nghiệp vụ và khung phân tích cho BA khi đọc, đánh giá, hoặc tạo tài liệu đồng bộ giữa hệ thống PMS khách sạn và ERPNext (Frappe). Không chứa code, schema, hoặc hướng dẫn cấu hình.

---

## Phần 1: Hiểu biết nghiệp vụ PMS khách sạn

### 1.1 Vòng đời đặt phòng và lưu trú (Reservation Lifecycle)

Mọi hoạt động trong PMS xoay quanh vòng đời của một reservation. BA cần nắm rõ các giai đoạn và chuyển đổi trạng thái sau:

**Các trạng thái chính:**

| Giai đoạn | Trạng thái | Ý nghĩa nghiệp vụ |
|-----------|-----------|-------------------|
| Pre-arrival | Prospect / Tentative / Confirmed | Đặt phòng đã được ghi nhận nhưng khách chưa đến |
| Pre-arrival | Waiting List / Holding List | Đặt phòng chờ xác nhận hoặc đang giữ chỗ tạm |
| In-house | In-House (Checked-in) | Khách đã nhận phòng, đang lưu trú |
| Post-stay | Checked-out | Khách đã trả phòng, folio đã đóng |
| Exception | Cancelled | Đặt phòng bị hủy trước hoặc sau ngày đến |
| Exception | No-show | Khách không đến mà không báo trước |

**Đặc điểm quan trọng cho đồng bộ:**

- Trạng thái là **một chiều và không hoàn toàn tuyến tính**: một reservation có thể nhảy từ Confirmed → Cancelled mà không qua In-house. Tuy nhiên, một số PMS hỗ trợ Recovery (phục hồi từ Cancelled → trạng thái trước đó).
- **Check-in là điểm ngoặt dữ liệu**: trước check-in, thông tin khách thường chưa đầy đủ (đặc biệt với OTA). Tại check-in, hotel thu thập passport, địa chỉ, thông tin immigration → đây là thời điểm dữ liệu khách hoàn chỉnh nhất.
- **Check-out là điểm đóng tài chính**: tất cả charges phải được reconciled, folio phải cân bằng trước khi trả phòng. Sau check-out, reservation trở thành read-only.

### 1.2 Các thực thể nghiệp vụ cốt lõi

#### Guest / Profile
- Đại diện cho một cá nhân trong hệ thống PMS.
- Mỗi hotel (property) thường có PMS instance riêng → **cùng một khách vật lý có thể có nhiều ProfileId ở các hotel khác nhau**. Đây là điểm then chốt khi đồng bộ sang hệ thống tập trung.
- Profile chứa: thông tin cá nhân, ID/passport, quốc tịch, VIP status, membership, preferences, blacklist, consent.
- **Profile Merge**: PMS cho phép gộp hai profile trùng lặp → hệ thống sẽ phát hai sự kiện: xóa profile bị gộp + cập nhật profile còn lại. BA cần xác nhận hệ thống đồng bộ xử lý cặp sự kiện này đúng thứ tự.

#### Reservation / Booking
- Là hợp đồng lưu trú giữa khách và hotel cho một khoảng thời gian xác định.
- Chứa: room type, rate plan, package, số đêm, số khách (adult/child/infant), arrival/departure, channel, segment, source.
- Một reservation có thể gắn với **nhiều guest** (main guest + accompanying guests). BA cần xác nhận mối quan hệ 1-N này được xử lý trong mapping.
- Reservation liên kết chéo với: folio (tài khoản thu), rate contract, travel agent, group/party booking.

#### Folio
- Tài khoản tài chính gắn với reservation.
- Ghi lại mọi charges (room, F&B, minibar, spa, laundry...) và payments.
- Một reservation có thể có nhiều folio windows (A, B, C...) — cho phép tách bill theo mục đích (ví dụ: folio A = room do công ty trả, folio B = minibar khách tự trả).
- **Folio routing / Special Billing**: quy tắc tự động chuyển charge từ folio này sang folio khác, vô cùng phổ biến với group booking. BA cần đặc biệt chú ý khi map sang hệ thống ERP vì logic routing này thường không có sẵn.

#### Room
- Master data: room number, room type (category), building/wing/floor, view, bed type, connecting rooms, special features.
- Room status (housekeeping): Vacant Clean (VC), Vacant Dirty (VD), Occupied Clean (OC), Occupied Dirty (OD), Out of Order (OO), Out of Inventory (OI), Out of Service (OS).
- Room status là dữ liệu thay đổi liên tục (housekeeping cập nhật realtime). BA cần xác nhận: đồng bộ room status có cần thiết cho CRM/ERP không, hay chỉ cần master data tĩnh.

#### Rate Plan / Contract
- Xác định giá phòng cho từng room type, từng ngày, từng channel.
- Có nhiều loại: BAR (Best Available Rate), Corporate, Government, Package, Promotional.
- Rate có thể thay đổi theo ngày → mỗi đêm trong cùng một reservation có thể có giá khác nhau (DailyRates).
- Contract rate liên kết với Company/Agent → BA cần xác nhận mối tương quan giữa "Contract" trong PMS và "Customer" type corporate trong ERP.

#### POS Posting / Incidental Charges
- Các chi phí phát sinh trong thời gian lưu trú: F&B, spa, minibar, laundry, telephone, business center.
- Charge có thể đến từ POS system (nhà hàng, bar) hoặc posting thủ công (minibar, laundry).
- POS charges cho in-house guest được post vào folio của reservation. POS charges cho walk-in (không có reservation) tạo transaction riêng.

#### Payment / Deposit
- Deposit: khoản tiền khách trả trước (advance payment), thường khi booking hoặc check-in.
- Payment: thanh toán khi check-out hoặc trong quá trình lưu trú.
- Refund: hoàn tiền deposit khi hủy hoặc thay đổi.
- Payment methods: cash, credit card, bank transfer, city ledger (AR), voucher.

#### Group / Party Booking
- Group: nhiều reservations thuộc cùng một nhóm (đoàn, hội nghị).
- Party: tương tự group nhưng thường dùng cho events nhỏ hơn.
- Group có master room (phòng chính) nơi charges chung được gom.
- BA cần xác nhận: group/party booking được biểu diễn như thế nào ở phía ERP — là một đối tượng riêng hay là thuộc tính của Sales Order.

### 1.3 Kênh phân phối (Distribution Channels)

**Tại sao quan trọng cho đồng bộ**: Kênh booking quyết định **chất lượng dữ liệu khách** và **thời điểm đồng bộ**.

| Kênh | Chất lượng dữ liệu khách | Thời điểm có dữ liệu đầy đủ |
|------|--------------------------|----------------------------|
| OTA (Booking.com, Agoda, Expedia) | Thấp — tên có thể alias, email là proxy, không có passport | Chỉ khi check-in |
| Website khách sạn | Trung bình — email/phone thật, nhưng thường chưa có passport | Booking hoặc check-in |
| Walk-in | Cao — thu thập trực tiếp tại quầy | Ngay lúc booking |
| Direct (phone, email) | Trung bình — tùy quy trình thu thập | Booking hoặc check-in |
| Travel Agent (GDS) | Trung bình — thông tin qua trung gian | Check-in |

**Hệ quả thiết kế**: Hệ thống đồng bộ phải có **logic rẽ nhánh theo channel** — không thể áp dụng cùng một luồng xử lý cho mọi kênh booking.

### 1.4 PMS phối hợp với hệ thống khác

PMS là trung tâm vận hành, kết nối với:

| Hệ thống | Vai trò | Dữ liệu trao đổi |
|----------|---------|-------------------|
| Channel Manager | Quản lý rate/availability trên OTA | Room availability, rates, restrictions ↔ Reservations |
| POS (F&B, Spa, Retail) | Ghi nhận doanh thu dịch vụ | Charges posted to guest folio |
| Payment Gateway | Xử lý thanh toán | Authorization, capture, refund |
| Housekeeping | Quản lý trạng thái phòng | Room status updates |
| Key Card System | Tạo thẻ phòng | Room assignment, check-in/out events |
| Accounting | Báo cáo tài chính | Night audit, revenue posting, city ledger |
| CRM/ERP | Quản lý khách hàng, vận hành | Guest profile, booking, charges (đây là phạm vi đồng bộ) |

**BA cần xác nhận**: trong scope đồng bộ, những hệ thống nào đã kết nối trực tiếp với PMS và dữ liệu nào sẽ đi qua PMS → ERP vs. đi trực tiếp vào ERP từ nguồn khác.

---

## Phần 2: Hiểu biết ERPNext / Frappe

### 2.1 Kiến trúc logic Frappe Framework

**DocType — đơn vị cơ bản**: Mọi thứ trong Frappe/ERPNext đều xoay quanh DocType. Một DocType tương đương một business entity với data model, form view, list view, workflow, và permission built-in. BA cần hiểu:

- **Standard DocType**: có sẵn trong ERPNext (Customer, Contact, Sales Order, Sales Invoice, Payment Entry, Item, Address...). Có thể thêm custom fields nhưng không nên thay đổi behavior gốc.
- **Custom DocType**: tạo hoàn toàn mới cho nghiệp vụ đặc thù (ví dụ: Hotel Room, Registration, PMS Profile Map). BA cần liệt kê Custom DocTypes cần tạo và lý do.
- **Child Table**: DocType dạng bảng con, chỉ tồn tại bên trong DocType cha (ví dụ: Sales Order Item là child table của Sales Order). Khi map dữ liệu từ PMS, array/nested objects thường thành child table.

**Workflow**: Frappe hỗ trợ workflow engine cho trạng thái của document (Draft → Submitted → Cancelled). BA cần nắm:
- Sales Order có 3 trạng thái Frappe bắt buộc: Draft, Submitted, Cancelled.
- Draft cho phép chỉnh sửa tự do → phù hợp cho reservation status 0-7 (booking đến in-house).
- Submitted → khóa record, bắt đầu tạo Sales Invoice → phù hợp cho check-out.
- Cancelled → hủy bỏ, không xóa dữ liệu.
- **Lưu ý quan trọng**: trạng thái Frappe (Draft/Submitted/Cancelled) KHÔNG map 1:1 với trạng thái PMS. BA cần rõ ràng mapping giữa hai hệ thống trạng thái.

**Permission & Role**: Frappe quản lý quyền truy cập theo Role + DocType + mức hành động (read/write/create/delete/submit/cancel). BA cần xác nhận: ai có quyền sửa record do sync tạo ra, và logic sync chạy dưới role/user nào.

**Notification & Activity**: Frappe ghi lại mọi thay đổi trên document (activity log). BA có thể tận dụng để audit trail cho sync events.

### 2.2 ERPNext như CRM và platform vận hành

Trong ngữ cảnh đồng bộ PMS, ERPNext đóng vai trò:

**Quản lý khách hàng (CRM):**
- **Contact**: lưu thông tin cá nhân — tên, email, phone, passport, quốc tịch. Một Contact có thể link với nhiều Customer.
- **Customer**: đại diện cho mối quan hệ kinh doanh — một khách hàng có lịch sử giao dịch, hạn mức, điều khoản thanh toán. Customer link với Contact.
- **Address**: địa chỉ, có thể gắn với Contact hoặc Customer. Hỗ trợ nhiều loại: billing, shipping (residential/working trong ngữ cảnh hotel).
- **Quan hệ Contact ↔ Customer**: Trong ERPNext standard, mối quan hệ là N:N (nhiều Contact có thể link 1 Customer, 1 Contact có thể link nhiều Customer). BA cần xác nhận thiết kế cụ thể: 1 Contact = 1 Customer (đơn giản) hay 1 Contact có thể là khách của nhiều Customer entities.

**Quản lý giao dịch:**
- **Sales Order**: đơn hàng, trong ngữ cảnh hotel = reservation. Chứa items (room, services), giá, các điều kiện.
- **Sales Invoice**: hóa đơn, tạo từ Sales Order khi check-out.
- **Payment Entry**: ghi nhận thanh toán/deposit.
- **Item**: sản phẩm/dịch vụ (room category, F&B item, spa service). Mỗi room type trở thành 1 Item trong ERPNext.

**Quản lý đa công ty (Multi-Company):**
- ERPNext hỗ trợ multi-company natively: mỗi Sales Order, Sales Invoice, Payment Entry thuộc 1 Company.
- Trong ngữ cảnh hotel chain, mỗi hotel branch = 1 Company.
- **Hệ quả**: Customer/Contact là toàn cục (cross-company), nhưng giao dịch thuộc về từng Company. Đây là nền tảng cho consolidation lịch sử khách qua nhiều hotel.

### 2.3 Các đặc tính của Frappe ảnh hưởng đến đồng bộ

| Đặc tính | Ảnh hưởng |
|----------|-----------|
| DocType naming rule | Mỗi document có name unique (auto hoặc custom pattern). Sync logic cần quyết định: dùng PMS ID làm primary key hay để Frappe auto-generate + lưu PMS ID trong custom field. |
| Amendment flow | Frappe không cho phép sửa Submitted document → phải Cancel + Amend. Nếu check-out rồi cần sửa → phải cancel invoice + sửa SO + submit lại. |
| Link field validation | Khi tạo Sales Order, Customer phải tồn tại trước. BA cần xác nhận thứ tự sync: master data → transactional data. |
| Background Jobs | Frappe xử lý async qua background workers (RQ). Sync webhook nên được xử lý async để không block API response. |
| Idempotency | Frappe không có native idempotency cho API calls. Sync logic phải tự handle: cùng 1 event gửi 2 lần không được tạo 2 records. |

---

## Phần 3: Điểm giao nhau khi đồng bộ PMS ↔ ERPNext

### 3.1 Mapping thực thể

| PMS Entity | ERPNext DocType(s) | Ghi chú |
|-----------|-------------------|---------|
| Guest Profile | Contact + Customer | 1 guest = 1 Contact. Customer tạo kèm hoặc link tới Contact đã có. |
| Profile (per hotel) | PMS Profile Map (child of Contact) | Mỗi hotel ghi 1 row vào child table để map ngược về PMS ProfileId. |
| Reservation | Sales Order | 1 reservation = 1 Sales Order (Draft). Check-out → Submit. |
| Room charges + Services | Sales Order Item (child table) | Room category là Item chính, services append thêm trong quá trình lưu trú. |
| Folio / Invoice | Sales Invoice | Tạo tại check-out từ Sales Order. |
| Deposit / Payment | Payment Entry | Link tới Sales Order hoặc Sales Invoice. |
| Room | Hotel Room (Custom) + Item | Hotel Room lưu physical room. Item lưu room category (type). |
| Group Booking | Booking Group (Custom) | Link từ Sales Order. |
| POS Order | Sales Order Item (append) hoặc Sales Invoice Item (walk-in) | Tùy khách có reservation hay không. |

### 3.2 Xác định Source of Truth

**Nguyên tắc chung**: mỗi field phải có MỘT source of truth duy nhất. BA cần xác định rõ cho từng field:

| Loại dữ liệu | Source of Truth | Ghi chú |
|--------------|----------------|---------|
| Thông tin đặt phòng (dates, room type, rate) | PMS | PMS vận hành realtime, ERP nhận để lưu trữ. |
| Thông tin khách (tên, passport, phone, email) | Phân cấp — ERP ưu tiên nếu đã có, PMS bổ sung nếu trống | ERP là golden record cho CRM; PMS chỉ bổ sung, không ghi đè. |
| Trạng thái reservation | PMS | PMS phát sự kiện, ERP cập nhật theo. |
| Tài chính (charges, payments, invoices) | PMS (nguồn) → ERP (ghi nhận) | Số liệu tài chính phải khớp; ERP không tự tạo charge. |
| Membership / Loyalty | ERP (nếu có chương trình riêng) hoặc PMS | Cần xác nhận với stakeholder. |
| Master data (room, rate) | PMS | Sync one-way PMS → ERP. |

### 3.3 Thứ tự đồng bộ (Dependency Chain)

BA cần xác nhận đồng bộ theo đúng thứ tự phụ thuộc:

```
1. Master Data (prerequisite — sync trước, ít thay đổi)
   ├── Room Type → Item (tạo Item cho mỗi room category)
   ├── Room → Hotel Room (tạo record cho mỗi phòng vật lý)
   └── Company → Company (mapping hotel branch)

2. Guest Data (sync khi có event)
   ├── Profile → Contact + Customer
   └── Address → Address (link to Contact)

3. Transactional Data (phụ thuộc vào 1 + 2)
   ├── Reservation → Sales Order (cần Item + Customer đã tồn tại)
   ├── POS Order → Sales Order Item hoặc Sales Invoice Item
   ├── Deposit → Payment Entry (cần Sales Order đã tồn tại)
   └── Check-out → Sales Invoice (cần Sales Order đã Submit)
```

**Rủi ro**: nếu thứ tự sai (ví dụ: nhận reservation trước khi Item room type được tạo), sync sẽ fail. BA cần xác nhận có mechanism xử lý dependency failure (retry, queue, manual resolve).

### 3.4 Xác định Guest — Bài toán multi-hotel

**Bối cảnh**: Mỗi hotel PMS instance là độc lập → cùng 1 khách có ProfileId khác nhau ở mỗi hotel. ERPNext cần gộp thành 1 Contact duy nhất.

**Matching logic**: BA cần xác nhận strategy matching với thứ tự ưu tiên rõ ràng:
1. **Exact match trên PMS Profile Map** (CompanyId + ProfileId) → đã biết khách này ở hotel này
2. **Exact match trên unique identifiers** (Passport number, National ID, Member card number)
3. **Soft match** (email, phone + last name) → cần flagging để review thủ công
4. **No match** → tạo Contact mới

**Câu hỏi BA cần đặt:**
- Khi soft match, ai confirm: staff tự động hay cần approval?
- Nếu match sai (gộp 2 khách khác nhau), quy trình rollback là gì?
- Passport number có thể thay đổi (gia hạn, đổi quốc tịch) — xử lý thế nào?
- Khách OTA dùng tên giả — có lưu tên giả không, hay chờ check-in mới lưu tên thật?

### 3.5 Timing — Khi nào đồng bộ cái gì

BA cần mapping rõ ràng giữa **PMS event** → **hành động đồng bộ** → **ERPNext document affected**:

| PMS Event | Timing | Action trên ERPNext | Điều kiện |
|-----------|--------|--------------------|-----------| 
| profile.created | Realtime | Tạo/cập nhật Contact + Customer | Chỉ nếu channel ≠ OTA |
| profile.updated | Realtime | Cập nhật Contact (bổ sung, không ghi đè) | Chỉ nếu channel ≠ OTA |
| profile.merged | Realtime | Xóa profile bị gộp, cập nhật profile còn lại | Cần xử lý cặp event đúng thứ tự |
| reservation.created | Realtime | Tạo Sales Order (Draft) | Customer link tùy channel |
| reservation.updated | Realtime | Cập nhật Sales Order | Chỉ nếu còn Draft |
| reservation.checked_in | Realtime | Sync Contact (nếu OTA), cập nhật SO (room, occupants) | Thời điểm có passport |
| reservation.stay_updated | Realtime | Append Items vào Sales Order | Charges mới phát sinh |
| reservation.checked_out | Realtime | Submit Sales Order → Tạo Sales Invoice | Folio phải cân bằng |
| reservation.cancelled | Realtime | Cancel Sales Order | Nếu OTA + chưa có Contact → clean |
| reservation.noshow | Realtime | Cancel Sales Order + flag no-show | Tương tự Cancelled |
| reservation.recovery | Realtime | Un-cancel → Draft | Cần xác nhận Frappe có support un-cancel không |
| order.created / completed | Realtime | Append Items vào SO (in-house) hoặc tạo SI (walk-in) | Cần xác định guest có reservation không |

---

## Phần 4: Các loại tài liệu cần BA phân tích

### 4.1 Tài liệu từ phía PMS

| Loại | Nội dung cần chú ý | Rủi ro nếu thiếu/mơ hồ |
|------|--------------------|-----------------------|
| API Dictionary / Data Dictionary | Định nghĩa fields, data types, enums, nullable, required | Thiếu enum values → mapping sai; thiếu nullable info → crash khi null |
| Webhook Event Catalog | Danh sách events, payload structure, trigger conditions | Không biết khi nào event fire → logic sync sai timing |
| Business Rules / Status Matrix | Quy tắc chuyển trạng thái, ràng buộc nghiệp vụ | Không xử lý edge cases (cancel → recovery, no-show) |
| Authentication & Security specs | Phương thức auth (API key, HMAC, OAuth), rate limits | Lỗi bảo mật hoặc bị rate-limited khi cao tải |
| Error Handling specs | Error codes, retry policy, partial failure handling | Không biết retry → duplicate records hoặc mất dữ liệu |

### 4.2 Tài liệu từ phía ERPNext

| Loại | Nội dung cần chú ý | Rủi ro nếu thiếu/mơ hồ |
|------|--------------------|-----------------------|
| DocType specifications | Các DocType cần tạo/customize, field definitions | Không rõ data model đích → mapping sai |
| Workflow definitions | Trạng thái, transitions, permissions | Sync có thể vi phạm workflow rules |
| Multi-company setup | Company hierarchy, naming conventions | Giao dịch gắn sai company |
| Naming rules | Document naming patterns (auto, custom) | ID collision hoặc không trace được nguồn PMS |
| Permission matrix | Ai được làm gì trên DocType nào | Sync user không có quyền → silent failure |

### 4.3 Tài liệu tích hợp (Integration Specs)

| Loại | Nội dung cần chú ý |
|------|-------------------|
| Data Mapping Matrix | Mapping field-by-field PMS → ERPNext, bao gồm transformation rules |
| Sync Flow Diagrams | Sequence diagrams cho từng event, bao gồm happy path + error path |
| Decision Matrix | Bảng quyết định cho từng tình huống (OTA vs. direct, new vs. existing guest) |
| Exception Handling Plan | Xử lý khi sync fail, khi dữ liệu conflict, khi thiếu prerequisite |
| Reconciliation Procedure | Cách verify dữ liệu 2 bên khớp nhau sau sync |

---

## Phần 5: Câu hỏi cần làm rõ với nghiệp vụ

### 5.1 Về phạm vi (Scope)

1. **Chiều đồng bộ**: Chỉ PMS → ERPNext (one-way), hay có luồng ngược ERPNext → PMS? Ví dụ: khi sửa thông tin khách trên ERPNext, có push ngược về PMS không?
2. **Dữ liệu nào trong scope**: Room master data, guest profile, reservation, POS, payment — tất cả hay chỉ một phần? Housekeeping status có sync không?
3. **Dữ liệu lịch sử**: Có cần migrate dữ liệu cũ từ PMS sang ERPNext không, hay chỉ sync từ thời điểm go-live?
4. **Frequency**: Realtime (webhook), near-realtime (polling mỗi X phút), hay batch (daily)?

### 5.2 Về nghiệp vụ khách hàng (Guest / CRM)

5. **Matching strategy final**: Thứ tự ưu tiên matching fields đã xác nhận chưa? Có trường hợp nào cần manual approval không?
6. **OTA Guest handling**: Khi khách OTA no-show, Sales Order cancel mà chưa bao giờ có Contact — có tạo Contact "anonymous" không hay để trống?
7. **Guest data conflict**: Khi PMS gửi email/phone khác với ERPNext hiện có, quy tắc resolve cụ thể là gì? Ghi đè, giữ cũ, hay tạo log conflict?
8. **Blacklist**: Khách bị blacklist trên PMS → hành động gì trên ERPNext? Cảnh báo, block booking, hay chỉ đánh dấu?
9. **Consent / PDPA**: Dữ liệu consent từ PMS có chuyển sang ERPNext không? ERPNext có cần enforce consent trước khi gửi marketing?

### 5.3 Về tài chính (Financial)

10. **Revenue recognition**: ERPNext ghi nhận doanh thu vào thời điểm nào — khi charge phát sinh (accrual) hay khi thanh toán (cash basis)?
11. **Currency**: Multi-currency support? Nếu khách trả USD nhưng hotel sổ sách bằng THB, ai quyết định exchange rate — PMS hay ERPNext?
12. **Tax handling**: PMS tính tax hay ERPNext tự tính? Nếu cả hai, làm sao đảm bảo số liệu khớp?
13. **Deposit lifecycle**: Deposit từ PMS map vào Payment Entry type nào — Advance Payment, hay Journal Entry?
14. **Group billing / Folio routing**: Khi charges của nhiều phòng gom về 1 master folio — Sales Invoice tạo cho ai, Customer nào?

### 5.4 Về vận hành (Operations)

15. **Downtime handling**: Khi ERPNext hoặc PMS maintenance → webhook miss → cơ chế catch-up/replay là gì?
16. **Conflict resolution SLA**: Khi sync fail hoặc conflict → ai xử lý (staff, admin, auto) và trong bao lâu?
17. **Audit requirements**: Cần log gì cho mỗi sync event? Retention period bao lâu?
18. **Performance**: Peak load (high season, check-out rush 10:00-12:00) có bao nhiêu events/phút? Hệ thống chịu được không?

### 5.5 Về ngoại lệ (Exceptions)

19. **Early check-out / Late check-out**: Thay đổi departure date giữa chừng → Sales Order đã có items cho đêm chưa ở → xử lý thế nào?
20. **Room move**: Khách đổi phòng giữa chừng → Hotel Room link thay đổi → có tạo record mới hay cập nhật record cũ?
21. **Day-use reservation**: Khách ở ban ngày, không qua đêm (check-in + check-out cùng ngày) → Nights = 0 → tính charges thế nào?
22. **Walk-in POS**: Khách vào nhà hàng hotel nhưng không có reservation → POS order không gắn được ProfileId → tạo SI trực tiếp hay tạo Contact rồi mới tạo SI?

---

## Phần 6: Rủi ro và ngoại lệ thường gặp khi đồng bộ

### 6.1 Rủi ro dữ liệu

| Rủi ro | Mô tả | Hậu quả | Biện pháp giảm thiểu |
|--------|-------|---------|---------------------|
| Duplicate Contact | Matching sai hoặc thiếu → tạo 2 Contact cho 1 khách | Report sai, member benefits sai | Strict matching rules + periodic dedup review |
| Orphan Sales Order | OTA booking cancel → SO không có Customer link → rác | DB clutter, report nhiễu | Cleanup job định kỳ |
| Data conflict | PMS gửi phone mới, ERPNext đã có phone cũ | Không biết số nào đúng | Source-of-truth rule rõ ràng + conflict log |
| Stale data | PMS cập nhật nhưng webhook fail → ERPNext out-of-date | Thông tin cũ, quyết định sai | Retry + reconciliation check |
| ID collision | PMS RecordId trùng giữa 2 hotel instance | Sales Order link sai | Composite key (CompanyId + RecordId) |
| Encoding issues | Tên khách Unicode (Thai, Vietnamese, Chinese) bị lỗi | Tên hiển thị sai | UTF-8 enforcement end-to-end |

### 6.2 Rủi ro luồng xử lý

| Rủi ro | Mô tả | Hậu quả | Biện pháp giảm thiểu |
|--------|-------|---------|---------------------|
| Out-of-order events | Webhook checked_out đến trước stay_updated → SO chưa có charge cuối | Invoice thiếu charges | Queue + ordering by timestamp hoặc sequence |
| Race condition | 2 events cho cùng 1 reservation đến đồng thời | Data inconsistency | Locking hoặc sequential processing per reservation |
| Partial failure | Tạo Contact thành công nhưng tạo Customer fail | Contact không có Customer link | Transaction-like handling: rollback hoặc compensate |
| Recovery paradox | PMS cancel → ERPNext cancel SO → PMS recovery → ERPNext cần un-cancel | Frappe không native un-cancel | Xác nhận approach: tạo SO mới hay amend |
| Webhook loss | Network issue → PMS gửi nhưng ERPNext không nhận | Dữ liệu mất | Retry from PMS + periodic reconciliation |

### 6.3 Rủi ro nghiệp vụ

| Rủi ro | Mô tả | Hậu quả |
|--------|-------|---------|
| Folio balance ≠ 0 tại check-out | PMS cho check-out nhưng folio chưa cân bằng | Sales Invoice có outstanding amount — cần xác nhận có tạo AR entry không |
| Group billing complexity | Charges routing giữa các phòng trong group | ERPNext Sales Order model không native support folio routing |
| Rate change after booking | Khách upgrade room giữa chừng → rate thay đổi | DailyRates entries trước và sau không nhất quán → cần recalculate |
| Profile merge sau khi đã có transactions | PMS gộp 2 profile → ERPNext có 2 Contact với SO riêng | Cần merge Contact trên ERPNext + re-link SO → phức tạp |
| Multi-property loyalty | Điểm loyalty tích từ nhiều hotel → 1 account | ERPNext Loyalty Program có support multi-company không? Cần xác nhận |

---

## Phần 7: Khung phân tích cho BA

### 7.1 Checklist khi nhận tài liệu đồng bộ mới

Khi nhận bất kỳ tài liệu nào liên quan đến đồng bộ PMS ↔ ERPNext, BA nên kiểm tra:

- [ ] **Scope rõ ràng**: Tài liệu nói về entities nào, events nào, chiều sync nào?
- [ ] **Mapping đầy đủ**: Mỗi field từ PMS có target field trên ERPNext không? Có field nào unmapped?
- [ ] **Transformation rules**: Có field nào cần chuyển đổi (enum → text, ID → Link, concatenation)?
- [ ] **Xử lý null/empty**: Khi PMS gửi field rỗng, ERPNext xử lý thế nào — bỏ qua, set default, hay xóa giá trị cũ?
- [ ] **Thứ tự phụ thuộc**: Có dependency chain rõ ràng và được enforce?
- [ ] **Error handling**: Mỗi bước sync fail thì sao — retry, skip, alert, hay block cả flow?
- [ ] **Idempotency**: Cùng 1 event gửi 2 lần có an toàn không?
- [ ] **Edge cases**: Tài liệu có cover: no-show, cancel, recovery, group booking, walk-in POS, day-use?
- [ ] **Performance**: Có ước lượng throughput không? Peak load handling?
- [ ] **Reconciliation**: Có cơ chế verify dữ liệu 2 bên khớp post-sync?

### 7.2 Template đánh giá field mapping

Khi review một bảng mapping field, BA nên bổ sung các cột đánh giá:

| PMS Field | ERPNext Field | Data Type Match? | Nullable? | Transform Needed? | Source of Truth | Gap/Concern |
|-----------|--------------|-----------------|-----------|-------------------|----------------|-------------|
| _(fill)_ | _(fill)_ | Yes/No | Yes/No | Description | PMS/ERPNext | _(fill)_ |

### 7.3 Template đánh giá luồng đồng bộ

Khi review một luồng sync, BA nên verify:

| Tiêu chí | Đánh giá | Ghi chú |
|----------|----------|---------|
| Trigger event rõ ràng | ✅/⚠️/❌ | Sự kiện nào từ PMS trigger flow này? |
| Prerequisites xác định | ✅/⚠️/❌ | Những gì phải tồn tại trước khi flow chạy? |
| Happy path mô tả đủ | ✅/⚠️/❌ | Luồng chính có đủ chi tiết? |
| Error path mô tả đủ | ✅/⚠️/❌ | Khi fail thì sao? |
| Idempotent | ✅/⚠️/❌ | Chạy 2 lần có safe không? |
| Source of Truth rõ | ✅/⚠️/❌ | Mỗi field biết lấy từ đâu? |
| Edge cases covered | ✅/⚠️/❌ | OTA, group, walk-in, cancel, recovery? |

---

## Phụ lục: Ví dụ nghiệp vụ minh họa

### Ví dụ A: OTA Booking → Check-in → Check-out (Happy Path)

1. Khách A book phòng Deluxe 3 đêm qua Booking.com → PMS nhận reservation, tạo ProfileId=500 (Hotel Saigon, CompanyId=1).
2. PMS fire `reservation.created` (Status=2, ChannelCode=BCOM) → ERPNext tạo Sales Order (Draft), Item = RM-DELUXE, Qty=3 nights. **Không tạo Contact** vì OTA, lưu `ota_guest_name="Mr. Booking"`, `pending_guest_sync=true`.
3. Khách đến check-in, xuất trình passport AB123456 → PMS fire `reservation.checked_in` → ERPNext: Tìm Contact theo PassportNo → Không tìm thấy → Tạo Contact mới (PassportNo=AB123456, tên thật từ passport) + Customer + PMS Profile Map row (CompanyId=1, ProfileId=500). Update Sales Order: gắn Customer link, assign RoomNo=301, xóa `pending_guest_sync`.
4. Ngày 2, khách ăn tối nhà hàng, charge 2,500 THB → PMS fire `order.completed` → ERPNext: Append Item "F&B-REST01" vào Sales Order.
5. Ngày 3, khách check-out → PMS fire `reservation.checked_out` → ERPNext: Submit Sales Order → Tạo Sales Invoice (room 3 nights + F&B 2,500).

### Ví dụ B: Multi-hotel Guest Consolidation

1. Khách B (PassportNo=CD789012) đã từng ở Hotel Bangkok (CompanyId=2, ProfileId=200). ERPNext đã có Contact với PMS Profile Map row {CompanyId=2, ProfileId=200}.
2. Khách B book phòng tại Hotel Phuket (CompanyId=3) → PMS Phuket tạo ProfileId=350.
3. PMS Phuket fire `profile.created` (CompanyId=3, ProfileId=350, PassportNo=CD789012, ChannelCode=WEB).
4. ERPNext: Tìm Contact theo PMS Profile Map (CompanyId=3, ProfileId=350) → Không tìm thấy. Tìm theo PassportNo=CD789012 → **Tìm thấy Contact cũ** → Thêm PMS Profile Map row mới {CompanyId=3, ProfileId=350}. Không tạo Contact mới. Cập nhật fields trống nếu có.
5. Kết quả: 1 Contact, 1 Customer, 2 rows trong PMS Profile Map → có thể xem toàn bộ lịch sử qua 2 hotel.

### Ví dụ C: Conflict — Phone number khác nhau

1. Contact trên ERPNext có MobileNo = "0891234567" (nguồn: Website booking trước đó).
2. PMS Hotel mới gửi profile cùng PassportNo nhưng MobileNo = "0899999999".
3. Theo source-of-truth rule: ERPNext giữ "0891234567" (đã có từ trước), **không ghi đè**.
4. Hệ thống ghi log conflict: "MobileNo mismatch — ERPNext: 0891234567, PMS: 0899999999".
5. Staff CRM review log → xác nhận số nào đúng → cập nhật thủ công nếu cần.

---

> **Lưu ý cuối**: Tài liệu này là khung kiến thức nền. Các chi tiết cụ thể (PMS vendor nào, version nào, ERPNext version, custom modifications) cần được xác nhận với project stakeholders trước khi áp dụng vào phân tích cụ thể.
