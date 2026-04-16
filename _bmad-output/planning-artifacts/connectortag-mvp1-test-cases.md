# ConnectorTag MVP 1 - Test Cases Manual (QC)

> **Dự án:** ConnectorTag - Stage 1.0 MVP  
> **Phiên bản tài liệu gốc:** Spec v1 - Version 3 (5 Jan 2026)  
> **Người tạo:** Winston (Architect Agent)  
> **Ngày tạo:** 14-Apr-2026  
> **Mục tiêu:** Bao phủ toàn bộ nghiệp vụ MVP, tương tác liên module, và edge cases

---

## Quy ước

- **Pre-condition:** Điều kiện tiên quyết trước khi thực hiện test
- **Steps:** Các bước thực hiện
- **Expected:** Kết quả mong đợi
- **Priority:** P0 (Critical), P1 (High), P2 (Medium), P3 (Low)
- **Type:** Positive / Negative / Edge Case / Integration

---

## Module 1: Landing Page (Đăng ký / Đăng nhập)

### 1.1 Hiển thị Landing Page

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-001 | Hiển thị Landing Page đúng layout | Positive | P0 |

**Steps:**
1. Truy cập www.connectortag.com

**Expected:**
- Hiển thị logo ConnectorTag (full name) trên Landing Page
- Hiển thị dropdown/button "Choose your City"
- Hiển thị field "Enter your first name" (empty free-text)
- Hiển thị 2 nút Google: Sign-up (nút 1) và Sign-in (nút 2)
- Hiển thị links "Terms of Service" và "Privacy Policy"
- Không hiển thị sidebar navigation

---

### 1.2 Chọn City

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-002 | Mở modal chọn city | Positive | P0 |

**Steps:**
1. Click vào "Choose your City"

**Expected:**
- Modal pop-up mở ra với danh sách 10 cities
- Có nút X ở góc trên bên phải để đóng modal
- Danh sách: Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, Singapore, London, New York City NY, Los Angeles CA
- Mỗi city có cờ quốc gia tương ứng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-003 | Chọn một city thành công | Positive | P0 |

**Steps:**
1. Click "Choose your City" → modal mở
2. Click vào "Sydney"

**Expected:**
- Modal đóng lại
- Trên Landing Page hiển thị "🇦🇺 Sydney" thay cho placeholder "Choose your City"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-004 | Đổi city sau khi đã chọn | Positive | P1 |

**Steps:**
1. Chọn city "Sydney"
2. Click lại vào box city
3. Chọn "Singapore"

**Expected:**
- Modal mở lại với danh sách 10 cities
- Sau khi chọn Singapore, hiển thị "🇸🇬 Singapore"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-005 | Đóng modal city mà không chọn | Negative | P2 |

**Steps:**
1. Click "Choose your City" → modal mở
2. Click nút X góc trên phải

**Expected:**
- Modal đóng lại
- Placeholder "Choose your City" vẫn hiển thị (chưa chọn city nào)

---

### 1.3 HELP - Waiting List

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-006 | HELP "1..." - Thêm vào Waiting List | Positive | P1 |

**Steps:**
1. Mở modal chọn city
2. Click HELP "1..."
3. Nhập email và city, country
4. Click "Send"

**Expected:**
- Modal HELP mở ra trên modal city
- Hiển thị các placeholder trong field nhập liệu (biến mất khi user bắt đầu gõ)
- Sau khi click Send: email + city,country được lưu vào Waiting List
- Modal đóng lại

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-007 | HELP "2..." - Hiển thị thông tin trợ giúp | Positive | P2 |

**Steps:**
1. Mở modal chọn city
2. Click HELP "2..."

**Expected:**
- Modal HELP thứ 2 mở ra với nội dung trợ giúp phù hợp
- Có nút X để đóng

---

### 1.4 Nhập First Name

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-008 | Nhập first name hợp lệ (2-25 ký tự) | Positive | P0 |

**Steps:**
1. Click vào field "Enter your first name"
2. Nhập "Rom" (3 ký tự)

**Expected:**
- Field hiển thị "Rom"
- Trên mobile/tablet: bàn phím mở lên
- Không có error message

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-009 | Nhập first name quá ngắn (1 ký tự) | Negative | P0 |

**Steps:**
1. Nhập "R" vào field first name
2. Thử tiến hành đăng ký

**Expected:**
- Error message màu đỏ: "*Name must contain between 2-25 characters including spaces."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-010 | Nhập first name quá dài (>25 ký tự) | Negative | P1 |

**Steps:**
1. Nhập "ABCDEFGHIJKLMNOPQRSTUVWXYZ" (26 ký tự) vào field first name

**Expected:**
- Error message: "*Name must contain between 2-25 characters including spaces."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-011 | Nhập first name đúng 2 ký tự (boundary) | Edge Case | P1 |

**Steps:**
1. Nhập "Ab" vào field first name

**Expected:**
- Chấp nhận, không có error

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-012 | Nhập first name đúng 25 ký tự (boundary) | Edge Case | P1 |

**Steps:**
1. Nhập chuỗi 25 ký tự bao gồm spaces

**Expected:**
- Chấp nhận, không có error

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-013 | Nhập tên nằm trong danh sách banned names | Negative | P0 |

**Steps:**
1. Nhập "admin" vào field first name
2. Thử đăng ký

**Expected:**
- Hệ thống không cho phép đăng ký với tên banned
- Danh sách banned names bao gồm: admin, administrator, user admin, ConnectorTag, official account, và tất cả censored tags

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-014 | Nhập tên banned dạng viết hoa khác nhau | Edge Case | P1 |

**Steps:**
1. Thử nhập "Admin", "ADMIN", "AdMiN"

**Expected:**
- Tất cả đều bị từ chối (case-insensitive check cho banned names)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-015 | Nhập first name có spaces | Positive | P2 |

**Steps:**
1. Nhập "Mary Jane" (10 ký tự bao gồm space)

**Expected:**
- Chấp nhận, tên hiển thị "Mary Jane"

---

### 1.5 Đăng ký (Sign-up) với Google

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-016 | Đăng ký thành công - New User | Positive | P0 |

**Pre-condition:** Google account chưa tồn tại trong hệ thống

**Steps:**
1. Chọn city (vd: Sydney)
2. Nhập first name hợp lệ (vd: "TestUser")
3. Click "Sign-in with Google" (nút 1 - Sign-up)
4. Hoàn tất Google OAuth

**Expected:**
- Tài khoản mới được tạo với Google User ID
- Landing Page đóng lại
- Mở trang "My Tags (free version)"
- Hệ thống gửi Welcome Email đến email Google của user

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-017 | Đăng ký khi chưa chọn city | Negative | P0 |

**Steps:**
1. Nhập first name "TestUser"
2. Click "Sign-in with Google" (nút 1) mà KHÔNG chọn city

**Expected:**
- Error message hiển thị, không cho phép tiếp tục
- Yêu cầu chọn city trước

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-018 | Đăng ký khi chưa nhập first name | Negative | P0 |

