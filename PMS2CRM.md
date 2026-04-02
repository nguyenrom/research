# PMS (Soraso) → ERPNext (Frappe) Synchronization Analysis

> Source: SORASO API Dictionary_FRAPPE (1).xlsx
> Date: 2026-04-02

---

## 1. Architecture Overview

```
PMS Event Occurs (real-time)
    ↓
Webhook (Notify) → Frappe Webhook Endpoint
    ↓ (immediate <5s response)
Verify X-Soraso-Signature (HMAC-SHA256 with Webhook Secret) → Return 200 OK
    ↓ (async background job)
Fetch full JSON via GET to resource_uri (with X-API-KEY + X-HOTEL-UNIQUE-KEY)
    ↓
Map & Create/Update Frappe Records
```

### Events to Handle

| Category | Events |
|----------|--------|
| Reservation | `reservation.created` / `reservation.updated` / `reservation.checked_in` / `reservation.stay_updated` / `reservation.checked_out` / `reservation.cancelled` / `reservation.noshow` / `reservation.recovery` |
| Profile | `profile.created` / `profile.updated` (including merged profiles → delete + update pair) |
| POS | `order.created` / `order.completed` (incidental charges) |

### Multi-Company Structure

Each hotel branch = 1 Company in ERPNext. CompanyId maps to Company doctype.

---

## 2. Operational Flow Summary

> **Đọc section này trước để hiểu toàn bộ lifecycle trước khi đi vào chi tiết mapping.**

### Reservation Lifecycle (PMS Status → Frappe State)

```
PMS RecordStatus                          Frappe Action                                  Document State
────────────────────────────────────────  ─────────────────────────────────────────────  ──────────────────────────────────
0 - PROSPECT                              Create Sales Order                             Draft (Sales Order)
1 - TENTATIVE                             Create/Update Sales Order                      Draft (Sales Order)
2 - CONFIRMED                             Create/Update Sales Order                      Draft (Sales Order)
5 - WAITING LIST                          Create/Update Sales Order                      Draft (Sales Order)
6 - HOLDING LIST                          Create/Update Sales Order                      Draft (Sales Order)
7 - IN-HOUSE (Check-in)                   Update Sales Order (Room#, Guests)             Draft (Sales Order)
7 - IN-HOUSE (Stay)                       Append Items (F&B, Spa, Minibar) to Table      Draft (Sales Order)
8 - CHECKED-OUT                           Submit Sales Order → Create Sales Invoice      Submitted → Sales Invoice
3 - CANCELLATION                          Cancel Sales Order                             Cancelled
4 - NO-SHOW                               Cancel Sales Order with no-show flag           Cancelled
```

**RecordStatus Enum:**
- 0 = Prospect
- 1 = Tentative
- 2 = Confirmed
- 3 = Cancellation
- 4 = No-show
- 5 = Waiting List
- 6 = Holding List
- 7 = In-House
- 8 = Checked-out

---

### Guest Identity — Primary/Secondary Key

```
Key         Field           Dùng để                          Ghi chú
──────────  ──────────────  ───────────────────────────────  ──────────────────────────────────
Primary     PassportNo      Match khách giữa PMS ↔ ERPNext   Unique toàn cầu, có khi check-in
Secondary   IdCard (PMS)    Fallback khi không có passport   CMND/CCCD cho khách nội địa
```

**Tại sao Passport là PK:**
- Unique toàn cầu, không trùng giữa các khách
- Bắt buộc thu tại check-in (theo luật TM.05 Thailand, immigration VN)
- 1 khách ở nhiều hotel → cùng 1 PassportNo → gộp được thành 1 Customer trên ERPNext

**IdCard (PMS) = CMND/CCCD là SK:**
- Cho khách nội địa không có passport
- PMS field tên `IdCard`, map vào Frappe Contact field `id_card`

---

### Multi-Hotel Guest Consolidation

**Vấn đề:** 1 khách ở 3 hotel = 3 PMS ProfileId khác nhau (mỗi hotel 1 PMS instance). ERPNext phải gộp thành 1 Customer duy nhất.

```
PMS Hotel A (CompanyId=1)           PMS Hotel B (CompanyId=2)           PMS Hotel C (CompanyId=3)
ProfileId = 100                     ProfileId = 200                     ProfileId = 300
PassportNo = "AB123456"             PassportNo = "AB123456"             PassportNo = "AB123456"
FirstName = "John"                  FirstName = "John"                  FirstName = "John"
                    ╲                           │                           ╱
                     ╲                          │                          ╱
                      ╲                         │                         ╱
                       ▼                        ▼                        ▼
                    ┌──────────────────────────────────────────────────┐
                    │  ERPNext: 1 Contact + 1 Customer                │
                    │                                                  │
                    │  Contact: "John", PassportNo = "AB123456"       │
                    │  ├─ PMS Profile Map (child table):              │
                    │  │   Hotel A (Company 1) → PMS ProfileId 100    │
                    │  │   Hotel B (Company 2) → PMS ProfileId 200    │
                    │  │   Hotel C (Company 3) → PMS ProfileId 300    │
                    │  │                                               │
                    │  Customer: link → Contact                        │
                    │  ├─ Sales Order SO-001 (Hotel A, DLX, 3 nights) │
                    │  ├─ Sales Order SO-045 (Hotel B, SUP, 2 nights) │
                    │  └─ Sales Order SO-112 (Hotel C, STD, 1 night)  │
                    └──────────────────────────────────────────────────┘
```

#### PMS Profile Map — Child Table trên Contact

Mỗi khi nhận profile từ 1 hotel, ghi vào child table để map ngược:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| hotel_branch | Link → Company | Hotel nào | "Hotel A Saigon" |
| pms_profile_id | Int | ProfileId bên PMS | 100 |
| pms_profile_code | Data | ProfileCode bên PMS | "VH0000001" |
| pms_company_id | Int | CompanyId bên PMS | 1 |
| last_synced | Datetime | Lần sync cuối | "2026-04-01 14:30:00" |

**Lookup logic khi nhận webhook:**
```
Nhận profile từ PMS (CompanyId=2, ProfileId=200, PassportNo="AB123456"):
  1. Tìm Contact WHERE PMS Profile Map.pms_company_id=2 AND pms_profile_id=200
     → FOUND → Update Contact (đã biết khách này ở hotel này)
  2. KHÔNG tìm thấy → Tìm Contact WHERE PassportNo="AB123456"
     → FOUND → Thêm row vào PMS Profile Map (khách cũ, hotel mới)
  3. KHÔNG tìm thấy → Tìm Contact WHERE id_card="079123456789"
     → FOUND → Thêm row vào PMS Profile Map
  4. KHÔNG tìm thấy → Tạo Contact mới + row PMS Profile Map đầu tiên
```

#### Customer — History across hotels

Customer link tới Contact. Tất cả Sales Orders từ mọi hotel đều thuộc cùng 1 Customer:

