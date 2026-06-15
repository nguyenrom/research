# BRAND — Nhận diện VLU

> VLU dùng **palette riêng**, KHÔNG dùng Blue Coral (`_brand/` ở repo root chỉ cho tài liệu mới
> của Blue Coral). Palette dưới đây trích từ các report VLU đã phát hành.

## Bảng màu (token)

| Vai trò      | Tên          | Hex        | Dùng cho |
|--------------|--------------|------------|----------|
| Primary      | VLU Navy     | `#1a3a5c`  | Tiêu đề, header, thanh chính |
| Accent       | VLU Gold     | `#d4a418`  | Nhấn, số liệu nổi bật, đường kẻ nhấn |
| Surface      | Cream        | `#f9f8f5`  | Nền tài liệu |
| Secondary    | Sky          | `#3a7abc`  | Link, biểu đồ phụ |
| Alert        | Red          | `#e63946`  | Cảnh báo (dùng tiết chế) |
| Deep accent  | Maroon       | `#7e1f2e`  | Nhấn sang trọng, footer |

Quy ước: **status** (đúng/sai/cảnh báo) chỉ dùng đỏ/xanh lá tiêu chuẩn, không dùng Gold cho status.

## Typography
- Sans: hệ thống (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`).
- Mono (số/code): `ui-monospace, SFMono-Regular, Menlo, monospace`.
- `<CẦN CHỐT>`: font thương hiệu chính thức nếu VLU có (vd. font tuyển sinh).

## Format chuẩn
- Tiền VND: `#,##0` (vd. `1,250,000`). Ngày: `dd/mm/yyyy`.
- Ngôn ngữ mặc định: tiếng Việt.

## Logo & tài sản
- `<CẦN CHỐT>`: đường dẫn file logo chính thức (SVG/PNG), vùng an toàn, kích thước tối thiểu.

## Office (Excel/Word/PPTX)
- Lấy màu từ bảng token trên, không gõ hex rời rạc trong từng script.
- `<CẦN CHỐT>`: có cần `vlu_brandkit.py` riêng (giống `_brand/brandkit.py`) để tái dùng token không?

---
*Mục `<CẦN CHỐT>` chốt qua `_foundation/init/INIT-GUIDE.md` — Bước 1.*
