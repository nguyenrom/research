# SoW/JD Dịch Vụ Điều Phối Triển Khai Loyalty Cho Khách Sạn & Nhà Hàng

## 1. Định Vị Dịch Vụ

Dịch vụ này là **Loyalty Implementation Operations Service**: cung cấp nhân sự vận hành triển khai, đứng giữa khách sạn và vendor CRM/loyalty để đảm bảo chương trình loyalty được triển khai thành công trong thực tế.

Dịch vụ không bán phần mềm, không phát triển hệ thống, không sở hữu CRM/loyalty platform. Trọng tâm là biến yêu cầu kinh doanh thành rule, kịch bản vận hành, SOP, UAT, training và go-live readiness cho các bộ phận liên quan, đặc biệt là FO, Reservation, F&B, Cashier và CRM/Admin.

Định vị ngắn gọn:

> Chúng tôi đại diện khách sạn để quản lý triển khai loyalty từ business rules, kịch bản vận hành, phối hợp vendor, UAT, training đến go-live và hypercare.

## 2. Mục Tiêu Dịch Vụ

- Đảm bảo chương trình loyalty được thiết kế đủ rõ để vendor CRM/loyalty cấu hình chính xác.
- Đảm bảo các tình huống vận hành thực tế tại FO, Reservation, F&B và Cashier được xử lý trước khi go-live.
- Giảm rủi ro triển khai sai do khoảng cách giữa business, hotel operation và vendor kỹ thuật.
- Chuẩn hóa SOP, training và checklist để nhân viên khách sạn có thể vận hành loyalty nhất quán.
- Theo dõi issue, bug, dependency và blocker trong quá trình triển khai.
- Đưa hệ thống loyalty vào vận hành với tiêu chí nghiệm thu rõ ràng.

## 3. Phạm Vi Cung Cấp

### 3.1 Bao Gồm

- Implementation PM / Operations Lead.
- Loyalty Business Analyst.
- Người điều phối vendor CRM/loyalty.
- Người điều phối với PMS/POS vendor nếu dự án có tích hợp.
- Người thiết kế kịch bản vận hành FO/F&B.
- Người viết SOP, UAT script, checklist và training material.
- Người hỗ trợ go-live và hypercare trong phạm vi đã thỏa thuận.

### 3.2 Không Bao Gồm

- License CRM/loyalty platform.
- Phí vendor PMS/POS/CRM/loyalty.
- Phát triển API, middleware hoặc custom software.
- Cấu hình kỹ thuật thuộc trách nhiệm vendor, trừ khi được thống nhất riêng.
- Vận hành marketing campaign dài hạn sau go-live.
- Nhập liệu thủ công toàn bộ dữ liệu khách hàng cũ nếu không có scope riêng.
- Chịu trách nhiệm với lỗi kỹ thuật thuộc hệ thống hoặc vendor.
- Cam kết doanh thu trực tiếp nếu không kiểm soát marketing, pricing, sales và hệ thống.

## 4. Vai Trò Cung Cấp

### 4.1 Loyalty Implementation PM / Operations Lead

Trách nhiệm:

- Quản lý kế hoạch triển khai tổng thể.
- Điều phối khách sạn, vendor CRM/loyalty, PMS/POS vendor và các bộ phận vận hành.
- Theo dõi timeline, milestone, dependency, issue và risk.
- Tổ chức kickoff, weekly meeting, UAT review, go-live readiness review.
- Escalate blocker cho Project Sponsor, GM hoặc Owner.
- Đảm bảo các deliverables được hoàn tất và sign-off đúng thời điểm.

Deliverables:

- Project charter.
- Implementation timeline.
- RACI matrix.
- Weekly status report.
- Risk, issue, action log.
- Go-live readiness report.

### 4.2 Loyalty Business Analyst

Trách nhiệm:

- Thu thập yêu cầu loyalty từ khách sạn.
- Làm rõ business rules: earn, burn, tier, voucher, benefit, expiry, exception.
- Chuyển yêu cầu thành kịch bản cấu hình cho vendor.
- Review cấu hình vendor so với rule đã sign-off.
- Viết scenario book, UAT script và exception matrix.

Deliverables:

- Loyalty rules document.
- Tier & benefit matrix.
- Earn/burn scenario book.
- Exception handling matrix.
- Vendor configuration checklist.
- UAT script.

### 4.3 Hotel Operations Consultant / FO-F&B Process Lead

Trách nhiệm:

- Thiết kế SOP cho FO, Reservation, F&B và Cashier.
- Xây dựng kịch bản xử lý tại điểm chạm khách hàng.
- Viết script cho nhân viên khi giới thiệu loyalty, tra cứu member, giải thích benefit và xử lý khiếu nại.
- Tổ chức role-play theo tình huống vận hành thật.
- Đề xuất điều chỉnh quy trình nếu rule loyalty gây vướng tại hiện trường.