```
Customer: CUST-00123 (John Doe)
├─ Contact: John Doe (PassportNo: AB123456)
│   └─ PMS Profile Map:
│       ├─ Hotel A → ProfileId 100
│       ├─ Hotel B → ProfileId 200
│       └─ Hotel C → ProfileId 300
│
├─ Sales Orders (view history tất cả hotels):
│   ├─ SO-001  Hotel A  2026-01-10 → 2026-01-13  DLX  3 nights  Checked-out
│   ├─ SO-045  Hotel B  2026-02-20 → 2026-02-22  SUP  2 nights  Checked-out
│   └─ SO-112  Hotel C  2026-04-01 → 2026-04-02  STD  1 night   In-House
│
├─ Sales Invoices:
│   ├─ INV-001  Hotel A  15,000 THB  Paid
│   └─ INV-045  Hotel B   8,500 THB  Paid
│
└─ Links to Hotels (từ PMS Profile Map):
    ├─ Hotel A: xem profile trên PMS Hotel A
    ├─ Hotel B: xem profile trên PMS Hotel B
    └─ Hotel C: xem profile trên PMS Hotel C
```

---

### 3 Tình huống đồng bộ Guest Data

```
Tình huống              Kênh define       Thời điểm sync Contact    Matching key
──────────────────────  ────────────────  ────────────────────────  ──────────────────
A. OTA Booking          ChannelCode=OTA   Check-in (Status 7)      PassportNo (lúc CI)
B. Website / Walk-in    ChannelCode=WEB   Booking (Status 0-2)     PassportNo / NatID
                        ChannelCode=WLK
C. Member-first         —                 Đã có trên ERPNext       PassportNo / NatID
```

**ChannelCode** xác định kênh → quyết định thời điểm sync:

```
ChannelCode   Kênh                    Sync Contact khi nào
────────────  ──────────────────────  ─────────────────────────────────────
BCOM          Booking.com             Check-in (Status 7) — KHÔNG sync lúc booking
AGODA         Agoda                   Check-in (Status 7) — KHÔNG sync lúc booking
EXPEDIA       Expedia                 Check-in (Status 7) — KHÔNG sync lúc booking
OTA_*         Các OTA khác            Check-in (Status 7) — KHÔNG sync lúc booking
WEB           Website khách sạn       Booking (Status 0-2) — sync ngay
WALKIN        Walk-in                 Booking (Status 0-2) — sync ngay
DIRECT        Đặt trực tiếp          Booking (Status 0-2) — sync ngay
PHONE         Đặt qua điện thoại     Booking (Status 0-2) — sync ngay
```

---

#### Tình huống A: OTA Booking (Booking.com, Agoda, Expedia...)

Khách book qua OTA → PMS chỉ nhận tên + email OTA → **KHÔNG sync Contact/Customer lúc booking** → Chỉ tạo Sales Order trước. Khi check-in mới có passport → sync Contact.

```
OTA → PMS                          PMS → ERPNext
─────────────────────────          ──────────────────────────────────────────────────────

1. OTA gửi booking                 reservation.created (Status 0-2)
   - Tên khách (có thể alias)      → KIỂM TRA ChannelCode
   - Email OTA (proxy)                ChannelCode ∈ {BCOM, AGODA, EXPEDIA, OTA_*}
   - Không có passport, DOB           → KHÔNG tạo Contact/Customer
   - Không có phone thật           → Create Sales Order (Draft) — KHÔNG có Customer link
                                       - Item = Room Category
                                       - ChannelCode = "BCOM"/"AGODA"/...
                                       - OtaBookingId = OTA ref number
                                       - ota_guest_name (Frappe) = tên từ OTA (lưu tạm)
                                       - ota_guest_email (Frappe) = email OTA proxy (lưu tạm)
                                       - Flag: pending_guest_sync (Frappe) = true

2. Khách đến check-in              reservation.checked_in (Status 7)
   - Hotel thu passport, scan      → BÂY GIỜ mới sync Contact:
   - Điền DOB, phone, address         Có PassportNo → TÌM Contact (matching logic):
   - Ký registration card               1. PassportNo (PK)
                                         2. IdCard (SK)
                                       → FOUND → Update Contact + thêm PMS Profile Map row
                                       → NOT FOUND → Tạo Contact mới + PMS Profile Map
                                    → Tạo/Link Customer
                                    → Update Sales Order:
                                       - Gắn Customer link (lúc này mới có)
                                       - Assign RoomNo
                                       - Update Guests (Frappe: Occupant Detail)
                                       - Xóa flag pending_guest_sync (Frappe)

3. Trong thời gian lưu trú         reservation.stay_updated (Status 7)
   - Minibar, Spa, F&B             → Append Items to Sales Order
   - POS charges                   → order.created / order.completed

4. Check-out                        reservation.checked_out (Status 8)
                                    → Submit Sales Order → Sales Invoice
```

**Rủi ro cần xử lý:**
- OTA gửi tên alias ("Mr. Booking") → lưu vào ota_guest_name (Frappe) trên Sales Order, KHÔNG tạo Contact
- Email OTA proxy (hash@guest.booking.com) → lưu vào ota_guest_email (Frappe), không gửi marketing
- Sales Order KHÔNG có Customer link cho đến khi check-in → report/filter cần handle NULL customer
- Khách no-show OTA → Sales Order cancel mà chưa bao giờ có Contact → clean

---

#### Tình huống B: Website / Walk-in Booking

Khách book trên website khách sạn hoặc walk-in → Có đầy đủ thông tin từ đầu → Sync Contact ngay.

```
Website/Walk-in → PMS              PMS → ERPNext
─────────────────────────          ──────────────────────────────────────────────────────

1. Khách đặt phòng                 profile.created
   - Điền đầy đủ thông tin         → KIỂM TRA ChannelCode
   - Tên thật, email thật             ChannelCode ∈ {WEB, WALKIN, DIRECT, PHONE}
   - Phone, có thể có passport        → Sync Contact NGAY
                                    → TÌM Contact (matching logic):
                                       1. PassportNo (PK) — nếu có
                                       2. IdCard (SK) — nếu có
                                       3. Email (exact match, non-OTA)
                                    → FOUND → Update Contact + thêm PMS Profile Map row
                                    → NOT FOUND → Tạo Contact mới + PMS Profile Map
                                    → Tạo/Link Customer

                                    reservation.created (Status 0-2)
                                    → Create Sales Order (Draft)
                                       - Customer = real Customer (đã có)
                                       - ChannelCode = "WEB"/"WALKIN"
                                       - pending_guest_sync (Frappe) = false

2. Check-in                         reservation.checked_in (Status 7)
                                    → Update Contact (bổ sung nếu thiếu):
                                       - PassportNo (scan tại quầy) → RE-MATCH nếu lúc booking chưa có
                                    → Update Sales Order:
                                       - Assign RoomNo
                                       - Update Guests (Frappe: Occupant Detail)

3-4. Stay + Check-out              (Giống tình huống A từ bước 3)
```

**Khác biệt với OTA:**
- Contact tạo ngay lúc booking, không chờ check-in
- Sales Order có Customer link từ đầu
- Email thật → có thể gửi confirmation, marketing
- Nếu booking chưa có passport → RE-MATCH lại khi check-in (scan passport)

---

#### Tình huống C: Member-first (Đăng ký thành viên trước)

Khách đăng ký thành viên trên ERPNext → Contact + Customer đã tồn tại → Sau đó mới booking tại khách sạn → Match bằng PassportNo/IdCard.

