# DATA-SSOT — Kênh dữ liệu đồng bộ (tùy chọn)

> Bảng dữ liệu chung là **tùy chọn**. Nếu workspace có dùng, đó là **single source of truth** cho
> nội dung cập nhật. File (Excel/Sheet/CSV) chỉ là *snapshot kết xuất*, không phải nơi cập nhật.

## Vì sao
Mỗi người sửa một bản Excel rời sẽ tạo ra nhiều phiên bản, không ai biết bản nào đúng, tốn thời
gian gộp và recheck. Khi nội dung nằm tập trung trên một kênh đồng bộ online, ai cũng cập nhật vào
đó và mọi deliverable lấy ra từ một nguồn.

## Chọn Google Sheets hay Airtable

| Tiêu chí | Google Sheets | Airtable |
|----------|---------------|----------|
| Quen thuộc, không cần học | Có | Cần làm quen |
| Chèn ảnh trực tiếp vào ô | Không | Có |
| View, lọc, theo dõi cập nhật | Cơ bản | Mạnh |
| Khuyến nghị khi | Bắt đầu nhanh, dữ liệu đơn giản | Content nhiều hình ảnh, cần theo dõi chặt |

Nếu đã quen Sheets thì bắt đầu với Sheets là đủ. Cần đồng nhất content kèm hình ảnh và theo dõi
cập nhật chặt hơn thì dùng Airtable.

## Quy tắc
1. **Cập nhật nội dung đi thẳng vào kênh đồng bộ**, không sửa vào file kết xuất rồi gửi qua lại.
2. **Một nguồn, nhiều view**: mỗi nhu cầu (theo dự án/giai đoạn/người phụ trách) là 1 view, không tách nguồn mới.
3. **AI không tự tạo, không hỏi copy tay.** Cần dữ liệu thì gọi connector (mục dưới).
4. **Mọi snapshot ghi xuất xứ**: ngày lấy, số bản ghi, nguồn (link hoặc base/table/view).
5. **Secret chỉ ở `.env`.** Không token trong chat/Markdown/Git. Lộ thì rotate.

## Cập nhật content giữa các team (giảm recheck)
Mục tiêu: nhiều team cùng cập nhật mà không tốn nhiều nhân lực kiểm tra chéo.
1. Mọi thay đổi đi qua kênh đồng bộ, không gửi file rời qua lại.
2. Mỗi bản ghi gắn **trạng thái**: `Draft`, `Cần duyệt`, `Đã duyệt`. Team khác nhìn trạng thái để biết cái gì đã chốt.
3. **AI tự rà soát** ngay trên kênh: sai format, thiếu trường, sai thuật ngữ (đối chiếu GLOSSARY), trùng lặp, thiếu ảnh.
4. Người chỉ xử lý phần AI gắn cờ, không recheck từng dòng.

## Cách AI lấy dữ liệu (nếu dùng Airtable)
Chạy từ folder workspace:

```bash
python3 scripts/airtable_inspect.py "<AIRTABLE_URL>" --max-records 100 --format json
```

Output dùng làm context: `columns`, `rows`, `raw_records`. Cần cả dataset cho Excel/slide thì tăng
`--max-records` và ghi rõ giới hạn đã lấy. Chi tiết scope token và lỗi thường gặp: `README.md`.
Với Google Sheets, dùng link share (quyền xem) hoặc export CSV làm nguồn.

## Cấu hình nguồn dữ liệu (chốt khi init)

| Thành phần | Giá trị |
|------------|---------|
| Công cụ | `<CẦN CHỐT: Google Sheets / Airtable / không dùng>` |
| Link hoặc Base ID | `<CẦN CHỐT>` |
| View theo dự án | `<CẦN CHỐT: mỗi dự án 1 view>` |
| Người sở hữu (quản quyền) | `<CẦN CHỐT>` |

## Ranh giới file vs kênh đồng bộ

| Để ở file (Git/Drive) | Để ở kênh đồng bộ |
|-----------------------|-------------------|
| Luật, brand, template, script | Records, danh sách, nội dung, trạng thái |
| Deliverable đã chốt (snapshot có ngày) | Mọi dữ liệu còn thay đổi |
| README/context dự án | Dữ liệu nhiều người cùng sửa |

---
*Mục `<CẦN CHỐT>` chốt qua INIT-GUIDE, Bước 5 (Data).*
