# BOOTSTRAP-PROMPT · Tự dựng Foundation bằng 1 prompt

> Cách dùng: mở Claude Code hoặc Codex tại folder gốc của workspace (vd. folder đã sync từ Cloud
> Drive), bỏ sẵn tư liệu brand (slide mẫu, Excel mẫu, logo, bảng màu) vào folder, dán nguyên khối
> prompt dưới đây vào terminal và Enter. AI sẽ tự tạo toàn bộ cấu trúc folder và file, người dùng
> không tạo gì bằng tay. Sau khi xong, chạy "guide init" để điền các mục CẦN CHỐT.

---

```text
Bạn là trợ lý setup chuẩn hóa workspace cho team. Hãy TẠO toàn bộ cấu trúc folder và file dưới đây ngay trong folder hiện tại; người dùng không tạo gì bằng tay. Viết toàn bộ bằng tiếng Việt, không dùng em-dash. Không tự tạo số liệu không có nguồn, không in token. Nếu file đã tồn tại thì hỏi trước khi ghi đè. Nếu trong folder đã có sẵn tư liệu brand (ví dụ folder Assets/: slide mẫu, Excel mẫu, logo, bảng màu), hãy đọc và dùng làm nền tảng khi sinh BRAND.md và template.

Cấu trúc mục tiêu của workspace:
WORKSPACE/
  README.md           (giới thiệu workspace, mô tả cấu trúc, trỏ tới _foundation)
  _foundation/        (guideline: toàn bộ luật chung)
  (mỗi dự án sau này là 1 folder riêng, tạo từ _foundation/init/project-template)

Tạo `README.md` ở gốc: giới thiệu workspace; mô tả cấu trúc (README, _foundation là guideline, mỗi dự án 1 folder); hướng dẫn người dùng đọc _foundation/00-START-HERE.md trước, dùng _foundation/init/onboarding-new-member.md để onboard, và _foundation/init/INIT-GUIDE.md để chốt guideline.

Tạo folder `_foundation/` với các file:

1. `00-START-HERE.md`: điểm vào AI đọc đầu tiên. Phải nêu BƯỚC 0 bắt buộc đọc luật trước khi làm; thứ tự ưu tiên "lệnh user, rồi _foundation/RULES.md, rồi context dự án, rồi mặc định AI"; 3 quy tắc vàng: (a) không tự ý lệch concept/brand/term, khác chuẩn thì hỏi confirm; (b) một nguồn sự thật, nếu dùng kênh đồng bộ thì dữ liệu nằm ở đó, file chỉ là snapshot; (c) tái lập được, deliverable kèm script.

2. `RULES.md`: luật cứng R1 tới R7. R1 đọc foundation trước; R2 nếu workspace dùng bảng dữ liệu chung (tùy chọn) thì lấy dữ liệu cập nhật từ đó (Google Sheets hoặc Airtable), không hỏi user copy tay, không nhận token qua chat; R3 brand và format (tiền VND #,##0, ngày dd/mm/yyyy, tiếng Việt); R4 dùng đúng thuật ngữ trong GLOSSARY và ngữ điệu trong TONE-OF-VOICE; R5 mỗi dự án 1 folder, đặt tên chuẩn; R6 tái lập bằng script (Excel openpyxl, Word python-docx, PPTX python-pptx); R7 không commit secret, token lộ thì rotate. Kết bằng checklist trước khi giao deliverable.

3. `BRAND.md`: bảng màu token (cột vai trò, tên, hex, dùng cho); nếu trong folder đã có tư liệu brand (slide, Excel mẫu, logo, bảng màu) thì trích ra để điền, nếu chưa có thì để giá trị là CẦN CHỐT; typography; format số và ngày; logo.

4. `STRUCTURE.md`: sơ đồ folder (workspace gồm README, _foundation, mỗi dự án 1 folder; tiền tố _ cho folder hệ thống; mỗi dự án tự chứa README, scripts, assets, deliverables); quy ước đặt tên file dạng loai-chu-de-pham-vi-yyyy-mm-dd.ext, chữ thường, gạch nối, không dấu; hướng dẫn tạo dự án mới từ template.

5. `TONE-OF-VOICE.md`: tiếng Việt chuyên nghiệp; kết luận trước dẫn chứng sau (Pyramid Principle); mọi nhận định có số liệu hoặc nguồn; không dùng em-dash; khuyến nghị trình bày 2 phương án và 1 đề xuất kèm trade-off.

6. `GLOSSARY.md`: bảng thuật ngữ chuẩn (cột từ chuẩn, viết tắt, EN, định nghĩa, biến thể cấm dùng); quy tắc gặp thuật ngữ mới thì thêm dòng trước khi dùng.

7. `DATA-SSOT.md`: bảng dữ liệu chung là tùy chọn; nếu dùng thì đó là single source of truth cho dữ liệu cập nhật, ưu tiên Airtable (chèn được ảnh vào ô, theo dõi cập nhật tốt) hoặc Google Sheets nếu đã quen; file chỉ chứa snapshot có ngày; cấm sửa file rời rồi gửi qua lại; nếu dùng Airtable, cách lấy dữ liệu là chạy python3 scripts/airtable_inspect.py "URL" --max-records 100 --format json từ folder workspace; thêm quy trình cập nhật content giữa các team: mọi thay đổi đi qua kênh đồng bộ, mỗi bản ghi có trạng thái (Draft, Cần duyệt, Đã duyệt), AI tự rà soát format và thuật ngữ trước khi người duyệt; mục cấu hình nguồn dữ liệu để CẦN CHỐT (công cụ, link hoặc Base ID, view theo dự án, người sở hữu).

8. `init/INIT-GUIDE.md`: quy trình guide init chạy 1 lần, 6 bước confirm và điền: (1) Brand, (2) Structure, (3) Tone, (4) Glossary, (5) Data, (6) rà dự án và shim. Mỗi bước AI đọc file luật và tư liệu brand đã bỏ vào folder, hỏi user xác nhận hoặc điền chỗ CẦN CHỐT, ghi vào file, tick checklist. Kết bằng bump version.

9. `init/onboarding-new-member.md`: 5 bước onboard người mới khoảng 10 phút (lấy folder đã sync; cấu hình kênh dữ liệu nếu có; bảo AI đọc luật trước; quy tắc bất di bất dịch; khi bí đọc RULES).

10. `init/project-template/README.md` và `init/project-template/AGENTS.md`: template tạo dự án mới, kế thừa foundation, chỉ ghi cái riêng của dự án; AGENTS.md template có BƯỚC 0 trỏ về ../_foundation/00-START-HERE.md.

Tạo hoặc ghi đè ở GỐC folder hiện tại:
- `AGENTS.md` và `CLAUDE.md`: shim BƯỚC 0 trỏ về _foundation/00-START-HERE.md, nêu thứ tự ưu tiên và quy tắc kênh dữ liệu. Hai file dùng chung một nguồn luật để Claude và Codex không lệch nhau.
- `.gitignore`: thêm .DS_Store, __pycache__/, *.py[cod], .env, .env.*, !.env.example, token.md.
- `.env.example`: nội dung AIRTABLE_TOKEN=pat_xxx.

Sau khi tạo xong, in cây thư mục đã tạo. Tiếp đó CHẠY LUÔN guide init mà không cần tôi gọi lại: lần lượt đi qua 6 tiêu chí (Brand, Structure, Tone, Glossary, Data, Shim). Với mỗi tiêu chí, đọc tư liệu brand trong folder nếu có, đề xuất giá trị cho các mục CẦN CHỐT, hỏi tôi xác nhận hoặc chỉnh sửa, ghi vào file tương ứng rồi sang tiêu chí kế. Hỏi từng tiêu chí một, không hỏi dồn. Hết 6 tiêu chí thì tóm tắt thay đổi và bump version trong 00-START-HERE.md.
```

---

## Biến thể cho dự án mới (workspace đã có Foundation)
Nếu chỉ tạo 1 dự án con trong workspace đã có foundation, dán prompt ngắn này:

```text
Tạo dự án mới tên "TEN-DU-AN" trong workspace này: copy _foundation/init/project-template/ thành folder ten-du-an (chữ thường, gạch nối), rồi điền README.md theo mô tả tôi sẽ cung cấp. Trước khi làm, đọc _foundation/00-START-HERE.md và tuân RULES, BRAND, STRUCTURE, GLOSSARY, TONE.
```
