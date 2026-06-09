# HAWEE — Nền tảng Hội viên · Bộ tài liệu pitch

Khách hàng: **HAWEE (Hội Nữ Doanh nhân TP.HCM)**. Đề xuất nền tảng số xây riêng cho HAWEE.

## Cấu trúc thư mục

| File | Mô tả |
|---|---|
| `hawee-pitch-deck.html` | **Bản trình chiếu chính** (v3.1, 46 slide). Mở bằng trình duyệt, điều hướng phím ‹ ›. Đây là bản gốc chuẩn. |
| `hawee-pitch-deck.pptx` | Bản PowerPoint chỉnh sửa được (mirror của HTML), biểu đồ & bảng native. |
| `build_hawee_pptx.py` | Script tạo lại file `.pptx`. |
| `research/domain-hawee-membership-platform-research-2026-05-18.md` | Nghiên cứu domain (bối cảnh, vấn đề, giải pháp, lộ trình). |
| `research/market-association-membership-platform-vietnam-research-2026-05-18.md` | Nghiên cứu thị trường đầy đủ (quy mô, khách hàng, cạnh tranh, khuyến nghị). |
| `research/pitch-hawee-platform-outline-2026-05-18.md` | Outline pitch (bản trước v3, giữ để tham khảo cấu trúc). |

## Tạo lại bản PPTX sau khi sửa script

```
.venv-pptx/bin/python hawee-pitch/build_hawee_pptx.py
```

(Cần `.venv-pptx` ở gốc repo với `python-pptx`. Nếu chưa có:
`python3 -m venv .venv-pptx && .venv-pptx/bin/pip install python-pptx`)

## Ràng buộc khi chỉnh sửa (khách yêu cầu, luôn giữ)

1. Tiếng Việt là chính, hạn chế thuật ngữ.
2. Không dùng dấu gạch ngang trong slide.
3. Thông điệp lạc quan ("rời tổ chức", không "mất").
4. Một phương án duy nhất: xây riêng cho HAWEE (không so sánh giải pháp bên thứ ba).
5. Số liệu mockup ghi rõ "Mô phỏng minh họa"; giữ disclaimer ở slide xác minh AI.
6. Phong cách navy/trắng tối giản, mockup kiểu CRM nhiều widget + biểu đồ thật.

Sửa nội dung trong `hawee-pitch-deck.html` (mỗi slide là một `<section class="slide">`), sau đó cập nhật `build_hawee_pptx.py` và chạy lại để đồng bộ bản PPTX.