**Steps:**
1. Chọn city Sydney
2. Click "Sign-in with Google" (nút 1) mà KHÔNG nhập first name

**Expected:**
- Error message yêu cầu nhập first name

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-019 | Đăng ký với Google account đã tồn tại | Negative | P0 |

**Pre-condition:** Google account đã có trong hệ thống

**Steps:**
1. Chọn city, nhập first name
2. Click "Sign-in with Google" (nút 1 - Sign-up)
3. Chọn Google account đã đăng ký trước đó

**Expected:**
- Error message: "*An account already exists. Sign-in below for existing users."
- KHÔNG tạo tài khoản mới

---

### 1.6 Đăng nhập (Sign-in) - Existing User

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-020 | Đăng nhập thành công - Existing User | Positive | P0 |

**Pre-condition:** User đã có tài khoản

**Steps:**
1. Click "Sign-in with Google" (nút 2 - Sign-in)
2. Chọn Google account đã đăng ký

**Expected:**
- Hệ thống bỏ qua mọi thông tin đã nhập trong các field khác (city, name)
- Landing Page đóng lại
- Mở trang "My Matches"
- KHÔNG mở My Tags page

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-021 | Đăng nhập với Google account chưa đăng ký | Negative | P0 |

**Steps:**
1. Click "Sign-in with Google" (nút 2)
2. Chọn Google account CHƯA đăng ký

**Expected:**
- Error message: "*An existing account does not exist, sign-up above."

---

### 1.7 Links pháp lý

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-022 | Click Terms of Service | Positive | P2 |

**Steps:**
1. Click link "Terms of Service"

**Expected:**
- Mở modal pop-up với nội dung Terms of Service
- Có nút X góc trên phải để đóng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| LP-023 | Click Privacy Policy | Positive | P2 |

**Steps:**
1. Click link "Privacy Policy"

**Expected:**
- Mở modal pop-up với nội dung Privacy Policy
- Có nút X góc trên phải để đóng

---

## Module 2: Navigation Sidebar

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| NAV-001 | Hiển thị sidebar khi hover/click logo | Positive | P0 |

**Pre-condition:** User đã đăng nhập, đang ở bất kỳ trang nào (trừ Landing Page)

**Steps:**
1. Hover chuột (desktop) hoặc click (mobile) lên logo ở góc trên trái

**Expected:**
- 5 box đen hiển thị bên dưới logo (theo thứ tự):
  1. My Tags
  2. My Matches
  3. My Profile
  4. Popular Tags
  5. Upgrade to PRO
- Phần content còn lại semi-transparent và unclickable (nếu implemented)
- Logo hiển thị là phiên bản ngắn (không phải full name)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| NAV-002 | Sidebar không hiển thị trên Landing Page | Negative | P1 |

**Steps:**
1. Truy cập Landing Page (chưa đăng nhập)

**Expected:**
- Sidebar navigation KHÔNG hiển thị
- Logo full name hiển thị trên Landing Page

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| NAV-003 | Ẩn "Upgrade to PRO" cho PRO user | Positive | P1 |

**Pre-condition:** User đã upgrade lên PRO

**Steps:**
1. Click/hover logo để mở sidebar

**Expected:**
- Chỉ hiển thị 4 box: My Tags, My Matches, My Profile, Popular Tags
- KHÔNG hiển thị "Upgrade to PRO"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| NAV-004 | Navigate đến My Tags từ sidebar | Positive | P0 |

**Steps:**
1. Mở sidebar → click "My Tags"

**Expected:**
- Trang My Tags mở ra (Free hoặc PRO tùy trạng thái user)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| NAV-005 | Content dịch sang phải để không bị sidebar che | Positive | P1 |

**Steps:**
1. Quan sát layout trên mọi trang (trừ Landing Page)

**Expected:**
- Toàn bộ content text/form dịch sang phải, không bị sidebar che khuất

---

## Module 3: My Tags Page

### 3.1 My Tags - Free Version

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-001 | Hiển thị My Tags - New User (Free) | Positive | P0 |

**Pre-condition:** New user vừa đăng ký thành công

**Steps:**
1. Sau khi Sign-up, trang My Tags tự động mở

**Expected:**
- 5 tag fields trống
- Field đầu tiên có placeholder: "Enter your first tag here"
- Nút START hiển thị
- Minimum number of matching tags = 2 (default, không hiển thị cho user free)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-002 | Hiển thị My Tags - Existing User (Free) | Positive | P0 |

**Pre-condition:** User free đã có tags từ trước

**Steps:**
1. Click "My Tags" từ sidebar

**Expected:**
- 5 tag fields hiển thị tags đã nhập trước đó
- Thứ tự tags giữ nguyên như lần nhập trước

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-003 | Nhập tag hợp lệ | Positive | P0 |

**Steps:**
1. Click vào tag field đầu tiên
2. Nhập "football" (8 ký tự, lowercase, Latin)

**Expected:**
- Tag hiển thị "football"
- Không có error message
- Trên mobile/tablet: bàn phím mở lên

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-004 | Tag quá ngắn (<2 ký tự) | Negative | P0 |

**Steps:**
1. Nhập "a" (1 ký tự) vào tag field

**Expected:**
- Error: "*Tag must contain between 2-20 characters consisting of only letters, numbers and spaces."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-005 | Tag quá dài (>20 ký tự) | Negative | P1 |

**Steps:**
1. Nhập chuỗi 21+ ký tự vào tag field

**Expected:**
- Error: "*Tag must contain between 2-20 characters consisting of only letters, numbers and spaces."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-006 | Tag boundary - đúng 2 ký tự | Edge Case | P1 |

**Steps:**
1. Nhập "ab"

**Expected:**
- Chấp nhận, không error

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-007 | Tag boundary - đúng 20 ký tự | Edge Case | P1 |

**Steps:**
1. Nhập chuỗi đúng 20 ký tự Latin lowercase

**Expected:**
- Chấp nhận, không error

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-008 | Tag chứa symbols/underscore | Negative | P0 |

**Steps:**
1. Nhập "foot_ball" hoặc "foot@ball" hoặc "foot!ball"

**Expected:**
- Error: "*Tag must contain between 2-20 characters consisting of only letters, numbers and spaces."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-009 | Tag chứa số và spaces | Positive | P1 |

**Steps:**
1. Nhập "30s club"

**Expected:**
- Chấp nhận, hiển thị "30s club"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-010 | Auto-lowercase khi nhập uppercase | Positive | P0 |

**Steps:**
1. Nhập "Football" hoặc "FOOTBALL"

**Expected:**
- Hệ thống tự động chuyển thành "football" trên giao diện
- Lưu trong DB là "football" (cùng Tag ID với "football")

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-011 | Trim spaces đầu và cuối tag | Edge Case | P0 |

**Steps:**
1. Nhập "  football  " (có spaces trước và sau)

**Expected:**
- Hệ thống lưu và hiển thị là "football" (đã trim)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-012 | Nhiều spaces liên tiếp thành 1 space | Edge Case | P0 |

