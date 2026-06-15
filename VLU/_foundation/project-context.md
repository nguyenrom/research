# Project Context — VLU Workspace Standard

> Context cho AI/thành viên về hệ thống chuẩn hóa làm việc với AI của team VLU.
> Đọc cùng `00-START-HERE.md`. Cập nhật khi có quyết định mới.

## Mục tiêu
Nhiều người dùng AI khác nhau trên cùng dự án dẫn tới lệch concept, brand, thuật ngữ và dữ liệu
phân mảnh. Workspace Standard giải quyết bằng một tầng luật chung mọi AI đọc trước khi làm, giúp
kết quả đồng nhất và giảm thời gian onboard, bàn giao, recheck.

## Quyết định đã chốt
- **Phạm vi:** VLU làm pilot; bộ chuẩn thiết kế để tái sử dụng cho project/team khác.
- **Công cụ:** Cloud Drive (OneDrive/Dropbox/Google Drive) để chứa và chia sẻ + AI (Claude/Codex)
  để thực thi. Bảng dữ liệu chung là **tùy chọn** (Google Sheets hoặc Airtable).
- **AI tools:** Claude + Codex, dùng chung một nguồn luật qua `AGENTS.md` (Codex+Claude) và
  `CLAUDE.md` (Claude). `AGENTS.md`/`CLAUDE.md` chỉ là shim trỏ về `_foundation/`.
- **Kênh dữ liệu:** nếu dùng, ưu tiên Airtable (chèn ảnh vào ô, theo dõi cập nhật) hoặc Sheets nếu
  đã quen. File chỉ là snapshot, dữ liệu cập nhật nằm trên kênh đồng bộ.

## Mô hình 3 tầng
1. **Foundation** (`_foundation/`): luật bất biến, mọi AI đọc trước (brand, structure, tone, term, data).
2. **Project**: mỗi dự án 1 folder, kế thừa Foundation, tạo từ `init/project-template/`.
3. **Data** (tùy chọn): kênh đồng bộ online làm single source of truth cho nội dung cập nhật.

Thứ tự ưu tiên khi mâu thuẫn: lệnh user > `_foundation/RULES.md` > context dự án > mặc định AI.

## Cách dựng và vận hành
- **Dựng:** dán `init/BOOTSTRAP-PROMPT.md` vào terminal AI tại folder workspace → AI tự sinh toàn
  bộ cấu trúc rồi tự chạy guide init (hỏi xác nhận 6 tiêu chí: Brand, Structure, Tone, Glossary,
  Data, Shim) và bump version.
- **Onboard:** `init/onboarding-new-member.md`.
- **Cập nhật content giữa các team:** đi qua kênh đồng bộ, mỗi bản ghi có trạng thái
  (Draft/Cần duyệt/Đã duyệt), AI tự rà soát trước, người chỉ xử lý phần AI gắn cờ → giảm recheck.
- **Tài liệu giới thiệu (cho team):** `VLU-Workspace-Standard.html`.

## Quy ước nội dung
- Tiếng Việt, không dùng em-dash. Không tự tạo số liệu không có nguồn.
- Tiền VND `#,##0`, ngày `dd/mm/yyyy`. Khuyến nghị trình bày 2 phương án + 1 đề xuất.

## Còn mở (CẦN CHỐT khi init thật)
- Palette/font/logo VLU chính thức (bỏ tư liệu vào `Assets/` để AI trích).
- Thuật ngữ và số liệu mốc trong `GLOSSARY.md`.
- Cấu hình nguồn dữ liệu trong `DATA-SSOT.md` (công cụ, link/Base, view, người sở hữu).
- Rotate PAT trong `VLU/token.md` (đang plaintext), chỉ giữ ở `.env`.