```
ERPNext (có sẵn)                    PMS → ERPNext (khi booking)
─────────────────────────          ──────────────────────────────────────────────────────

0. Khách đăng ký member            Contact + Customer đã tồn tại trên ERPNext:
   trên ERPNext (web/app)             - Contact: đầy đủ info + PassportNo/IdCard
   - Điền profile đầy đủ              - Customer: Is Member (Frappe) = true
   - Nhận custom_member_card_no (CRM)  - PMS Profile Map: TRỐNG (chưa có PMS ProfileId)
   - Chưa ở hotel nào

1. Khách booking tại hotel          profile.created / profile.updated
   (qua kênh WEB/WALKIN/DIRECT)    → TÌM Contact (matching logic):
   - PMS tạo ProfileId mới            1. PassportNo (PK) ← match ở đây
                                       2. IdCard (SK)
                                    → FOUND → Update Contact:
                                       - Thêm row PMS Profile Map (hotel này, ProfileId mới)
                                       - KHÔNG ghi đè data ERPNext
                                       - Chỉ bổ sung fields trống

                                    reservation.created (Status 0-2)
                                    → Create Sales Order (Draft)
                                       - Customer = matched Customer (đã là member)

   (qua kênh OTA)                  → KHÔNG sync Contact lúc booking (như tình huống A)
                                    → Khi check-in: PassportNo match → gắn vào Contact cũ
                                       + thêm PMS Profile Map row

2-4. Check-in → Stay → Check-out   (Giống tình huống A/B tùy kênh)
```

---

### Matching Rules — Thứ tự ưu tiên

```
Priority  Field(s)                    Type   Action khi match
────────  ──────────────────────────  ─────  ─────────────────────────────────────────
1         PassportNo                  PK     Auto-link + thêm PMS Profile Map row
2         IdCard (CMND/CCCD)          SK     Auto-link + thêm PMS Profile Map row
3         Email (exact, non-OTA)      Soft   Auto-link nhưng log để review
4         MobileNo + LastName         Fuzzy  Flag để staff confirm thủ công
—         Không match được            —      Tạo Contact mới + PMS Profile Map row đầu tiên
```

**Quy tắc ghi đè khi match:**

```
Field               ERPNext có sẵn    PMS gửi về       Action
──────────────────  ────────────────  ────────────────  ──────────────────────────
Email               "real@gmail"      "hash@ota"        GIỮ ERPNext (source-of-truth)
Email               "real@gmail"      "real@gmail"      Không thay đổi
Email               —                 "real@gmail"      LẤY từ PMS (bổ sung)
PassportNo          —                 "AB123456"        LẤY từ PMS (bổ sung)
PassportNo          "AB123456"        "AB123456"        Không thay đổi
IdCard              —                 "079123456789"    LẤY từ PMS (bổ sung)
NationalityCode     —                 "TH"              LẤY từ PMS (bổ sung)
MobileNo            "0891234567"      "0891234567"      Không thay đổi
MobileNo            "0891234567"      "0899999999"      GIỮ ERPNext, log conflict
PMS Profile Map     —                 CompanyId+ProfId  THÊM row (không ghi đè row cũ)
```

**Rule tổng quát: ERPNext là source-of-truth. PMS chỉ BỔ SUNG fields trống, KHÔNG ghi đè. PMS Profile Map chỉ THÊM row, không xóa.**

---

### Sync Logic tổng hợp — Decision Tree

```
Khi nhận webhook từ PMS (CompanyId, ProfileId, ChannelCode):
│
├─ Event: profile.created / profile.updated
│   │
│   ├─ Xác định kênh: ChannelCode ∈ OTA group?
│   │   │
│   │   ├─ OTA (BCOM, AGODA, EXPEDIA...) → SKIP, không sync Contact
│   │   │   (chờ check-in mới sync)
│   │   │
│   │   └─ Non-OTA (WEB, WALKIN, DIRECT, PHONE) → Sync Contact:
│   │       │
│   │       ├─ Tìm Contact bằng PMS Profile Map (CompanyId + ProfileId)
│   │       │   └─ FOUND → đã biết khách này → Update Contact (bổ sung)
│   │       │
│   │       ├─ KHÔNG tìm thấy → Tìm bằng PassportNo (PK)
│   │       │   └─ FOUND → khách cũ, hotel mới → thêm PMS Profile Map row
│   │       │
│   │       ├─ KHÔNG tìm thấy → Tìm bằng IdCard (SK)
│   │       │   └─ FOUND → khách cũ, hotel mới → thêm PMS Profile Map row
│   │       │
│   │       └─ KHÔNG tìm thấy → Tạo Contact mới + Customer + PMS Profile Map
│   │
│   └─ Tạo/Update Customer (link Contact) — chỉ nếu non-OTA
│
├─ Event: reservation.created / reservation.updated
│   │
│   ├─ Tìm Sales Order theo ConfirmationNo / RecordId
│   │   ├─ FOUND → Update Sales Order
│   │   └─ NOT FOUND → Create Sales Order (Draft)
│   │
│   ├─ ChannelCode ∈ OTA → Sales Order KHÔNG có Customer link
│   │   (pending_guest_sync (Frappe) = true, lưu ota_guest_name/email (Frappe) tạm)
│   │
│   └─ ChannelCode ∈ Non-OTA → Link Customer (đã tạo/match ở bước profile)
│
├─ Event: reservation.checked_in (Status 7)
│   │
│   ├─ CÓ passport/NatID → Sync Contact (matching logic ở trên)
│   │   ├─ Nếu OTA: đây là lần đầu sync Contact cho booking này
│   │   └─ Nếu non-OTA: RE-MATCH nếu lúc booking chưa có passport
│   │
│   ├─ Update Sales Order:
│   │   ├─ Gắn Customer link (nếu OTA, lần đầu có Customer)
│   │   ├─ Assign RoomNo
│   │   ├─ Update Guests (Frappe: Occupant Detail)
│   │   └─ Xóa pending_guest_sync (Frappe) flag
│   │
│   └─ Update Sales Order (Room, Occupants, Customer link)
│
├─ Event: reservation.stay_updated / order.created
│   └─ Append Items to Sales Order
│
├─ Event: reservation.checked_out (Status 8)
│   ├─ Submit Sales Order
│   └─ Create Sales Invoice
│
├─ Event: reservation.cancelled / reservation.noshow
│   └─ Cancel Sales Order (+ no-show flag nếu noshow)
│
└─ Event: reservation.recovery
    └─ Re-activate cancelled Sales Order → Draft
```

---

### Phase-by-Phase Summary (tất cả tình huống)

#### Phase 1: At Booking (Status 0=PROSPECT → 6=HOLDING LIST)
1. **Kiểm tra ChannelCode** → xác định kênh booking
2. **Non-OTA**: Match/tạo Contact + Customer ngay (bằng PassportNo/IdCard)
3. **OTA**: KHÔNG sync Contact — lưu ota_guest_name/email (Frappe) tạm trên Sales Order
4. Create Sales Order (Draft) — OTA: không có Customer link, Non-OTA: có Customer link
5. Items: Room Category (e.g., RM-DELUXE) with estimated nights
6. Metadata: Map Groups.GroupCode, OtaBookingId, ExternalConfirmNo, ChannelCode
7. Deposit: Link to Customer → flag as `Is Payer` (Frappe) (chỉ non-OTA)