**Steps:**
1. Nhập "ballroom   dancing" (3 spaces liên tiếp)

**Expected:**
- Hệ thống lưu và hiển thị là "ballroom dancing" (1 space)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-013 | Nhập tag trùng nhau trong nhiều fields | Positive | P1 |

**Steps:**
1. Nhập "single" vào cả 5 tag fields
2. Click START

**Expected:**
- Hệ thống chấp nhận (user được phép nhập cùng 1 từ nhiều lần)
- Chuyển sang My Matches page

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-014 | Nhấn RETURN để chuyển tag field | Positive | P1 |

**Steps:**
1. Nhập tag hợp lệ vào field 1
2. Nhấn phím RETURN

**Expected:**
- Con trỏ di chuyển sang field 2
- Nếu field 2 đã có data, data đó được highlight
- Nếu gõ 1 ký tự bất kỳ, data cũ bị thay thế

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-015 | RETURN ở field cuối → select START → RETURN → click START | Positive | P1 |

**Steps:**
1. Nhập tag hợp lệ vào field 5 (field cuối)
2. Nhấn RETURN → START button được select
3. Nhấn RETURN lần nữa

**Expected:**
- START button được click
- Nếu tất cả 5 tags hợp lệ → chuyển sang My Matches

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-016 | Click START khi chưa điền đủ 5 tags (Free) | Negative | P0 |

**Steps:**
1. Chỉ nhập 3 tags (2 fields trống)
2. Click START

**Expected:**
- Error màu đỏ: "*All 5 tags must be completed."
- KHÔNG chuyển trang

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-017 | Click START thành công (Free) | Positive | P0 |

**Steps:**
1. Nhập đúng 5 tags hợp lệ
2. Click START

**Expected:**
- Trang My Tags đóng lại
- Mở trang My Matches
- Algo bắt đầu tìm matching tags với users cùng location
- Nếu có match → hiển thị Matched-Users trên My Matches

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-018 | Banned tag bị loại khỏi search nhưng user không biết | Positive | P0 |

**Steps:**
1. Nhập 5 tags, trong đó 1 tag nằm trong danh sách banned tags
2. Click START

**Expected:**
- Hệ thống chấp nhận (KHÔNG báo lỗi cho user)
- User KHÔNG được thông báo tag nào là banned
- Algo tìm kiếm match chỉ dùng 4 tags còn lại (loại trừ banned tag)

---

### 3.2 My Tags - PRO Version

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-019 | Hiển thị My Tags - PRO User | Positive | P0 |

**Pre-condition:** User đã upgrade PRO

**Steps:**
1. Click "My Tags" từ sidebar

**Expected:**
- 12 tag fields hiển thị
- Cho phép nhập 5-12 tags (minimum 5)
- Hiển thị option "Minimum number of matching tags" (1-12)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-020 | PRO - Nhập ít hơn 5 tags | Negative | P0 |

**Steps:**
1. Nhập 4 tags, để 8 fields trống
2. Click START

**Expected:**
- Error: "*At least 5 tags must be completed."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-021 | PRO - Nhập đúng 5 tags (minimum) | Positive | P0 |

**Steps:**
1. Nhập 5 tags, để 7 fields trống
2. Click START

**Expected:**
- Chấp nhận, chuyển sang My Matches
- 7 empty fields KHÔNG được sử dụng trong search (không match với empty fields của user khác)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-022 | PRO - Nhập đủ 12 tags | Positive | P1 |

**Steps:**
1. Nhập 12 tags hợp lệ
2. Click START

**Expected:**
- Chấp nhận, tất cả 12 tags được sử dụng trong search

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-023 | PRO - Set minimum matching tags = 1 | Positive | P0 |

**Steps:**
1. Nhập 5 tags
2. Set "Minimum number of matching tags" = 1
3. Click START

**Expected:**
- Algo chỉ cần 1 tag trùng khớp để tạo match

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| TAG-024 | PRO - Minimum matching tags không vượt quá số tags đã nhập | Edge Case | P1 |

**Steps:**
1. Nhập 5 tags
2. Thử set "Minimum number of matching tags" = 8

**Expected:**
- Hệ thống giới hạn max = min(12, số tags đã nhập) = 5
- Không cho phép set lớn hơn số tags hiện tại

---

## Module 4: Matching Algorithm (Nghiệp vụ cốt lõi)

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-001 | Match 2 free users - đủ 2 tags trùng | Positive | P0 |

**Pre-condition:**
- User A (free, Sydney): tags = "coffee", "running", "music", "travel", "reading"
- User B (free, Sydney): tags = "coffee", "running", "coding", "gaming", "writing"

**Expected:**
- A và B match (2 tags trùng: "coffee", "running" >= min 2)
- Cả hai xuất hiện trong My Matches của nhau

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-002 | Không match - chỉ 1 tag trùng (Free users) | Negative | P0 |

**Pre-condition:**
- User A (free, Sydney): tags = "coffee", "abc", "def", "ghi", "jkl"
- User B (free, Sydney): tags = "coffee", "xyz", "mno", "pqr", "stu"

**Expected:**
- A và B KHÔNG match (1 tag trùng < min 2 cho free)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-003 | Không match - khác location | Negative | P0 |

**Pre-condition:**
- User A (free, Sydney): tags = "coffee", "running", "music", "travel", "reading"
- User B (free, Melbourne): tags = "coffee", "running", "music", "travel", "reading"
- (Tất cả 5 tags giống nhau, nhưng khác city)

**Expected:**
- A và B KHÔNG match (khác location)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-004 | Match case-insensitive | Positive | P0 |

**Pre-condition:**
- User A nhập "Football" → lưu "football"
- User B nhập "FOOTBALL" → lưu "football"
- Cùng location, đủ tags trùng

**Expected:**
- Cả hai có cùng Tag ID cho "football"
- Algo match thành công

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-005 | PRO user set min=3, Free user min=2 | Integration | P0 |

**Pre-condition:**
- User A (free, Sydney, min=2): tags = "single", "dates", "coffee", "30s", "morning"
- User B (PRO, Sydney, min=3): tags = "single", "dates", "coffee", "friends", "events", "nightlife"

**Expected:**
- 3 tags trùng: "single", "dates", "coffee"
- A thỏa mãn (3 >= 2), B thỏa mãn (3 >= 3)
- A và B match thành công

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-006 | PRO user set min=3, Free user min=2 - chỉ 2 tags trùng | Negative | P0 |

**Pre-condition:**
- User A (free, Sydney, min=2): tags = "single", "dates", "coffee", "30s", "morning"
- User B (PRO, Sydney, min=3): tags = "single", "dates", "yoga", "friends", "events", "nightlife"

**Expected:**
- 2 tags trùng: "single", "dates"
- A thỏa mãn (2 >= 2), NHƯNG B KHÔNG thỏa mãn (2 < 3)
- A và B KHÔNG match (phải thỏa mãn rule của CẢ HAI user, lấy min cao hơn)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-007 | Duplicate tags - algo dùng tag nhiều lần | Edge Case | P0 |