Deliverables:

- FO SOP.
- Reservation SOP.
- F&B SOP.
- Cashier SOP.
- Guest complaint / missing point SOP.
- Member enrollment script.
- FO/F&B quick reference sheet.

### 4.4 Training & Change Enablement Lead

Trách nhiệm:

- Chuẩn bị tài liệu đào tạo theo từng vai trò.
- Đào tạo FO, Reservation, F&B, Cashier, CRM/Admin và Manager.
- Tổ chức kiểm tra readiness trước go-live.
- Ghi nhận câu hỏi, lỗi hiểu sai, điểm nghẽn trong quá trình training.

Deliverables:

- Training deck.
- Role-based user guide.
- Training attendance record.
- Staff readiness checklist.
- Internal FAQ.

## 5. Phạm Vi Công Việc Chi Tiết

## 5.1 Project Governance

Công việc:

- Xác định sponsor, owner và nhóm triển khai.
- Lập timeline triển khai.
- Xác định milestone: kickoff, rule sign-off, configuration review, UAT, training, go-live, hypercare.
- Thiết lập cơ chế họp định kỳ.
- Quản lý action list, risk log, issue log và decision log.
- Theo dõi tiến độ vendor CRM/loyalty.
- Điều phối escalation khi có blocker.

Deliverables:

- Project plan.
- RACI matrix.
- Meeting cadence.
- Weekly status report.
- Risk/issue/action/decision log.

## 5.2 Loyalty Business Rules & Scenario Design

Công việc:

- Làm rõ nhóm khách được tham gia loyalty:
  - Khách lưu trú trực tiếp.
  - Khách OTA.
  - Khách corporate.
  - Khách walk-in nhà hàng.
  - Khách local dining.
  - Khách VIP/Owner/Partner nếu có.
- Làm rõ rule tích điểm:
  - Room revenue.
  - F&B spend.
  - Spa hoặc dịch vụ phụ trợ nếu có.
  - Thuế, service charge, minibar, banquet, corporate rate.
- Làm rõ rule đổi điểm:
  - Voucher F&B.
  - Discount.
  - Room upgrade.
  - Late checkout.
  - Breakfast.
  - Amenities.
- Làm rõ tier:
  - Điều kiện lên hạng.
  - Điều kiện giữ hạng.
  - Downgrade.
  - Expiry.
- Làm rõ exception:
  - Khách quên báo member.
  - Thiếu điểm sau check-out.
  - Bill POS không sync.
  - Sai số điện thoại.
  - Duplicate profile.
  - Voucher hết hạn.
  - Khách tranh chấp quyền lợi.

Deliverables:

- Loyalty business rules document.
- Tier & benefit matrix.
- Earn/burn scenario book.
- Exception handling matrix.
- FAQ cho vận hành.

## 5.3 Vendor CRM/Loyalty Coordination

Công việc:

- Gửi requirement, rule và scenario cho vendor.
- Tổ chức walkthrough để vendor hiểu logic khách sạn.
- Review cấu hình do vendor demo.
- Theo dõi bug, defect và change request.
- Điều phối với vendor PMS/POS nếu cần tích hợp hoặc đối soát dữ liệu.
- Đảm bảo vendor bàn giao đúng các rule đã sign-off.
- Phân loại lỗi: business rule gap, configuration issue, integration issue, data issue, training issue.

Deliverables:

- Vendor requirement tracker.
- Configuration review notes.
- Bug/defect log.
- Change request log.
- Vendor sign-off checklist.

## 5.4 FO/F&B Operational SOP

### FO SOP

Cần bao phủ:

- Đăng ký member mới.
- Tra cứu member bằng số điện thoại, email hoặc member ID.
- Gắn member vào booking/stay.
- Xác nhận tier và benefit khi check-in.
- Xử lý upgrade, early check-in, late check-out, welcome amenity.
- Giới thiệu loyalty cho khách chưa là member.
- Ghi nhận khách OTA có/không được tích điểm.
- Xử lý missing point.
- Xử lý duplicate profile.
- Xử lý khi khách khiếu nại quyền lợi.

### Reservation SOP

Cần bao phủ:

- Nhận diện member khi đặt phòng qua phone, email, website hoặc direct channel.
- Ghi nhận member ID vào booking.
- Tư vấn benefit khi khách đặt trực tiếp.
- Escalate booking có benefit đặc biệt.
- Ghi chú loyalty request cho FO trước arrival.

### F&B SOP

Cần bao phủ:

- Tra cứu member trước khi thanh toán.
- Áp dụng discount hoặc voucher.
- Ghi nhận điểm F&B.
- Xử lý khách nhà hàng không lưu trú.
- Xử lý bill room charge.
- Xử lý split bill.
- Xử lý khách báo member sau khi bill đã đóng.
- Xử lý voucher đã dùng, hết hạn hoặc không hợp lệ.