#### Phase 2: At Check-in & In-House (Status 7=IN-HOUSE)
1. **Sync Contact** — dùng PassportNo (PK) hoặc IdCard (SK) để match
2. **OTA**: Lần đầu tạo/match Contact + gắn Customer link vào Sales Order
3. **Non-OTA**: RE-MATCH nếu lúc booking chưa có passport
4. **Multi-hotel**: Thêm PMS Profile Map row nếu khách đã có Contact từ hotel khác
5. Room Assignment: Update Hotel Room link + RoomNo
6. Occupant Sync: Update Guests (Frappe: Occupant Detail) child table
7. Incidental Charges: Append new items (Minibar, Spa, etc.)

#### Phase 3: At Check-out (Status 8=CHECKED-OUT)
1. Step A — Final Review: Last check of Draft Sales Order
2. Step B — Submit: Change Sales Order to Submitted (locks record)
3. Step C — Invoice: Generate Sales Invoice

#### Cancellation (Status 3=CANCELLATION, 4=NO-SHOW)
- Status 3 — CANCELLATION: Cancel Sales Order
- Status 4 — NO-SHOW: Cancel Sales Order with no-show flag
- OTA no-show: Sales Order cancel mà chưa có Contact → clean (không tạo Contact rác)

#### Recovery
- Re-activate cancelled Sales Order → quay lại Draft

#### POS Flow
- In-house guest (Status 7=IN-HOUSE): Append incidental items to existing Sales Order
- Walk-in (no reservation): Create direct Sales Invoice lines linked to guest Contact

---

## 3. Frappe Doctype Registry

> **Tạo tất cả custom doctypes và custom fields TRƯỚC khi code sync logic.**

### 3.1 Custom Doctypes (to create)

| # | Doctype | Type | Notes | Cần cho |
|---|---------|------|-------|---------|
| 1 | PMS Profile Map | Custom (Child Table) | Map 1 Contact ↔ nhiều PMS ProfileId (per hotel). Fields: hotel_branch, pms_profile_id, pms_profile_code, pms_company_id, last_synced | Guest matching + Multi-hotel |
| 2 | Hotel Room | Custom | Room master data, linked to Company and Item | RoomMaster sync |
| 3 | Register Membership | Custom | Guest consent tracking | GuestProfile sync |
| 4 | Booking group | Custom | Group reservation management | Reservation sync |
| 5 | Party group | Custom | Party reservation management | Reservation sync |
| 6 | PurposeOfStays | Custom | Purpose of stay tracking | Reservation sync |
| 7 | Contract | Custom | Rate contract (Note: unclear source - possibly Customer with contract flag) | Reservation sync |

### 3.2 Standard Doctypes Requiring Custom Fields

| # | Doctype | Custom Fields Needed | Cần cho |
|---|---------|---------------------|---------|
| 1 | Item | Hotel Branch (Link→Company), Room type fields | RoomMaster + Reservation |
| 2 | Contact | PassportNo (PK), IdCard (SK), PMS Profile Map (Table), VIPTypeCode, GuestTypeCode, NationalityCode, BlacklistStatus, LanguageCode, LicensePlate, etc. | GuestProfile + Reservation + Multi-hotel |
| 3 | Address | Standard fields sufficient; may need TaxId custom field | GuestProfile |
| 4 | Customer | Is Payer (Frappe), Is Member (Frappe), Is Contact Point (Frappe), VIP Status, Voucher (Table), Preferences | GuestProfile + Reservation |
| 5 | Sales Order | ConfirmationNo, RecordId, RecordStatus, ChannelCode, pending_guest_sync (Frappe), ota_guest_name (Frappe), ota_guest_email (Frappe), Options flags, Booking group (Link), Party group (Link), ArrivalDate/Time, DepartureDate/Time, PurposeOfStays (Link), Guests child table, rate/channel/segment fields | Reservation + OTA sync |
| 6 | Sales Order Item | RoomNo, Hotel Room (Link), NoOfAdult/Child/Infant/Guest, NoOfExtraBed/ExtraPerson | Reservation |
| 7 | Sales Invoice | Mirror relevant Sales Order custom fields | Reservation (Check-out) |
| 8 | Sales Invoice Item | Mirror relevant Sales Order Item custom fields | Reservation (Check-out) |

---

## 4. RoomMaster → Frappe Mapping

> **Sync master data phòng trước. Đây là prerequisite cho Reservation sync.**

### 4.1 Main Object → Hotel Room + Item

| PMS Field | Type | Description | Frappe Doctype | Frappe Field | Field Type | Option |
|-----------|------|-------------|----------------|--------------|------------|--------|
| CompanyId | number | Hotel property/chain ID | Item | Hotel Branch | Link | Company |
| RoomNo | string | Room number/name ("101","102") | Hotel Room | Room Number | Data | — |
| — | — | — | Hotel Room | Hotel Branch | Link | Company |
| StatRoom | string | Room status code (VC, VD, AC, AD, OC, OD, OO, OI, OS) | — | — | — | — |
| StatRoomName | string | Room status name ("Vacant Clean", "Vacant Dirty", etc.) | — | — | — | — |
| RoomTypeCode | string | Room type code (e.g., DLX-K) | Item | (+) room_type_code | Data | — |
| RoomTypeName | string | Room type name (e.g., "Deluxe King") | Item | (+) room_type_name | Data | — |
| — | — | — | Hotel Room | Category | Link | Item |
| RoomName | string | Display name for the room | Hotel Room | (+) room_name | Data | — |
| RackRate | number | Standard non-discounted price | Hotel Room | (+) rack_rate | Currency | — |
| FastCheckin | boolean | Eligible for fast check-in | Hotel Room | (+) fast_checkin | Check | — |
| BuildingId | number | Building system ID | Hotel Room | (+) building_id | Int | — |
| BuildingName | string | Building name ("Building A", "B", "C") | Hotel Room | (+) building_name | Data | — |
| WingId | number | Wing system ID | Hotel Room | (+) wing_id | Int | — |
| WingName | string | Wing name ("Left Wing", "Right Wing") | Hotel Room | (+) wing_name | Data | — |
| FloorId | number | Floor system ID | Hotel Room | (+) floor_id | Int | — |
| FloorName | string | Floor name ("Floor 1", "Floor 2") | Hotel Room | (+) floor_name | Data | — |
| ViewId | number | View system ID | Hotel Room | (+) view_id | Int | — |
| ViewName | string | View name ("City View", "Sea View") | Hotel Room | (+) view_name | Data | — |
| BedTypeId | number | Bed type system ID | Hotel Room | (+) bed_type_id | Int | — |
| BedTypeName | string | Bed type ("Twin", "Triple") | Hotel Room | (+) bed_type_name | Data | — |
| SpecialId | number | Special feature ID | Hotel Room | (+) special_id | Int | — |
| SpecialName | string | Special feature ("Non Smoke", "Smoking Room") | Hotel Room | (+) special_name | Data | — |
| ConnectionNo | string | Connecting room number (empty = non-connecting) | Hotel Room | (+) connection_no | Data | — |
| Seq | number | Display order sequence | Hotel Room | (+) seq | Int | — |
| RecordId | number | Related Reservation RecordId | Hotel Room | (+) record_id | Int | — |
| RoomSize | number | Room size (sqm) | Hotel Room | (+) room_size | Float | — |
| Active | boolean | Room active in system | Hotel Room | (+) active | Check | — |
| FloorSide | string | Floor side ("East") | Hotel Room | (+) floor_side | Data | — |
| — | — | — | Hotel Room | (+) no_of_extra_bed | Int | — |
| — | — | — | Hotel Room | (+) max_adults | Int | — |
| — | — | — | Hotel Room | (+) max_children | Int | — |
| — | — | — | Hotel Room | (+) no_of_infant | Int | — |