**Pre-condition:**
- User C (PRO, Sydney, min=1): tags = "single", "dates", "coffee", "30s", "morning"
- User D (PRO, Sydney, min=2): tags = "single", "single", "single", "single", "single"

**Expected:**
- Algo match: D's "single" x2 khớp với C's "single" x1 (dùng tag "single" 2 lần)
- C thỏa mãn (2 >= 1), D thỏa mãn (2 >= 2)
- C và D match thành công

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-008 | Thay đổi tags không unmatch users đã match | Positive | P0 |

**Pre-condition:** User A và B đã match

**Steps:**
1. User A vào My Tags, thay đổi tất cả tags thành tags hoàn toàn khác
2. Click START

**Expected:**
- A và B vẫn matched
- A và B vẫn thấy nhau trong My Matches
- A và B vẫn nhắn tin được

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-009 | Banned tag không tham gia matching | Negative | P0 |

**Pre-condition:**
- Tag "xxx" nằm trong banned tags
- User A (free, Sydney): tags = "xxx", "coffee", "running", "music", "travel"
- User B (free, Sydney): tags = "xxx", "coffee", "running", "yoga", "gaming"

**Expected:**
- "xxx" bị loại khỏi search cho CẢ HAI user
- Chỉ còn: A = "coffee", "running", "music", "travel"; B = "coffee", "running", "yoga", "gaming"
- 2 tags trùng (coffee, running) >= min 2 → A và B match

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-010 | Priority search - PRO trước Free | Integration | P1 |

**Pre-condition:** Nhiều users trong cùng location

**Expected:**
- PRO users được tìm match trước (ưu tiên ít nhất 6 new matches / 24h)
- Free users tiếp theo (2 new matches / 24h)
- Cycle lặp lại: PRO → Free → PRO...

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ALGO-011 | Time limit search per user | Edge Case | P1 |

**Pre-condition:** User có tags rất unique, không ai trùng

**Expected:**
- Hệ thống dừng tìm kiếm cho user đó sau timeout (vd: 1 phút)
- Chuyển sang tìm cho user tiếp theo
- Hệ thống không bị treo/stuck

---

## Module 5: My Matches Page

### 5.1 Không có Matched-User

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-001 | No matches - Free user | Positive | P0 |

**Pre-condition:** Free user, chưa có match nào

**Steps:**
1. Click START trên My Tags → chuyển sang My Matches

**Expected:**
- Hiển thị wording phù hợp cho free version (khuyến khích chờ đợi)
- Không hiển thị danh sách Matched-Users

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-002 | No matches - PRO user | Positive | P0 |

**Pre-condition:** PRO user, chưa có match nào

**Expected:**
- Hiển thị wording phù hợp cho PRO version (khác với free)

---

### 5.2 Có Matched-Users

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-003 | Hiển thị danh sách Matched-Users | Positive | P0 |

**Pre-condition:** User có ít nhất 1 Matched-User

**Expected:**
- Mỗi match hiển thị trong 1 white box
- Profile picture (hoặc greyed-out headshot nếu chưa upload)
- Tên Matched-User
- Preview tin nhắn cuối (cắt bớt nếu quá dài)
- Last online status
- Link "Staying Safe Online" ở đầu trang

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-004 | First match - hiển thị welcome message | Positive | P0 |

**Pre-condition:** User vừa được match lần đầu với Matched-User

**Expected:**
- Hiển thị: "You have a match! Start a conversation now."
- Blue circle hiển thị (unread indicator)
- Cả hai users có thể nhắn tin ngay (KHÔNG cần accept match)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-005 | Last online status - Online | Positive | P1 |

**Pre-condition:** Matched-User đang mở webapp

**Expected:**
- Hiển thị "Online"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-006 | Last online status - Minutes ago | Positive | P1 |

**Pre-condition:** Matched-User offline 5 phút trước

**Expected:**
- Hiển thị "5m ago"
- Format: Xm ago cho < 60 phút

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-007 | Last online status - Hours ago | Positive | P1 |

**Pre-condition:** Matched-User offline 2 giờ trước

**Expected:**
- Hiển thị "2h ago"
- Format: Xh ago cho >= 60 phút và < 24 giờ

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-008 | Last online status - Yesterday | Positive | P1 |

**Pre-condition:** Matched-User offline 30 giờ trước

**Expected:**
- Hiển thị "Yesterday" (24-48 giờ)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-009 | Last online status - A few days ago | Positive | P1 |

**Pre-condition:** Matched-User offline >48 giờ

**Expected:**
- Hiển thị "A few days ago"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-010 | Sắp xếp matches theo last online | Positive | P1 |

**Pre-condition:** User có nhiều Matched-Users

**Expected:**
- Danh sách sort theo last online time (gần nhất ở trên)
- Online > Xm ago > Xh ago > Yesterday > A few days ago

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-011 | Blue circle cho unread messages | Positive | P0 |

**Pre-condition:** Matched-User gửi tin nhắn, User chưa đọc

**Expected:**
- Blue circle hiển thị bên cạnh tên Matched-User
- Không hiển thị số (MVP không cần số)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-012 | Không có blue circle khi đã đọc hết | Positive | P1 |

**Pre-condition:** User đã đọc tất cả tin nhắn

**Expected:**
- Không có blue circle
- Chỉ hiển thị preview tin nhắn cuối

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-013 | Click vào match → mở My Messages | Positive | P0 |

**Steps:**
1. Click vào bất kỳ đâu trong white box (profile pic, tên, preview)

**Expected:**
- Trang My Matches đóng
- Mở My Messages cho Matched-User tương ứng

---

### 5.3 Unmatch & Delete

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-014 | Unmatch and delete - single match | Positive | P0 |

**Steps:**
1. Check tickbox bên trái 1 Matched-User
2. Click "unmatch and delete"

**Expected:**
- Match bị xóa
- Tin nhắn bị xóa khỏi view của CẢ HAI users
- Cả hai không thể thấy hoặc nhắn tin nhau nữa
- Hiển thị message màu xanh: "Unmatched successfully! However, you may match again in future if your tags connect. We are working to bring you Block and Report functionalities."

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-015 | Unmatch and delete - multiple matches | Positive | P1 |

**Steps:**
1. Check tickbox bên trái 3 Matched-Users
2. Click "unmatch and delete"

**Expected:**
- Tất cả 3 matches bị xóa đồng thời
- Success message hiển thị

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-016 | Sau unmatch - user xóa hết matches → về no-match screen | Integration | P1 |

**Steps:**
1. Unmatch tất cả Matched-Users

**Expected:**
- Hiển thị "no Matched-User" screen (free hoặc PRO tùy version)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MAT-017 | Staying Safe Online modal | Positive | P2 |

**Steps:**
1. Click link "Staying Safe Online" ở đầu trang My Matches

**Expected:**
- Modal pop-up mở ra với nội dung an toàn online
- Có nút X để đóng

---

## Module 6: My Messages Page

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-001 | Hiển thị My Messages page | Positive | P0 |

