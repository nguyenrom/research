# INIT-GUIDE — "guide init" (chạy 1 lần khi lập workspace)

> Người chạy: **lead/owner** của workspace (không phải mỗi thành viên).
> Mục tiêu: đi qua từng nhóm luật, **confirm hoặc điền** các mục `<CẦN CHỐT>`, rồi commit.
> Cách dùng với AI: mở Claude/Codex tại `VLU/` và nói: *"Chạy guide init theo
> `_foundation/init/INIT-GUIDE.md`, hỏi tôi từng bước."* AI sẽ dẫn bạn qua 6 bước dưới.

## Cách hoạt động
Mỗi bước: (1) AI đọc file luật tương ứng → (2) hỏi bạn xác nhận/điền chỗ `<CẦN CHỐT>` →
(3) ghi vào file → (4) tick checklist. Hết 6 bước → bump version ở `00-START-HERE.md` → commit.

---

### Bước 1 — BRAND  (`BRAND.md`)
Confirm: bảng màu (Navy/Gold/Cream...) có đúng nhận diện VLU hiện tại không?
Điền: `<CẦN CHỐT>` font thương hiệu, đường dẫn logo, có cần `vlu_brandkit.py` không.
- [ ] Brand đã chốt

### Bước 2 — STRUCTURE  (`STRUCTURE.md`)
Confirm: quy ước đặt tên file + sơ đồ folder. Liệt kê các dự án hiện có sẽ được "nắn" về chuẩn.
- [ ] Cấu trúc đã chốt

### Bước 3 — TONE  (`TONE-OF-VOICE.md`)
Confirm: nguyên tắc văn phong. Điền: `<CẦN CHỐT>` xưng hô đối ngoại, mức trang trọng nội bộ/đối ngoại.
- [ ] Ngữ điệu đã chốt

### Bước 4 — GLOSSARY  (`GLOSSARY.md`)
Điền: thuật ngữ tổ chức + khái niệm dự án + số liệu mốc (kèm nguồn) hay bị trích lệch.
- [ ] Thuật ngữ đã chốt

### Bước 5 — DATA SSOT  (`DATA-SSOT.md`)
Điền: Base ID, bảng chính, view theo từng dự án, người sở hữu base.
Kiểm tra: chạy thử `python3 scripts/airtable_inspect.py "<URL>" --max-records 5 --format markdown`.
- [ ] Airtable mapping đã chốt + kết nối chạy được

### Bước 6 — RÀ DỰ ÁN + SHIM
Confirm: `AGENTS.md` và `CLAUDE.md` ở gốc `VLU/` đã trỏ về `_foundation/`.
Mỗi dự án hiện có: đảm bảo có `README.md`. Dự án mới: tạo từ `project-template/`.
- [ ] Shim + các dự án đã chuẩn

---

## Hoàn tất init
1. Bump `Foundation version` trong `00-START-HERE.md` (vd. v0.1 → v1.0).
2. Commit: `git add VLU/_foundation VLU/AGENTS.md VLU/CLAUDE.md && git commit -m "VLU foundation v1.0"`.
3. Báo team: đọc `_foundation/init/onboarding-new-member.md`.

## Khi nào chạy lại
Thay đổi luật lớn (brand mới, đổi base Airtable, thêm quy ước) → cập nhật file tương ứng,
bump version, commit. Không cần chạy full 6 bước cho thay đổi nhỏ.