**Fields NOT mapped (audit/visual/operational only):** CreateBy, CreateDt, LastupdateBy, LastupdateDt, BsnRmId (NOT USE), Showcolumn, Usedlastdate, Ltop, Lleft, Lwidth, Lhigh, Lsize, Ncurvature, Nlabelctr (NOT USE), Keycardno, ElecttricNo, IccardNo, ZoneCode, UtilityId, MaidAssignCode, RmDiscrepancy, RmDpcStaffcode, RmDpcDatetime, KeycardPublicdoor, EnableDigitalLock, DoorMacAddress, RoomMasterLang, RoomExtension

---

## 5. GuestProfile → Frappe Mapping

> **Sync guest master data trước Reservation. Guest/Customer phải tồn tại trước khi tạo Sales Order.**

### 5.1 Profile (Main Object) → Contact + Customer

#### Contact Doctype

| PMS Field | Type | Description | Example | Frappe Field |
|-----------|------|-------------|---------|--------------|
| ProfileId | number | Guest unique ID | 1 | (+) profile_id |
| ProfileCode | string | Guest profile code | VH0000001 | (+) profile_code |
| ProfileName | string | Full name | John Snow | full_name (default) |
| FirstName | string | First name | John | first_name (default) |
| LastName | string | Last name | Snow | last_name (default) |
| TitleId | number | Title ID | Enum: 1=Mr. 2=Miss 3=Mrs. 4=Ms 11=Other | salutation (default) |
| TitleName | string | Title display | MR. | — (dùng TitleId map) |
| GenderId | number | Gender code | Enum: 1=Male 2=Female 3=Other | gender (default) |
| GenderName | string | Gender display | "Male" | — (dùng GenderId map) |
| VIPTypeCode | string | VIP status code | Enum: 1=MEMBER, 2=VIP, 3=Other | (+) vip_type_code |
| VIPTypeName | string | VIP display | — | — (dùng VIPTypeCode map) |
| DateOfBirth | string | Birthday (ISO 8601) | "2025-11-12T..." | (+) date_of_birth |
| IdCard | string | CMND/CCCD (SK cho matching) | "079123456789" | (+) id_card |
| PassportNo | string | Passport number (PK cho matching) | "AB123456" | (+) passport_no |
| JoinDate | string | Profile creation date | "2025-11-12T..." | (+) join_date |
| ExpireDate | string | Profile/membership expiry | "2025-11-12T..." | (+) expire_date |
| MobileNo | string | Primary mobile | — | mobile_no (default) |
| NationalityCode | string | Nationality code | "TH" | (+) nationality_code |
| NationalityName | string | Nationality name | "Thai" | — (dùng NationalityCode map) |
| CountryId | number | Country ID | — | — (dùng CountryName map) |
| CountryName | string | Country name | "Thailand" | (+) country |
| Email | string | Primary email | — | email_id (default) |
| GuestTypeCode | string | Guest category | Enum: REG, BUS, FIT, GOV, GRP | (+) guest_type_code |
| GuestTypeName | string | Guest type display | — | — (dùng GuestTypeCode map) |
| ChannelCode | string | Booking channel code | OTA | (+) channel_code |
| ChannelName | string | Booking channel name | Online Travel Agent | — (dùng ChannelCode map) |
| SegmentCode | string | Market segment code | OTA | (+) segment_code |
| SegmentName | string | Market segment name | Online Travel Agent | — (dùng SegmentCode map) |
| Notice | string | General notice | — | (+) notice |
| PolicyRemark | string | Special policies | — | (+) policy_remark |
| Active | boolean | Profile active | true | (+) is_active |
| KeepHistory | boolean | Retain visit history | true | (+) keep_history |
| SocialMediaType | string | Social media type ("LINE", "Facebook") | — | Source |
| SocialMediaTypeName | string | Social media display | — | Channel |
| SocialMediaId | string | Social media user ID | — | Channel |
| LicensePlate | string | Vehicle license plate | — | (+) license_plate |
| LanguageCode | string | Preferred language ("en-US", "th-TH") | — | language (default) |
| BlacklistStatus | boolean | On blacklist | true/false | (+) blacklist_status |
| MiddleName | string | Middle name | — | middle_name (default) |
| ~~MemberCardNo~~ | — | ~~CRM tự quản lý (custom_member_card_no trên Customer) — không sync từ PMS~~ | — | — |
| ~~MemberTier~~ | — | ~~CRM tự quản lý — không sync từ PMS~~ | — | — |
| StartEffectiveDate | string | Membership start | "2025-11-12T..." | (+) start_effective_date |
| EndEffectiveDate | string | Membership expiry | "2025-11-12T..." | (+) end_effective_date |
| RefNo | string | General reference number | — | (+) ref_no |
| BackupEmail | string | Secondary email | — | (+) backup_email |
| BillingAddressType | number | Address for billing (1=Residential, 2=Working) | — | Address (Link) |
| ResidentialAddress | object | Home address | See Address table | Address (Link) |
| WorkingAddress | object | Work address | See Address table | Address (Link) |
| BillingAddress | object | Billing address | See Address table | Address (Link) |
| GuestPicture | array | Guest pictures | See GuestPicture table | — |
| ~~LastVisitInfo~~ | — | ~~ERPNext tự derive từ Sales Orders~~ | — | — |
| MemberList | array | Associated memberships | See MemberList table | — |
| AttachmentList | array | File attachments (passport scan) | See AttachmentList table | — |
| ConsentList | array | Guest consents (marketing) | See ConsentList table | — |
| ProfileNotes | object | Preferences and caveats | See ProfileNotes table | Notes/comment |

**NOT USED fields:** VisitType, VisitTypeName, HiddenProfile

#### Customer Doctype (created alongside Contact)

| Frappe Field | Field Type | Option | Notes |
|--------------|------------|--------|-------|
| Contact | Link | Contact | Link to Contact doctype |
| Billing address | Link | Address | — |
| Is Payer | Boolean | — | Flag for payment responsibility (Frappe) |
| Is Member | Boolean | — | Member flag (Frappe, CRM tự quản lý) |
| Is Contact Point | Boolean | — | Primary contact flag (Frappe) |
| Tax ID | Data | — | From BillingAddress.TaxId |
| Payment Terms | — | — | — |
| Currency | Link | Currency | From reservation CurrCode |
| (+) Member Level | Select | Silver, Gold, Platinum | CRM tự quản lý membership tier |
| (+) Point Balance | Number | — | Điểm loyalty hiện tại |
| (+) Loyalty ID | Data | — | Mã loyalty CRM tự sinh |
| (+) Total Points | Number | — | Tổng điểm tích lũy |
| Join Date | Date | — | Tracking tenure |
| Preferences | String | — | Food allergies, High floor, etc. |
| VIP Status | Select | VIP 1, VIP 2, VVIP | From VIPTypeCode |
| Voucher | Table | Voucher | Voucher child table |