**Pre-condition:** User click vào 1 Matched-User từ My Matches

**Expected:**
- Tên và profile picture Matched-User hiển thị ở trên cùng
- Toàn bộ tin nhắn trước đó hiển thị
- Scroll bar xuất hiện nếu nhiều tin nhắn, tự scroll xuống cuối
- Profile pic/name giữ cố định ở trên (không scroll theo)
- Field "Message...." ở dưới cùng
- Nút mũi tên phải (gửi) và mũi tên trái (quay lại)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-002 | Gửi tin nhắn thành công | Positive | P0 |

**Steps:**
1. Click vào field "Message...."
2. Nhập "Hello, nice to meet you!"
3. Click nút mũi tên phải (send)

**Expected:**
- Tin nhắn xuất hiện ở cuối thread
- Field "Message...." trở về trạng thái placeholder
- Matched-User nhận được tin nhắn

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-003 | Gửi khi field trống | Negative | P1 |

**Steps:**
1. Không nhập gì vào field
2. Click nút mũi tên phải

**Expected:**
- Không có gì xảy ra
- Không gửi tin nhắn trống

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-004 | Giới hạn ký tự tin nhắn (~120 ký tự) | Edge Case | P1 |

**Steps:**
1. Nhập tin nhắn vượt quá 120 ký tự

**Expected:**
- Hệ thống giới hạn hoặc cảnh báo khi vượt limit
- Không cho gửi tin nhắn quá dài

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-005 | Tin nhắn chứa ký tự, số, symbols | Positive | P1 |

**Steps:**
1. Nhập "Hi! Let's meet at 5pm :)"

**Expected:**
- Chấp nhận ký tự đặc biệt, số, symbols trong tin nhắn
- Tin nhắn hiển thị đúng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-006 | Quay lại My Matches - nút mũi tên trái | Positive | P0 |

**Steps:**
1. Nhập "draft message" nhưng KHÔNG gửi
2. Click nút mũi tên trái (hoặc swipe left trên mobile)

**Expected:**
- Tin nhắn chưa gửi bị bỏ qua (KHÔNG lưu draft)
- Quay lại trang My Matches

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-007 | Swipe left trên mobile để quay lại | Positive | P2 |

**Steps:**
1. Trên mobile/tablet, swipe từ phải sang trái

**Expected:**
- Quay lại My Matches (tương đương click mũi tên trái)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-008 | Profile pic/name tự động cập nhật | Integration | P1 |

**Pre-condition:** Matched-User thay đổi display name hoặc profile picture

**Steps:**
1. Mở My Messages với Matched-User đó

**Expected:**
- Tên và/hoặc profile picture hiển thị phiên bản MỚI NHẤT
- Tự động cập nhật, không cần refresh

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-009 | Bàn phím mở trên mobile khi click Message field | Positive | P1 |

**Steps:**
1. Trên mobile, click vào field "Message...."

**Expected:**
- Bàn phím mobile mở lên
- Layout điều chỉnh phù hợp

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| MSG-010 | Mỗi Matched-User có page riêng biệt | Positive | P0 |

**Pre-condition:** User có 3 Matched-Users: A, B, C

**Steps:**
1. Mở Messages với A → gửi "Hello A"
2. Quay lại, mở Messages với B → gửi "Hello B"
3. Quay lại, mở Messages với A lại

**Expected:**
- Messages với A chỉ chứa "Hello A"
- Messages với B chỉ chứa "Hello B"
- Không lẫn lộn giữa các conversations

---

## Module 7: Popular Tags Page

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| POP-001 | Hiển thị top 20 popular tags theo location | Positive | P0 |

**Pre-condition:** User ở Sydney, nhiều users đã tạo tags

**Steps:**
1. Click "Popular Tags" từ sidebar

**Expected:**
- Hiển thị top 20 tags phổ biến nhất tại Sydney
- Tự động populate (không cần admin thao tác)
- Sort theo usage count giảm dần

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| POP-002 | Minimum 20 counts để xuất hiện | Edge Case | P0 |

**Pre-condition:** Tag "tennis" chỉ có 15 users dùng tại Sydney

**Expected:**
- "tennis" KHÔNG xuất hiện trên Popular Tags page
- Chỉ tags có >= 20 counts mới hiển thị

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| POP-003 | Censored tags không hiển thị | Positive | P0 |

**Pre-condition:** Tag "censored_word" nằm trong censored tags, có >20 counts

**Expected:**
- "censored_word" KHÔNG hiển thị trên Popular Tags
- Tag tiếp theo (count cao nhất chưa hiển thị) thay thế

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| POP-004 | Users khác location thấy popular tags khác | Positive | P0 |

**Pre-condition:** User A ở Sydney, User B ở Singapore

**Steps:**
1. User A xem Popular Tags
2. User B xem Popular Tags

**Expected:**
- Danh sách tags khác nhau (dựa trên usage count tại mỗi location)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| POP-005 | Chỉ đếm tags đang active | Edge Case | P1 |

**Pre-condition:** User C trước đó dùng tag "football", giờ đã thay tag khác

**Expected:**
- Count của "football" giảm đi 1
- Chỉ đếm tags đang được sử dụng hiện tại

---

## Module 8: Upgrade to PRO Page

### 8.1 New User (Chưa dùng trial)

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-001 | Hiển thị trang Upgrade - chưa dùng trial | Positive | P0 |

**Pre-condition:** Free user, chưa bao giờ dùng free trial

**Steps:**
1. Click "Upgrade to PRO" từ sidebar

**Expected:**
- Hiển thị trang Upgrade to PRO với wording cho new user
- Free trial date tự động tính: today + 10 ngày
- Format ngày: DD-MMM-YYYY (tháng bằng chữ, vd: 24-APR-2026)
- Timezone theo location user đã chọn
- Giá: AUD 12.99/month (KHÔNG hardcode)
- Link "My Profile" mở tab mới
- Links ToS và Subscription Policy mở modal pop-up

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-002 | Chỉ users Australia thấy Upgrade option (MVP) | Positive | P0 |

**Pre-condition:** User ở Sydney (Australia)

**Expected:**
- Trang Upgrade hiển thị với đầy đủ options
- Stripe chỉ accept: billing address Australia + thẻ từ ngân hàng Australia

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-003 | Users ngoài Australia không upgrade được (MVP) | Negative | P0 |

**Pre-condition:** User ở Singapore/London/NYC/LA

**Expected:**
- Không hiển thị option upgrade HOẶC không thể hoàn tất payment
- Stripe reject thẻ/địa chỉ non-Australian

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-004 | Checkbox đồng ý trước khi payment | Positive | P0 |

**Steps:**
1. KHÔNG check tickbox
2. Click "Place Order"

**Expected:**
- Error: "Tick the box to agree then proceed with card details"
- Không tiến hành payment

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-005 | Payment thành công qua Stripe | Positive | P0 |

**Steps:**
1. Check tickbox đồng ý
2. Nhập thông tin thẻ hợp lệ (Australian bank)
3. Nhập địa chỉ Australia (post code, full address với dropdown)
4. Click "Place Order"