### Cashier SOP

Cần bao phủ:

- Kiểm tra member trước khi finalize bill.
- Đối chiếu discount/voucher trên POS.
- Xử lý void/refund liên quan đến điểm hoặc voucher.
- Ghi nhận lỗi khi POS không sync.
- Escalate bill có tranh chấp.

Deliverables:

- FO SOP.
- Reservation SOP.
- F&B SOP.
- Cashier SOP.
- Quick reference sheet cho từng bộ phận.
- Guest-facing script.
- Internal escalation flow.

## 5.5 UAT & Go-Live Readiness

Công việc:

- Viết test case theo tình huống vận hành thật.
- Tổ chức UAT với FO, Reservation, F&B, Cashier và CRM/Admin.
- Ghi nhận kết quả pass/fail.
- Phân loại lỗi theo mức độ nghiêm trọng.
- Làm việc với vendor để xử lý defect.
- Kiểm tra go-live readiness trước ngày launch.

Test case mẫu:

- Khách mới đăng ký tại FO.
- Khách member check-in.
- Khách member được áp dụng tier benefit.
- Khách OTA có/không được tích điểm.
- Khách nhà hàng không lưu trú muốn tích điểm.
- Khách đổi voucher tại nhà hàng.
- Bill POS sync lỗi.
- Staff nhập sai số điện thoại.
- Khách báo thiếu điểm sau check-out.
- Duplicate guest profile.
- Voucher hết hạn.
- Member upgrade/downgrade tier.

Deliverables:

- UAT script.
- UAT result report.
- Defect tracker.
- Go-live checklist.
- Go/no-go recommendation.

## 5.6 Training & Change Management

Công việc:

- Chuẩn bị tài liệu đào tạo theo vai trò.
- Tổ chức training cho từng nhóm:
  - FO Manager.
  - Receptionist.
  - Reservation.
  - F&B Manager.
  - Restaurant host/server.
  - Cashier.
  - CRM/Admin.
  - GM/Manager.
- Tổ chức role-play theo case thực tế.
- Ghi nhận câu hỏi và cập nhật FAQ.
- Đánh giá readiness trước go-live.

Deliverables:

- Training deck.
- Role-based user guide.
- Internal FAQ.
- Attendance record.
- Staff readiness checklist.

## 5.7 Go-Live & Hypercare

Công việc:

- Hỗ trợ launch theo mô hình onsite hoặc remote đã thống nhất.
- Theo dõi issue phát sinh trong ngày go-live.
- Làm đầu mối điều phối xử lý nhanh với vendor.
- Tổng hợp issue theo severity.
- Cập nhật SOP hoặc FAQ nếu phát sinh case mới.
- Báo cáo sau go-live.
- Đề xuất tối ưu sau giai đoạn hypercare.

Deliverables:

- Go-live support log.
- Daily hypercare report.
- Issue resolution tracker.
- Post-launch review.
- Optimization recommendations.

## 6. KPI Triển Khai Nên Cam Kết

Không nên cam kết doanh thu trực tiếp nếu dịch vụ không kiểm soát marketing, pricing, hệ thống và ngân sách bán hàng. Nên cam kết các KPI triển khai và readiness.

KPI đề xuất:

- 100% business rules được document và sign-off.
- 100% critical scenarios được đưa vào UAT.
- 100% nhóm FO, Reservation, F&B, Cashier, CRM/Admin được training trước go-live.
- Go-live checklist hoàn tất trước ngày launch.
- Critical defect được phân loại và có owner xử lý.
- SOP được bàn giao theo từng bộ phận.
- Vendor delivery được review theo checklist.
- Hypercare report được gửi theo lịch đã thống nhất.
- Issue log được cập nhật và phân loại đầy đủ trong giai đoạn hypercare.

## 7. Acceptance Criteria

Dự án được xem là hoàn tất khi:

- Loyalty rules đã được khách sạn sign-off.
- Vendor configuration đã được review dựa trên rule và scenario đã thống nhất.
- UAT hoàn tất với tỷ lệ pass theo ngưỡng nghiệm thu.
- Critical defects không còn mở, hoặc có workaround được khách sạn chấp nhận.
- FO, Reservation, F&B, Cashier và CRM/Admin đã được training.
- SOP và quick reference sheet đã được bàn giao.
- Go-live checklist đã được Project Sponsor hoặc người được ủy quyền xác nhận.
- Hypercare period hoàn tất và post-launch review đã được bàn giao.

## 8. Trách Nhiệm Của Khách Sạn

Khách sạn cần:

- Chỉ định Project Sponsor và Project Owner.
- Cử đại diện các bộ phận FO, Reservation, F&B, Cashier, Sales/Marketing, IT tham gia đúng lịch.
- Cung cấp chính sách kinh doanh, loyalty concept, benefit mong muốn và các quyết định cần thiết.
- Làm việc với vendor hiện tại để cung cấp quyền truy cập, demo, tài liệu hoặc dữ liệu cần thiết.
- Phê duyệt rule, SOP, UAT và go-live theo timeline.
- Đảm bảo nhân viên tham gia training đầy đủ.
- Chịu trách nhiệm với quyết định kinh doanh cuối cùng về reward, discount, tier và exception policy.

## 9. Trách Nhiệm Của Vendor CRM/Loyalty

Vendor CRM/loyalty cần:

- Tư vấn khả năng cấu hình trên hệ thống.
- Cấu hình rule, tier, point, voucher, campaign theo requirement đã sign-off.
- Cung cấp demo và hướng dẫn admin nếu thuộc phạm vi vendor.
- Xử lý bug, defect hoặc configuration issue.
- Hỗ trợ UAT và go-live trong phạm vi hợp đồng vendor.
- Cung cấp tài liệu kỹ thuật hoặc API/file specification nếu có tích hợp.

## 10. Assumptions & Dependencies

- Khách sạn đã chọn hoặc đang làm việc với một vendor CRM/loyalty.
- Vendor CRM/loyalty có năng lực cấu hình các rule loyalty đã thống nhất, hoặc sẽ xác nhận giới hạn hệ thống trước khi sign-off.
- Nếu cần tích hợp PMS/POS, vendor liên quan phải cung cấp API, file export/import hoặc phương án vận hành thay thế.
- Dữ liệu khách hàng hiện tại có thể cần cleansing trước khi import.
- Các quyết định về chính sách loyalty phải được khách sạn phê duyệt đúng hạn.
- Go-live phụ thuộc vào readiness của vendor, dữ liệu, SOP và training.

## 11. Out Of Scope

- Phát triển phần mềm, API, middleware hoặc mobile app.
- Mua license phần mềm.
- Đàm phán hợp đồng thương mại với vendor.
- Thiết kế brand identity hoặc creative campaign cho loyalty.
- Vận hành campaign CRM dài hạn sau hypercare.
- Chịu trách nhiệm doanh thu, repeat rate hoặc member revenue sau go-live nếu không có scope vận hành tăng trưởng riêng.
- Chỉnh sửa hệ thống PMS/POS/CRM ngoài quyền hạn hoặc phạm vi vendor.
- Nhập liệu thủ công dữ liệu khách hàng cũ ở quy mô lớn nếu không có phụ lục riêng.

## 12. Timeline Mẫu

Timeline thực tế phụ thuộc độ phức tạp hệ thống và vendor.

| Giai đoạn | Thời lượng tham khảo | Kết quả chính |
| --- | ---: | --- |
| Kickoff & Discovery | 1 tuần | Project plan, stakeholder map, current-state notes |
| Rule & Scenario Design | 1-2 tuần | Loyalty rulebook, scenario book, exception matrix |
| Vendor Configuration Coordination | 2-4 tuần | Requirement tracker, configuration review, issue log |
| SOP & Training Material | 1-2 tuần | FO/F&B/Cashier SOP, training deck |
| UAT | 1-2 tuần | UAT script, defect log, UAT report |
| Go-Live | 1 tuần | Go-live checklist, launch support |
| Hypercare | 1-4 tuần | Issue tracker, daily/weekly report, post-launch review |

## 13. Pricing Unit Gợi Ý

Có thể đóng gói thương mại theo một trong các cách:

- Fixed fee theo dự án.
- Monthly retainer trong thời gian triển khai.
- Day-rate cho Implementation PM / BA / Trainer.
- Package theo số outlet, số property hoặc số hệ thống cần phối hợp.
- Hypercare add-on sau go-live.

Gợi ý phân tầng:

| Gói | Phù hợp với | Phạm vi |
| --- | --- | --- |
| Basic | 1 khách sạn, ít tích hợp | Rule, SOP, vendor coordination, UAT, training |
| Standard | Khách sạn + nhà hàng | Thêm F&B SOP, cashier flow, go-live support |
| Advanced | Multi-outlet hoặc có PMS/POS integration | Thêm integration coordination, expanded UAT, hypercare dài hơn |

## 14. Câu Mô Tả Bán Hàng Ngắn

Chúng tôi cung cấp đội triển khai vận hành loyalty cho khách sạn và nhà hàng, làm đầu mối giữa business, FO/F&B và vendor CRM/loyalty. Phạm vi bao gồm chuẩn hóa rule, viết kịch bản vận hành, điều phối vendor, UAT, training, go-live và hypercare để chương trình loyalty không chỉ được cấu hình trên hệ thống mà còn chạy được trong vận hành thực tế.