### 5.2 Address (Reusable Object) → Address Doctype

Used for ResidentialAddress, WorkingAddress, and BillingAddress.

| PMS Field | Type | Description | Frappe Doctype |
|-----------|------|-------------|----------------|
| CompanyName | string | Company name (for WorkingAddress) | Address |
| Address1 | string | Street address line 1 | Address |
| Address2 | string | Street address line 2 | Address |
| CityName | string | City name | Address |
| CountryId | number | Country system ID | Address |
| CountryName | string | Country name | Address |
| ZipCode | string | Postal/ZIP code | Address |
| TelephoneNo | string | Phone number | Address |
| FaxNo | string | Fax number | Address |
| TelExtension | string | Phone extension | Address |
| Website | string | Company website | Address |
| TaxId | string | Business/tax ID number | Address |

### 5.3 GuestPicture (Child Array)

| PMS Field | Type | Description |
|-----------|------|-------------|
| Id | number | Picture unique ID |
| SeqNo | number | Display order |
| PictureUrl | string | URL where picture is stored |

### 5.4 MemberListItem (Child Array) → Contact

| PMS Field | Type | Description |
|-----------|------|-------------|
| CompanyCode | string | Company code for membership |
| CustomerCode | string | Customer code for membership |
| MemberCode | string | Membership code |

### 5.5 AttachmentList (Child Array) → Contact

| PMS Field | Type | Description |
|-----------|------|-------------|
| SeqNo | number | Display order |
| AttachmentUrl | string | URL where attachment is stored |
| DocumentType | string | Document type ("Passport", "ID Card") |

### 5.6 ConsentList (Child Array) → Register Membership (Custom Doctype)

| PMS Field | Type | Description |
|-----------|------|-------------|
| SeqNo | number | Display order |
| ConsentDate | string | Consent timestamp |
| AcceptFlag | boolean | Guest gave consent (true/false) |
| ConsentTypeName | string | Consent name ("Email Marketing", "PDPA") |

### 5.7 ProfileNotes (Object) → Contact Notes/comment

| PMS Field | Type | Description |
|-----------|------|-------------|
| Preferences | string | Guest preferences ("Likes high floor") |
| Caveats | string | Warnings/alerts ("Allergic to nuts") |

---

## 6. Reservations → Frappe Mapping

> **Phụ thuộc vào Section 4 (RoomMaster) và Section 5 (GuestProfile). Phải sync master data trước.**

### 6.1 Phase 1: Booking (Status 0-6) — Create Sales Order (Draft)

Actions:
1. Create Sales Order (Draft)
2. Customer = Contact with `Is Contact Point` (Frappe) flag
3. Items = Room Category (e.g., RM-DELUXE) with estimated nights
4. Metadata: Map Groups.GroupCode and OtaBookingId/ExternalConfirmNo
5. Deposit → Link to Customer → flag as `Is Payer` (Frappe)

### 6.2 Phase 2: Check-in & In-House (Status 7) — Update Sales Order (Still Draft)

Actions:
1. Room Assignment: Update Hotel Room link and physical RoomNo
2. Occupant Sync: Update Guests (Frappe: Occupant Detail) child table with all guest Contacts
3. Contact: Update information for guest profile
4. Incidental Charges: Append new rows to items table (Minibar, Spa, etc.)

### 6.3 Phase 3: Check-out (Status 8) — Submit → Invoice

Actions:
1. **Step A - Final Review:** Last check of Draft Sales Order
2. **Step B - Submit:** Change Sales Order to Submitted (locks record)
3. **Step C - Invoice:** Generate Sales Invoice

### 6.4 Reservation Main Object → Sales Order