**Expected:**
- Payment processed qua Stripe
- User upgrade lên PRO
- Hệ thống gửi PRO Subscription Email với:
  - Free trial end date
  - First payment date
  - Subscription term dates

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-006 | Billing address field - autocomplete | Positive | P2 |

**Steps:**
1. Bắt đầu gõ "1 Sydney Road" vào field address

**Expected:**
- Dropdown hiển thị danh sách địa chỉ matching
- User có thể chọn từ dropdown

---

### 8.2 Existing User (Đã dùng trial)

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PRO-007 | Hiển thị trang Upgrade - đã dùng trial | Positive | P0 |

**Pre-condition:** Free user, đã sử dụng free trial trước đó

**Steps:**
1. Click "Upgrade to PRO" từ sidebar

**Expected:**
- Hiển thị wording khác (no free trial)
- Yêu cầu payment ngay từ đầu
- Links và tickbox hoạt động tương tự PRO-001

---

## Module 9: My Profile Page

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-001 | Hiển thị My Profile | Positive | P0 |

**Steps:**
1. Click "My Profile" từ sidebar

**Expected:**
- Profile picture (hoặc greyed-out circle nếu chưa upload)
- Nút (+) để upload/update ảnh
- First name hiển thị (tên thực, không phải chữ "First Name")
- Icon pencil bên cạnh tên
- Link "Change my location"
- Links: About & FAQs, ToS, Privacy Policy, Sub & Cancel Policy
- Upgrade/Cancel PRO subscription
- Invite your friends (optional)
- Request account deletion or provide feedback

---

### 9.1 Profile Picture

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-002 | Upload profile picture - lần đầu | Positive | P0 |

**Pre-condition:** User chưa có profile picture

**Steps:**
1. Click nút (+)
2. Thấy message "1 photo • 1 face • PG only"
3. Upload ảnh có 1 mặt người, nội dung phù hợp

**Expected:**
- AWS Rekognition DetectFaces API: detect 1 human face → pass
- AWS Rekognition DetectModerationLabels API: no nudity/sexual/violence → pass
- Profile picture hiển thị thành công

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-003 | Upload ảnh không có mặt người | Negative | P0 |

**Steps:**
1. Click (+), upload ảnh phong cảnh (0 faces)

**Expected:**
- DetectFaces API: 0 faces → REJECT
- Error message thông báo cần 1 khuôn mặt

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-004 | Upload ảnh có nhiều mặt người | Negative | P1 |

**Steps:**
1. Click (+), upload ảnh nhóm (2+ faces)

**Expected:**
- DetectFaces API: >1 faces → REJECT
- Yêu cầu upload ảnh có đúng 1 mặt

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-005 | Upload ảnh vi phạm nội dung (nudity/violence) | Negative | P0 |

**Steps:**
1. Click (+), upload ảnh có nội dung không phù hợp

**Expected:**
- DetectFaces: 1 face → pass
- DetectModerationLabels: detected → REJECT
- Error message

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-006 | Update profile picture | Positive | P1 |

**Pre-condition:** User đã có profile picture

**Steps:**
1. Click (+), upload ảnh mới hợp lệ

**Expected:**
- Ảnh cũ bị thay thế (chỉ lưu 1 ảnh)
- Ảnh mới hiển thị
- Matched-Users sẽ thấy ảnh mới

---

### 9.2 Change Display Name

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-007 | Đổi display name thành công | Positive | P1 |

**Steps:**
1. Click icon pencil bên cạnh tên
2. Nhập tên mới hợp lệ "NewName"
3. Confirm

**Expected:**
- Tên cập nhật thành "NewName"
- Matched-Users sẽ thấy tên mới trong My Messages

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-008 | Đổi tên thành banned name | Negative | P0 |

**Steps:**
1. Click pencil, nhập "administrator"

**Expected:**
- Hệ thống từ chối, không cho phép dùng banned name

---

### 9.3 Change Location

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-009 | Đổi location thành công | Positive | P0 |

**Pre-condition:** User ở Sydney, có matches

**Steps:**
1. Click "Change my location"
2. Chọn "New York City, NY"

**Expected:**
- Location cập nhật thành NYC
- Algo DỪNG search ở Sydney, BẮT ĐẦU search ở NYC
- Tags hiện tại được dùng tại NYC
- Existing Matched-Users vẫn giữ nguyên (KHÔNG unmatch)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-010 | Đổi location không ảnh hưởng PRO status | Edge Case | P1 |

**Pre-condition:** PRO user ở Sydney

**Steps:**
1. Đổi location sang NYC

**Expected:**
- Vẫn là PRO user
- Tất cả PRO features vẫn hoạt động

---

### 9.4 Subscription Management

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-011 | Free user - click Upgrade/Cancel → redirect to Upgrade page | Positive | P1 |

**Pre-condition:** Free user

**Steps:**
1. Click "Upgrade/Cancel PRO subscription"

**Expected:**
- Mở trang Upgrade to PRO (giống click từ sidebar)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-012 | PRO user - Cancel subscription | Positive | P0 |

**Pre-condition:** PRO user

**Steps:**
1. Click "Upgrade/Cancel PRO subscription"
2. Hệ thống hỏi xác nhận với đầy đủ policy wording
3. Click "Cancel my PRO subscription"

**Expected:**
- Subscription cancelled
- Ngưng billing cho tương lai
- Vẫn giữ PRO access đến hết billing period hiện tại
- Gửi Pro Cancellation Email với ngày hết hạn PRO

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-013 | PRO user - Choose "Continue using PRO" | Positive | P1 |

**Steps:**
1. Click "Upgrade/Cancel PRO subscription"
2. Click "Continue using PRO"

**Expected:**
- Không có gì thay đổi, quay lại My Profile
- PRO subscription vẫn active

---

### 9.5 Các chức năng khác

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-014 | About and FAQs mở modal | Positive | P2 |

**Steps:**
1. Click "About and FAQs"

**Expected:**
- Modal pop-up mở với nội dung
- X ở góc trên phải để đóng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-015 | Request account deletion | Positive | P2 |

**Steps:**
1. Click "Request account deletion or provide feedback"

**Expected:**
- Modal pop-up: "To request account deletion or to provide feedback, kindly email us at support@connectortag.com"
- X ở góc trên phải để đóng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| PROF-016 | Invite your friends (Optional) | Positive | P3 |

**Steps:**
1. Click "Invite your friends!"

**Expected:**
- Cho phép gửi message qua WhatsApp / FB Messenger / SMS:
  "I am using ConnectorTag. Try today for free!
  www.connectortag.com"

---

## Module 10: Super Admin Page

### 10.1 Authentication & Access

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-001 | Admin login bằng Google | Positive | P0 |

**Steps:**
1. Truy cập trang Super Admin
2. Login bằng Google account được cấp quyền admin

**Expected:**
- Login thành công
- Dashboard cơ bản hiển thị (không cần fancy)

