# Prompt: Phân tích & Lập kế hoạch Merge 2 Repo Marketing

> Dán toàn bộ block bên dưới vào Claude Code để khởi chạy.

---

```
/bmad-agent-analyst

# Nhiệm vụ: Phân tích & Lập kế hoạch Merge 2 Repo Marketing theo BMad Method

## Bối cảnh
Tôi có 2 repo marketing đang phát triển song song và muốn hợp nhất chúng theo mô hình BMad Method.

- **Repo nguồn (sẽ được merge vào)**: `/Users/rom/Projects/marketingskills`
- **Repo đích (chuẩn BMad)**: `/Users/rom/Projects/bmad-performance-marketing`
- **Mục tiêu cuối**: Merge `marketingskills` → `bmad-performance-marketing`, giữ lại mô hình BMad làm khung chính, đảm bảo kết quả cuối **tuân thủ đầy đủ quy trình BMad** (agent → skill → workflow → template → config).

## Yêu cầu thực hiện

### 1. Khảo sát từng repo (độc lập)
Với mỗi repo, hãy ghi lại:
- Cấu trúc thư mục cấp 1-2 và mục đích
- Phạm vi nghiệp vụ marketing được cover (channels, workflows, deliverables)
- Artifacts/skills/agents/templates hiện có
- Mức độ hoàn thiện (sơ bộ → production-ready)
- Convention & quy chuẩn (đặt tên file, format SKILL.md, manifest, v.v.)

### 2. Phân tích đối chiếu (side-by-side)
- Vùng **chồng lấn nghiệp vụ** (overlap): cùng giải quyết một bài toán
- Vùng **bổ sung lẫn nhau** (complementary): repo này có, repo kia thiếu
- Vùng **xung đột** (conflict): cùng tên/concept nhưng logic hoặc convention khác nhau — phải nêu rõ conflict cụ thể
- Khoảng cách về convention so với chuẩn BMad

### 3. Tracking Table
Tạo bảng markdown với các cột tối thiểu:

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái (overlap/complement/conflict/unique) | Độ hoàn thiện ms (1-5) | Độ hoàn thiện bpm (1-5) | Hành động đề xuất khi merge | Ghi chú conflict |

Phân nhóm theo: agents, skills, workflows, templates, configs, docs.

### 4. Đánh giá tổng kết
- Repo nào "trưởng thành" hơn về nghiệp vụ, repo nào hơn về cấu trúc?
- Top 5 conflict nghiêm trọng nhất cần giải quyết trước khi merge
- Risk khi merge và cách mitigate

### 5. Đề xuất Naming cho Agent / Skill mới
Với mỗi capability từ `marketingskills` chưa tồn tại trong `bmad-performance-marketing`, đề xuất:

- **Tên agent persona** (nếu cần agent mới): theo convention BMad đang dùng — ví dụ John (PM), Mary (Analyst), Winston (Architect), Sally (UX). Đặt tên người + chuyên môn 1 dòng.
- **Skill ID**: theo convention `bmad-<verb>-<object>` hoặc `bmad-agent-<role>` — ví dụ `bmad-create-campaign-brief`, `bmad-agent-media-buyer`.
- **Display name + menu code** (2-3 ký tự viết tắt): ví dụ `[CB] Create Campaign Brief`.
- **Lý do chọn tên** & alternatives đã cân nhắc (ngắn gọn).

Trình bày dạng bảng:

| Capability gốc (ms) | Loại (agent/skill) | Tên đề xuất | Skill ID | Menu code | Persona (nếu agent) | Lý do |

### 6. Đề xuất Workflow còn thiếu
Đối chiếu với cấu trúc BMad chuẩn (analysis → planning → architecture → execution → review). Với mỗi capability của `marketingskills` chưa có workflow rõ ràng:

- Xác định **phase** phù hợp trong BMad (1-analysis / 2-planning / 3-execution / anytime…)
- Đề xuất **workflow steps** (3-7 bước) theo format `step-NN-<name>.md` của BMad
- Liệt kê **inputs / outputs / dependencies** (after / before skill nào)
- Đề xuất **template** đi kèm nếu cần
- Đánh dấu workflow nào là **required gate** vs **optional**

Trình bày dạng:

```
### Workflow: <tên>
- Phase: <phase>
- Trigger: <khi nào dùng>
- Steps:
  1. step-01-<name> — <mô tả>
  2. step-02-<name> — <mô tả>
  ...
- Inputs: <list>
- Outputs: <list>
- After: <skill>, Before: <skill>
- Required: yes/no
```

### 7. Đề xuất Merge Strategy (high-level)
- Thứ tự merge: cái gì trước, cái gì sau, lý do (nguyên tắc: foundation → agent → skill → workflow → template)
- Hạng mục nào keep / refactor / rewrite / drop
- Cách xử lý conflict cụ thể (ưu tiên convention BMad, giữ nghiệp vụ từ ms)
- Câu hỏi cần tôi quyết định trước khi triển khai

## Output mong muốn
- File báo cáo markdown lưu tại: `/Users/rom/Projects/research/docs/marketing-merge-analysis.md`
- Tracking table phải đầy đủ, không dùng placeholder
- Phần conflict phải dẫn link file/dòng cụ thể
- Bảng naming + workflow đề xuất phải sẵn sàng dùng làm input cho `bmad-customize` ở bước sau

## Ràng buộc
- Chỉ đọc file (read-only), không sửa gì trong 2 repo gốc
- Tuân thủ convention BMad hiện có (xem các skill `bmad-*` đã cài để học pattern naming, format SKILL.md, manifest)
- Nếu thiếu thông tin để đánh giá độ hoàn thiện hoặc đặt tên, **hỏi tôi** thay vì đoán
- Trả lời bằng tiếng Việt
```

---

## Ghi chú sử dụng

- Chạy trong **fresh context window** để Mary có đủ token cho việc đọc cả 2 repo
- Output sẽ nằm tại: `/Users/rom/Projects/research/docs/marketing-merge-analysis.md`
- Nếu muốn chạy lại với 2 repo khác: chỉ cần thay 2 đường dẫn ở phần **Bối cảnh**

## Bước tiếp theo sau khi có report

1. Review tracking table + naming proposals → quyết định keep/drop
2. Chạy `/bmad-customize` để tạo agent/skill mới theo tên đã chốt
3. Chạy `/bmad-create-architecture` (Winston) nếu cần thiết kế lại cấu trúc tổng
4. Implement từng workflow theo thứ tự merge strategy đã đề xuất