| PMS Field | Type | Description | Frappe Doctype | Frappe Field |
|-----------|------|-------------|----------------|--------------|
| RecordType | string | Record type ("RESERVATION", "IN-HOUSE") | Sales Order | (+) record_type |
| SeqNo | number | Sequence number | Sales Order | (+) seq_no |
| ConfirmationNo | string | Confirmation number (RR2500001) | Sales Order | (+) confirmation_no |
| RecordId | number | Internal reservation ID | Sales Order | (+) record_id |
| RecordStatus | number | Status code (0-8) | Sales Order | (+) record_status |
| BookingTypeId | number | Booking type ID | Sales Order | (+) booking_type_id |
| ShowAddress | number | Address display flag (1=Agent, 2=Guest) | Sales Order | (+) show_address |
| NoOfRoom | number | Number of rooms | Sales Order | Sale Order Item → Qty=1 |
| NoOfAdult | number | Total adults | Sales Order | Sale Order Item → (+) no_of_adult |
| NoOfChild | number | Total children | Sales Order | Sale Order Item → (+) no_of_child |
| NoOfInfant | number | Total infants | Sales Order | Sale Order Item → (+) no_of_infant |
| NoOfExtraBed | number | Extra beds added | Sales Order | Sale Order Item → (+) no_of_extra_bed |
| NoOfExtraPerson | number | Extra persons | Sales Order | Sale Order Item → (+) no_of_extra_person |
| NoOfAdditionalGuest | number | Additional guests | Sales Order | Sale Order Item → (+) no_of_additional_guest |
| ExtraBedQty | number | Extra bed quantity | Sales Order | Sale Order Item → (+) extra_bed_qty |
| NoOfGuest | number | Total guests (Adult+Child+Infant) | Sales Order | Sale Order Item → (+) no_of_guest |
| RoomTypeCode | string | Room type code | Sales Order | Sale Order Item → item_code (default) |
| RoomTypeName | string | Room type name | Sales Order | Sale Order Item → item_name (default) |
| RoomNo | string | Assigned room number | Sales Order | Sale Order Item → (+) room_no |
| ArrivalDate | string | Guest arrival date/time | Sales Order | (+) arrival_date |
| ArrivalTime | string | Estimated arrival time | Sales Order | (+) arrival_time |
| DepartureDate | string | Guest departure date/time | Sales Order | (+) departure_date |
| DepartureTime | string | Estimated departure time | Sales Order | (+) departure_time |
| OldDeparture | string | Previous departure date (if changed) | Sales Order | (+) old_departure |
| ArrivingBy | string | Transport mode ("Flight", "Car") | Sales Order | (+) arriving_by |
| ArrivingNo | string | Flight/license plate for arrival | Sales Order | (+) arriving_no |
| DepartingBy | string | Transport mode for departure | Sales Order | (+) departing_by |
| DepartingNo | string | Flight number for departure | Sales Order | (+) departing_no |
| ContractId | number | Rate contract internal ID | Sales Order | (+) contract_id |
| RateCode | string | Rate plan code ("BAR", "CORP") | Sales Order | (+) rate_code |
| AvgRate | number | Average nightly rate | Sales Order | (+) avg_rate |
| BreakfastCode | string | Breakfast package code | Sales Order | (+) breakfast_code |
| AvgBreakfast | number | Average nightly breakfast price | Sales Order | (+) avg_breakfast |
| SegmentCode | string | Market segment code | Sales Order | (+) segment_code |
| SourceCode | string | Booking source code | Sales Order | (+) source_code |
| ChannelCode | string | Booking channel code | Sales Order | (+) channel_code |
| GuestTypeCode | string | Guest type code | Sales Order | (+) guest_type_code |
| CurrCode | string | Currency code ("USD", "THB") | Sales Order | currency (default) |
| Remark | string | General remarks | Sales Order | (+) remark |
| TrnComment | string | Transaction comment | Sales Order | (+) trn_comment |
| PolicyRemark | string | Special policy remark | Sales Order | (+) policy_remark |
| IsMainGroup | boolean | Main reservation for group | Sales Order | (+) is_main_group |
| Groups | object | Group details | Sales Order | Booking group (Link) |
| Parties | object | Party details | Sales Order | Party group (Link) |
| Options | object | Boolean flags | Sales Order | Custom fields (see Options) |
| Guests | array | Guest list | Sales Order | Contact Child Table |
| DailyRates | array | Daily rate charges | Sales Order | — |
| ~~Deposits~~ | array | ~~Deposit list~~ | — | — | *Folio data — không sync, checkout mới settle* |
| ~~DepositRefunds~~ | array | ~~Deposit refund list~~ | — | — | *Folio data — không sync* |
| ~~SpecialBillings~~ | array | ~~Billing instructions/routing~~ | — | — | *Folio routing rules — PMS operational* |
| ~~SpecialRequests~~ | array | ~~Special requests~~ | — | — | *Operational — đã có ProfileNotes (5.7)* |
| ~~AddOns~~ | array | ~~Add-on packages/services~~ | — | — | *Folio charges — không sync* |
| ~~Guarantees~~ | array | ~~Guarantee methods~~ | — | — | *Folio data — không sync* |
| PurposeOfStays | array | Stay purposes | Sales Order | PurposeOfStays (Link) |
| BookingNo | string | Original booking number | Sales Order | (+) booking_no |
| CheckInNo | string | Registration number at check-in | Sales Order | (+) check_in_no |
| SaleCode | string | Salesperson code | Sales Order | (+) sale_code |
| ContactPerson | string | Booking contact name | Sales Order | contact_person (Link → Contact) |
| ContactTelephone | string | Contact phone | Sales Order | (+) contact_telephone |
| ContactEmail | string | Contact email | Sales Order | (+) contact_email |
| Nights | number | Total nights | Sales Order | Sale Order Item → qty (default) |
| ContractName | string | Rate contract name | Sales Order | (+) contract_name |
| ~~PaymentMethodId~~ | number | ~~Payment method ID~~ | — | — | *Folio data — không sync* |
| ~~PaymentMethodName~~ | string | ~~Payment method name~~ | — | — | *Folio data — không sync* |
| ~~ArCode~~ | string | ~~AR account code~~ | — | — | *Folio data — không sync* |
| ~~ArName~~ | string | ~~AR account name~~ | — | — | *Folio data — không sync* |
| ~~ArRemark~~ | string | ~~AR account remark~~ | — | — | *Folio data — không sync* |
| ~~ReferenceNo~~ | string | ~~General reference number~~ | — | — | *Folio data — không sync* |
| ~~ExternalConfirmNo~~ | string | ~~External confirmation number~~ | — | — | *Folio data — không sync* |
| ~~VoucherNo~~ | string | ~~Voucher number~~ | — | — | *Folio data — không sync* |
| UseRateFrom | number | Rate origin (0=Guest, 1=Contract, 2=Agent, 3=Source) | Customer | (+) use_rate_from |
| CompanyAgentId | number | Travel agent company ID | Customer | (+) company_agent_id |
| CompanyAgentCode | string | Travel agent code | Customer | (+) company_agent_code |
| CompanyAgentName | string | Travel agent name | Customer | (+) company_agent_name |
| CompanyAgentEmail | string | Travel agent email | Customer | (+) company_agent_email |
| CompanyAgentTel | string | Travel agent phone | Customer | (+) company_agent_tel |
| CompanySourceCode | string | Booking source code | Customer | (+) company_source_code |
| CompanySourceName | string | Booking source name | Customer | (+) company_source_name |
| CompanySourceEmail | string | Booking source email | Customer | (+) company_source_email |
| CompanySourceTel | string | Booking source phone | Customer | (+) company_source_tel |
| PaymentPolicy | string | Payment policy text | Sales Order | (+) payment_policy |
| CancellationPolicy | string | Cancellation policy text | Sales Order | (+) cancellation_policy |
| OtaBookingId | string | OTA booking ID | Sales Order | (+) ota_booking_id |
| OriginalRoomType | string | Original room type (if upgraded) | Sales Order | (+) original_room_type |
| IsShared | boolean | Sharer reservation (multi-guest) | — | — |
| IsMainShare | boolean | Primary guest of share | — | — |
| ShareRef | string | Reference code linking sharers | — | — |
| FolioBalance | number | Outstanding folio balance | — | — |

**NOT USED fields:** Extrabed, ExtraPerson, AppRateId, PkType, PkCode, PkCharge, RateCategories, IsRtc, FlagStatus, TripRefNo, ExternalRateType, AppRateDetailId, BlockNo, ShareType, IsTempShare, UsedById, UsedByName, UtilityPlan, MaxPax, RoomRate, AllowMonthlyAutopost, DepositInfo, Document, Emergency, HotelTransfer, EnableDigitalLock, PaymentInfo

### 6.5 Options (Object) → Sales Order Custom Fields

| PMS Field | Type | Description | Frappe Field |
|-----------|------|-------------|--------------|
| SuperBlock | boolean | Super block reservation | (+) super_block |
| PayAtHotel | boolean | Pay at Hotel booking | (+) pay_at_hotel |
| UseContractAddress | boolean | Use contract address | (+) use_contract_address |
| NonRefundable | boolean | Non-refundable booking | (+) non_refundable |
| NonCancellation | boolean | Non-cancellable booking | (+) non_cancellation |

**NOT USED:** GenerateVat, ViewProfile, AllowPOSOnline, AllowUseInternet, DoNotMove, CreditLimit

### 6.6 Guests (Child Array) → Contact

| PMS Field | Type | Description |
|-----------|------|-------------|
| ProfileSeq | number | Guest sequence (1=Main, 2=Accompanying) |
| ProfileId | number | Guest profile ID |
| TitleId | number | Title ID |
| GenderId | number | Gender ID |
| FirstName | string | First name |
| LastName | string | Last name |
| KeepHistory | boolean | Add to profile history |
| IdPassportTypeId | number | ID type (1=Passport, 2=ID Card) |
| PassportNo | string | ID/Passport number |
| DateOfBirth | string | Date of birth |
| ExpireDate | string | ID/Passport expiry |
| Email | string | Email |
| Telephone | string | Phone |
| SocialMediaType/Name/Id | string | Social media details |
| LicensePlate | string | Vehicle license plate |
| IsAdult | boolean | Is adult guest |
| NationalityCode | string | Nationality code |
| CountryId | number | Country ID |
| GuestTypeCode | string | Guest type code |
| VipTypeCode | string | VIP status code |
| BillingAddressType | number | Billing address type |
| ~~Registration~~ | — | ~~Immigration/legal compliance — không sync CRM~~ |
| GuestPicture | array | Guest pictures |
| ResidentialAddress | object | Home address |
| WorkingAddress | object | Work address |
| BillingAddress | object | Billing address |
| ExternalProfileCode | string | External system profile ID |
| MemberShipId | string | Membership ID (from PMS) |
| MemberConfirmNo | string | Membership confirmation number |
| AccessId | number | Access system ID |
| BankAccountNo | string | Bank account number |
| BankCode | string | Bank code |
| NoOfVisits | number | Total visits |
| ProfileNotes | object | Preferences and caveats |
| CheckinStatus | boolean | Guest checked in |
| IsBirthdayToday | boolean | Birthday today |
| BackupEmail | string | Secondary email |