---

### 10.2 Export Data

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-002 | Export Tag database to CSV | Positive | P0 |

**Steps:**
1. Vào Tag database
2. Click Export CSV

**Expected:**
- File CSV chứa: Tag ID, Tag name, Usage count (desc), Banned (yes/no), Censored (yes/no)
- Count chỉ đếm tags đang active

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-003 | Export Users database to CSV | Positive | P0 |

**Expected:**
- CSV chứa đầy đủ fields: Google User ID, Email, First/Last name (Google), Display name, PRO status, Profile pic status, Account status, City, Tags, Match count, Match IDs, Messages count, Sign-up date, PRO dates, Cancel dates, Last active timestamp

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-004 | Export Matches database to CSV | Positive | P0 |

**Expected:**
- CSV chứa: Match ID, User IDs (A & B), City, Min matching tags (cả 2 users), Tags của cả 2 users, Match created date, Match deleted date, Deletion reason

---

### 10.3 Tag Management

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-005 | Add new tag (manually) | Positive | P0 |

**Steps:**
1. Vào Tag database → Add new tag
2. Nhập tag name

**Expected:**
- Tag mới được tạo với Tag ID mới
- Usage count = 0

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-006 | Add tag to banned tags | Positive | P0 |

**Steps:**
1. Chọn 1 Tag ID
2. Đánh dấu là "Banned"

**Expected:**
- Tag ID thêm vào directory banned tags
- Tự động thêm vào directory censored tags (vì mọi banned = censored)
- Tag không tham gia matching nữa
- Tag không hiển thị trên Popular Tags

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-007 | Add tag to censored tags only | Positive | P0 |

**Steps:**
1. Chọn 1 Tag ID
2. Đánh dấu là "Censored" (KHÔNG banned)

**Expected:**
- Tag vẫn tham gia matching (algo vẫn dùng)
- Tag KHÔNG hiển thị trên Popular Tags
- Tag tiếp theo trong ranking thay thế vị trí

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-008 | Remove tag from banned tags | Positive | P1 |

**Steps:**
1. Chọn tag đang banned
2. Gỡ khỏi banned

**Expected:**
- Tag không còn banned
- Tag VẪN CÒN censored (chỉ gỡ banned, không gỡ censored)
- Tag tham gia lại matching

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-009 | Remove tag from censored tags | Positive | P1 |

**Steps:**
1. Chọn tag đang censored (không banned)
2. Gỡ khỏi censored

**Expected:**
- Tag có thể xuất hiện lại trên Popular Tags (nếu đủ count >= 20)

---

### 10.4 User Management

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-010 | Delete user and data | Positive | P0 |

**Steps:**
1. Tìm user trong Users database
2. Click Delete

**Expected:**
- User bị xóa hoàn toàn
- Tất cả data liên quan bị xóa
- Matches bị xóa
- Tags count giảm tương ứng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-011 | Delete/reject profile picture | Positive | P1 |

**Steps:**
1. Tìm user → view profile picture
2. Click delete/reject

**Expected:**
- Profile picture bị xóa
- User thấy greyed-out headshot

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-012 | Ban user | Positive | P0 |

**Steps:**
1. Tìm user → click Ban

**Expected:**
- User account status = "banned"
- User không thể đăng nhập

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-013 | Unban user | Positive | P1 |

**Steps:**
1. Tìm banned user → click Unban

**Expected:**
- User account status = "active"
- User có thể đăng nhập lại

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-014 | Change user subscription (free ↔ PRO) | Positive | P1 |

**Steps:**
1. Tìm free user → Change to PRO

**Expected:**
- User trở thành PRO user
- PRO features khả dụng ngay

---

### 10.5 Match Management

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-015 | Admin unmatch users | Positive | P1 |

**Steps:**
1. Tìm match trong Matches database
2. Click Unmatch

**Expected:**
- Match bị xóa
- Reason: "admin"
- Cả hai users không còn thấy nhau

---

### 10.6 Subscription Management (Stripe)

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-016 | View active PRO users | Positive | P0 |

**Expected:**
- Danh sách PRO users active
- Renewal dates
- Payment status

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-017 | View churned users & payment failures | Positive | P1 |

**Expected:**
- Danh sách users đã cancel
- Danh sách payment failures

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-018 | Manually cancel subscription | Positive | P1 |

**Steps:**
1. Tìm PRO user
2. Click cancel subscription

**Expected:**
- Subscription cancelled trên Stripe
- User trở về free sau hết billing period

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-019 | Manually grant free PRO | Positive | P1 |

**Steps:**
1. Tìm free user
2. Grant free PRO

**Expected:**
- User có PRO access miễn phí

---

### 10.7 Directories Management

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-020 | Manage banned names directory | Positive | P1 |

**Steps:**
1. Add/Remove words from banned names

**Expected:**
- Banned names bao gồm: admin, administrator, user admin, official account, Connector Tag, connectortag + tất cả censored tags
- Users không thể dùng banned names khi đăng ký hoặc đổi tên

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-021 | View Waiting List | Positive | P2 |

**Expected:**
- Danh sách email + city,country từ users yêu cầu thông báo

---

### 10.8 Moderation

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-022 | View message metadata (không nội dung) | Positive | P1 |

**Expected:**
- Chỉ hiển thị metadata: timestamps, message counts
- KHÔNG hiển thị nội dung tin nhắn (privacy)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| ADM-023 | View message content khi flagged | Positive | P1 |

**Pre-condition:** Conversation được flag (MVP: admin manual flag)

**Expected:**
- Admin có thể đọc nội dung tin nhắn khi conversation bị flag

---

## Module 11: Email System

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| EMAIL-001 | Welcome Email khi đăng ký | Integration | P0 |

**Pre-condition:** New user vừa đăng ký thành công

**Expected:**
- Email gửi đến địa chỉ Google của user
- Nội dung Welcome Email đúng template

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| EMAIL-002 | PRO Subscription Email | Integration | P0 |

**Pre-condition:** User vừa upgrade PRO thành công

**Expected:**
- Email chứa:
  - Free trial end date (DD-MMM-YYYY)
  - First payment date
  - Subscription term
  - Subsequent payment info

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| EMAIL-003 | PRO Cancellation Email | Integration | P0 |

**Pre-condition:** PRO user vừa cancel subscription

**Expected:**
- Email chứa: ngày hết hạn PRO access

---

## Module 12: Cross-Module / Integration Tests

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-001 | Full user journey: Sign-up → Tags → Match → Message | Integration | P0 |

**Steps:**
1. User A: Sign-up tại Sydney, nhập 5 tags
2. User B: Sign-up tại Sydney, nhập 5 tags (2+ tags trùng A)
3. Cả hai kiểm tra My Matches
4. A mở Messages với B, gửi "Hello"
5. B mở Messages với A, đọc và reply

**Expected:**
- Flow hoàn chỉnh, không lỗi
- Match xuất hiện cho cả hai
- Tin nhắn gửi/nhận thành công

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-002 | Free → PRO upgrade journey | Integration | P0 |

**Steps:**
1. Free user đăng ký, nhập 5 tags, click START
2. Click "Upgrade to PRO" từ sidebar
3. Hoàn tất payment
4. Quay lại My Tags → thấy 12 fields
5. Thêm tags, adjust min matching

**Expected:**
- Smooth transition từ Free sang PRO
- Existing tags giữ nguyên
- 7 fields mới trống
- Min matching tags adjustable

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-003 | PRO cancel → revert to Free | Integration | P0 |

**Steps:**
1. PRO user cancel subscription
2. Chờ hết billing period
3. Kiểm tra My Tags

**Expected:**
- My Tags hiển thị Free version (5 fields)
- Tags 6-12 bị xóa/ẩn?
- Min matching tags reset về 2
- Existing matches vẫn giữ nguyên

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-004 | Change location → algo restart | Integration | P0 |

**Steps:**
1. User ở Sydney, có 3 matches
2. Change location sang Melbourne
3. Nhập/giữ tags, click START

**Expected:**
- 3 matches cũ giữ nguyên
- Algo tìm match mới tại Melbourne
- Popular Tags hiển thị data Melbourne

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-005 | Unmatch → có thể match lại | Integration | P1 |

**Steps:**
1. A và B matched
2. A unmatch B
3. B thay đổi tags + click START
4. A thay đổi tags + click START (cùng location, đủ tags trùng)

**Expected:**
- A và B có thể match lại nếu tags đủ điều kiện
- Success message đã nói rõ: "you may match again in future"

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-006 | Banned user không đăng nhập được | Integration | P0 |

**Steps:**
1. Admin ban User A
2. User A thử Sign-in

**Expected:**
- User A không thể đăng nhập
- Error message phù hợp

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-007 | Admin delete profile pic → user thấy greyed-out | Integration | P1 |

**Steps:**
1. Admin xóa profile pic User A
2. User A vào My Profile
3. Matched-User B xem My Matches

**Expected:**
- A thấy greyed-out headshot (có thể upload lại)
- B thấy greyed-out headshot cho A

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| INT-008 | Tag banned → censored tag xuất hiện trên banned names | Integration | P1 |

**Pre-condition:** Admin thêm tag "badword" vào banned tags

**Expected:**
- "badword" cũng tự động nằm trong censored tags
- "badword" cũng nằm trong banned names (user không thể dùng làm tên)
- "badword" không tham gia matching
- "badword" không hiển thị trên Popular Tags

---

## Module 13: UI/UX & Responsive

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-001 | Error messages hiển thị màu đỏ | Positive | P1 |

**Expected:**
- Mọi error messages trên toàn app hiển thị màu đỏ
- Vị trí gần field/button liên quan

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-002 | Logo favicon | Positive | P2 |

**Expected:**
- Browser favicon sử dụng logo ngắn của ConnectorTag

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-003 | Responsive trên Mobile | Positive | P0 |

**Expected:**
- Layout phù hợp trên mobile
- Bàn phím mở khi click text fields
- Swipe gestures hoạt động (Messages page)

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-004 | Responsive trên Tablet | Positive | P1 |

**Expected:**
- Layout phù hợp trên tablet
- Sidebar hoạt động đúng

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-005 | Responsive trên Desktop | Positive | P0 |

**Expected:**
- Hover sidebar hoạt động
- Layout phù hợp trên desktop

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| UI-006 | Modal pop-ups đều có nút X đóng | Positive | P1 |

**Expected:**
- Mọi modal: ToS, Privacy Policy, Subscription Policy, About/FAQs, HELP, Choose City, Account Deletion → đều có nút X ở góc trên phải

---

## Module 14: Security & Data

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| SEC-001 | Google OAuth - chỉ hỗ trợ Google login | Positive | P0 |

**Expected:**
- Chỉ Sign-up/Sign-in qua Google
- Không có username/password thường

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| SEC-002 | Profile picture chỉ visible cho User, Matched-Users, Admin | Positive | P0 |

**Expected:**
- User thấy ảnh mình
- Matched-Users thấy ảnh qua My Matches/Messages
- Admin thấy qua admin panel
- Users KHÔNG matched KHÔNG thấy ảnh của nhau

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| SEC-003 | Message content chỉ admin thấy khi flagged | Positive | P1 |

**Expected:**
- Admin chỉ thấy metadata (timestamps, counts) bình thường
- Chỉ thấy nội dung khi conversation bị flag

---

| TC ID | Tên | Type | Priority |
|-------|-----|------|----------|
| SEC-004 | Last active timestamp chính xác | Positive | P1 |

**Expected:**
- Last active = most recent of: login / tag update / message sent
- Browser tab đang mở (background) = vẫn logged-in/Online

---

---

## Tổng kết

| Module | Số Test Cases | P0 | P1 | P2 | P3 |
|--------|:---:|:---:|:---:|:---:|:---:|
| Landing Page | 23 | 12 | 7 | 3 | 1 |
| Navigation Sidebar | 5 | 2 | 2 | 1 | 0 |
| My Tags (Free + PRO) | 24 | 12 | 9 | 1 | 2 |
| Matching Algorithm | 11 | 7 | 3 | 0 | 1 |
| My Matches | 17 | 5 | 8 | 3 | 1 |
| My Messages | 10 | 4 | 4 | 2 | 0 |
| Popular Tags | 5 | 3 | 1 | 1 | 0 |
| Upgrade to PRO | 7 | 4 | 1 | 2 | 0 |
| My Profile | 16 | 5 | 7 | 3 | 1 |
| Super Admin | 23 | 7 | 12 | 3 | 1 |
| Email System | 3 | 3 | 0 | 0 | 0 |
| Integration Tests | 8 | 4 | 3 | 0 | 1 |
| UI/UX | 6 | 2 | 2 | 2 | 0 |
| Security | 4 | 2 | 2 | 0 | 0 |
| **TỔNG** | **~162** | **~72** | **~61** | **~21** | **~8** |

---

## Lưu ý quan trọng cho QC Team

1. **Configurable values** - Giá (12.99), currency (AUD), free trial (10 ngày) KHÔNG hardcode. Verify bằng cách thay đổi config và kiểm tra.
2. **Banned vs Censored logic** - Mọi banned tag là censored tag, nhưng KHÔNG ngược lại. Test kỹ logic này.
3. **Matching algorithm** - Test kỹ boundary cases: duplicate tags matching, min matching tags rule áp dụng theo user nào cao hơn.
4. **Real-time behavior** - Online status, match notifications, message delivery cần test với 2 sessions đồng thời.
5. **Stripe integration** - Test với Stripe test mode, verify billing address restriction (Australia only) và card issuer restriction.
6. **AWS Rekognition** - Test với nhiều loại ảnh: no face, multiple faces, inappropriate content, edge cases.
7. **Data consistency** - Khi unmatch/delete, verify data bị xóa ở CẢ HAI phía.
8. **Tag processing** - Auto-lowercase, trim spaces, collapse multiple spaces - test tất cả combinations.