### 6.7 DailyRates (Child Array)

| PMS Field | Type | Description |
|-----------|------|-------------|
| Id | number | Daily rate entry ID |
| SeqNo | number | Sequence number |
| PostDate | string | Charge date |
| SegmentCode | string | Market segment for this day |
| RateCode | string | Rate code for this day |
| PostType | number | Posting type code |
| FolioCode | string | Folio window code |
| FolioName | string | Folio name |
| TransCode | string | Transaction code ("ROOM_CHARGE") |
| TransName | string | Transaction display name |
| Qty | number | Quantity |
| UnitId | number | Unit system ID |
| Amount | number | Base amount before discounts |
| Price | number | Price per unit |
| DiscountPercent | number | Discount percentage |
| DiscountAmount | number | Discount amount |
| NetAmount | number | After discounts, before tax/service |
| ServiceAmount | number | Service charge |
| VatAmount | number | VAT amount |
| TaxAmount | number | Total tax amount |
| GrandTotal | number | Final total (Net + Service + Tax) |
| Remark | string | Charge remark |
| SystemDate | string | Posting timestamp |
| IsPosted | boolean | Posted to folio |
| IsManualEdit | boolean | Manually edited |
| IsFixItem | boolean | Fixed-price item |
| IsRoomChargeItem | boolean | Main room charge |
| IsBreakfastItem | boolean | Breakfast charge |
| IsExtraItem | boolean | Extra item (extra bed) |
| IsPackageItem | boolean | Part of package |
| IsPackageBenefitItem | boolean | Package benefit (zero value) |
| PackageType | number | Package type ID |
| ExternalItemId | number | External item system ID |
| IsPackageBenefit | boolean | Package benefit flag |
| ItemTypeCode | string | Item type code |
| BuCode | string | Business unit code |
| BreakfastTypeId | number | Breakfast type ID |
| DayPost | number | Day of stay (1, 2, 3...) |
| BaseRate | number | Base rate before adjustments |
| MealsCode | string | Meal plan code |
| SubTransCode | string | Sub-transaction code |
| IsAbfitem | boolean | ABF (American Breakfast) item flag |

### 6.8 Groups (Object) → Booking Group (Custom Doctype)

| PMS Field | Type | Description |
|-----------|------|-------------|
| GroupCode | string | Unique group code |
| GroupName | string | Group display name |
| LeaderName | string | Group leader name |
| Remark | string | Group remark |
| PostToRoom | string | Charge posting instructions |
| DepositToMasterRoom | boolean | Deposits to group master room |
| IsCustomProfile | boolean | Group uses custom profile |

### 6.9 Parties (Object) → Party Group (Custom Doctype)

| PMS Field | Type | Description |
|-----------|------|-------------|
| PartyCode | string | Unique party code |
| PartyName | string | Party display name |
| Remark | string | Party remark |
| PostToRoom | string | Charge posting instructions |

### 6.10 PurposeOfStays (Child Array) → PurposeOfStays (Custom Doctype)

| PMS Field | Type | Description |
|-----------|------|-------------|
| Id | number | Entry ID |
| RecordId | number | Reservation RecordId |
| PurposeCode | string | Purpose code ("BUSINESS") |
| PurposeName | string | Purpose display name |

---

## 7. POSOrder → Frappe Mapping

> **Phụ thuộc vào Reservation (Section 6). POS charge cho in-house guest append vào Sales Order hiện tại.**

POS Orders → Append incidental Sales Order Items (if guest is in-house) or direct Sales Invoice lines (if walk-in).

### 7.1 Order (Main Object)

| PMS Field | Type | Description | Example |
|-----------|------|-------------|---------|
| OutletNo | string | Outlet identifier code | "REST-01" |
| OutletName | string | Outlet display name | "The Coffee Shop" |
| OrderDate | string | Order date/time (ISO 8601) | "2025-11-26T14:30:00Z" |
| CheckId | number | Internal check/bill ID | 10550 |
| CheckNo | string | Display check number | "CHK-251126-001" |
| CheckStatus | string | Bill status | OPEN, PAID, VOID, CANCEL |
| TableNo | string | Table number | T01, T02 |
| ProfileId | number | Guest profile ID (nullable) | 102345 |
| GuestName | string | Guest name | "John Doe" |
| GuestEmail | string | Guest email (for e-receipts) | "john.d@example.com" |
| Items | array | Ordered items list | See Items table |
| Payments | array | Payments applied | See Payments table |

### 7.2 Items (Child Array)

| PMS Field | Type | Description | Example |
|-----------|------|-------------|---------|
| Id | number | Line item ID | 5001 |
| CreateAt | string | Item added timestamp | "2025-11-26T14:35:00Z" |
| StatusOrder | string | Item kitchen status | COOKING, SERVED, CANCEL |
| ItemCode | string | Menu item SKU | "BEV-005" |
| SizeCode | string | Size code | "SZ-L" |
| SizeName | string | Size display | "Large" |
| ItemName | string | Menu item name | "Iced Latte" |
| Qty | number | Quantity ordered | 2 |
| UnitPrice | number | Price per unit | 120.00 |
| Amount | number | Subtotal (Qty * UnitPrice) | 240.00 |
| ServiceAmount | number | Service charge | 24.00 |
| VatAmount | number | VAT amount | 18.48 |
| CityTaxAmount | number | Local city tax | 0.00 |
| GrandTotal | number | Final total (Amount + Taxes + Service) | 282.48 |
| CondimentText | string | Special instructions | "Less Sweet, Oat Milk" |
| VatRate | number | VAT percentage | 7.0 |

### 7.3 OrderPayment (Child Array)

| PMS Field | Type | Description | Example |
|-----------|------|-------------|---------|
| PaymentCode | string | Payment method code | "CC" |
| PaymentName | string | Payment method name | "Credit Card" |
| PaymentReference | string | Receipt number | "ABB-251100001" |
| TotalPayment | number | Amount paid | 282.48 |

---

## 8. Reference: Sale Order Item — Hotel Room Example

```
Item: Deluxe                    → Room category (e.g., RM-DELUXE)
Hotel Room: BT_101              → Room 101, Ben Thanh branch
```

**Auto-fetched from Hotel Room:**
RoomName, RackRate, FastCheckin, Keycardno, BuildingId/Name, WingId/Name, FloorId/Name, ViewId/Name, BedTypeId/Name, SpecialId/Name, ConnectionNo, Seq, ElecttricNo, IccardNo, RecordId, Ltop, Lleft, Lwidth, Lhigh, Lsize, Ncurvature

**Manual (from booking data):**
NoOfAdult, NoOfChild, NoOfInfant, Extrabed, ExtraPerson, NoOfExtraBed, NoOfExtraPerson, NoOfAdditionalGuest, ExtraBedQty, NoOfGuest
