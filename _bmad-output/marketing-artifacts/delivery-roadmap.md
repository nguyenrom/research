# Delivery Roadmap — Marketing Rollout cho Khách

**Người deliver:** Rom (solo)
**Thời lượng MVP:** 6 tuần (W1–W6) → ads Meta + Google go-live
**Mở rộng:** W7–W10 → TikTok + LinkedIn
**Mục tiêu marketing:** Always-on ads + tăng tương tác social (KHÔNG phải campaign launch lớn)
**Deliverables chính:** Website rebuild + 4 kênh ads/social vận hành ổn định
**Ngày tạo:** 2026-05-12

---

## 1. Reality Check & Nguyên Tắc Phasing

| Vấn đề | Quyết định |
|---|---|
| Solo + 4 ads platforms + website rebuild trong 6 tuần | Chia 2 wave: **Wave 1 (W1–W6)** Meta + Google. **Wave 2 (W7–W10)** TikTok + LinkedIn |
| Khách chưa cung cấp info → không thể bắt đầu strategy | W1 dành 100% cho Discovery; mọi deliverable sau đều phụ thuộc gate này |
| Website rebuild block ads (cần landing page + tracking) | Website MVP go-live W4 (không phải full features) → ads chạy được W5 |
| "Không chạy campaign lớn" → always-on mode | Không cần J-14 launch sequence; thay bằng **soft launch + optimize loop** |
| Solo không có designer/dev/copy | Dùng template (Webflow/Framer/WordPress + Elementor), AI cho copy/creative draft, khách approve |

---

## 2. Timeline Tổng Quan (6 tuần MVP)

```
Tuần │ W1        W2        W3        W4        W5        W6
─────┼─────────────────────────────────────────────────────────
DISC │ ████████  ░░
BRAND│           ███████
WEB  │           ████████  ████████  ████████  ░░  (live W4 cuối)
TRACK│                     ████████  ████████
CRTV │                     ████      ████████  ░░
ADS  │                                         ████████  ████████ (live W5)
SOC  │                               ████      ████████  ████████ (organic)
OPT  │                                                   ████████
```

**Milestone gates:**
- 🚪 **G1 (cuối W1):** Discovery hoàn tất → khách approve brief
- 🚪 **G2 (cuối W2):** Positioning + messaging → khách approve
- 🚪 **G3 (giữa W3):** Website wireframe + sitemap → khách approve
- 🚪 **G4 (cuối W4):** Website MVP live + tracking → khách review
- 🚪 **G5 (giữa W5):** Creative bộ đầu + ads setup → khách approve creative
- 🚪 **G6 (cuối W6):** Ads chạy ổn định, có data đầu tiên → review tuần với khách

---

## 3. Chi Tiết Tuần-Theo-Tuần

### **Tuần 1 — Discovery & Audit** (Bạn ↔ Khách: 80% touchpoint)

**Mục tiêu:** Hiểu business + thu thập tất cả thông tin cần thiết để không phải hỏi lại.

**Việc của bạn (Rom):**
- Gửi **Discovery Questionnaire** trước buổi gặp (form/Google Doc) — gồm: business model, ICP, sản phẩm/dịch vụ, USP, đối thủ, budget, mục tiêu định lượng, brand assets hiện có
- Tổ chức **Kickoff call (90 phút)**: deep-dive interview về sản phẩm, customer, pain points, success criteria
- Audit hiện trạng: website cũ (nếu có), GA/GSC data, Facebook/IG/TikTok page hiện tại, Google Business Profile, danh sách email
- Map competitor (3–5 đối thủ chính): channel mix, ad creative, positioning
- Viết `marketing-context.md` — nguồn duy nhất tất cả phase sau dùng

**Việc của khách (cần ép cứng):**
- ✅ Trả Discovery Questionnaire trước W1 ngày 3
- ✅ Tham gia Kickoff call (đủ decision maker)
- ✅ Cấp truy cập: GA4, Search Console, Facebook Business Manager, Google Ads (nếu có), domain registrar, hosting
- ✅ Cung cấp brand assets: logo (vector), font, màu, hình ảnh sản phẩm gốc, video clip (nếu có)
- ✅ Danh sách 3–5 đối thủ + 5–10 khách hàng cũ tiêu biểu để tham khảo

**Deliverable cuối W1:**
- `marketing-context.md` (positioning baseline)
- `current-state-audit.md`
- `competitor-snapshot.md`

**🚪 Gate G1:** Khách ký approve Discovery Brief trước khi sang W2.

**Risk W1:** Khách trả info chậm → toàn bộ timeline trượt. **Mitigation:** Hợp đồng/SOW có điều khoản: nếu khách trễ info >3 ngày, deadline ads delay tương ứng.

---

### **Tuần 2 — Positioning, Messaging & Website Wireframe**

**Mục tiêu:** Chốt "nói gì" trước khi build "nói ở đâu".

**Việc của bạn:**
- Viết **Positioning Statement** (1 câu) + 3 messaging pillars + brand voice guide ngắn (1 trang)
- Vẽ **website sitemap** (5–8 page: Home, Service/Product, About, Case studies, Blog, Contact, Pricing nếu có, Landing page riêng cho ads)
- Wireframe low-fi cho Home + Landing page chính (Figma/Whimsical)
- Bắt đầu chọn template website (Webflow/Framer hoặc WordPress + theme)
- Draft copy cho Home + Landing page (dùng AI làm draft, Rom edit)

**Việc của khách:**
- ✅ **Messaging review meeting (60 phút)** giữa W2 — feedback positioning + voice
- ✅ **Wireframe review (45 phút)** cuối W2 — chốt sitemap + structure
- ✅ Cung cấp 3–5 case study/testimonial (text + ảnh nếu có)

**Deliverable cuối W2:**
- `positioning-strategy.md`
- `website-sitemap.md` + Figma wireframe link
- Copy draft Home + Landing v1

**🚪 Gate G2 + G3:** Khách approve messaging + sitemap. Không qua gate → KHÔNG build website.

---

### **Tuần 3 — Website Build (chính) + Tracking Setup**

**Mục tiêu:** 70% website xong, tracking infra ready.

**Việc của bạn:**
- Build Home + Landing page + About + Contact (4 page core trước)
- Setup **GA4** + **Google Tag Manager** + conversion events (form submit, click CTA, scroll depth)
- Setup **Meta Pixel** + Conversion API (server-side event quan trọng)
- Tạo **Google Ads account** (nếu chưa có) + link với GA4
- Setup **Google Business Profile** (nếu local business)
- Bắt đầu draft creative cho ads (5–10 concept ad copy + 5 visual concept)

**Việc của khách:**
- ✅ Approve copy Home + Landing (giữa W3)
- ✅ Cung cấp ảnh sản phẩm/dịch vụ chất lượng cao (hoặc duyệt ngân sách thuê chụp ngoài)
- ✅ Approve domain DNS change (chuyển sang hosting mới)

**Deliverable cuối W3:**
- Website 4 page core ở staging URL
- Tracking plan (`tracking-spec.md`) — list mọi event, parameter, conversion
- Creative concept board v1

**Risk W3:** Khách không có ảnh chất lượng → ad creative yếu. **Mitigation:** Ngân sách chụp ảnh nhanh ($200–500) hoặc dùng stock + Canva/AI generate.

---

### **Tuần 4 — Website Finish + Creative Production + Ads Pre-Launch**

**Mục tiêu:** Website live + 1 bộ ad creative ready.

**Việc của bạn:**
- Hoàn thiện Service/Pricing/Blog page
- QA website: speed (PageSpeed >80 mobile), responsive, form, tracking fire đúng
- **Go-live website** giữa W4 (DNS switch, SSL, sitemap submit GSC)
- Sản xuất creative bộ 1: **5 ad cho Meta** (3 image + 2 short video 15s) + **3 ad copy Google Search** (RSA)
- Setup ads campaign structure ở Meta + Google (campaigns + ad sets + ads, chưa publish)
- Audience research: 3–5 audience cho Meta (lookalike, interest, retargeting), keyword list cho Google Search

**Việc của khách:**
- ✅ Final website review (UAT) trước khi DNS switch
- ✅ **Approve creative bộ 1** (cuối W4) — gồm visual + copy + audience
- ✅ Confirm budget mensual cho ads (Meta + Google) — chốt số cụ thể

**Deliverable cuối W4:**
- Website **LIVE** ✅
- Ads campaigns built (chưa publish), pending approval
- `creative-batch-1.md` + assets folder

**🚪 Gate G4 + G5:** Website live + creative approved → publish ads.

---

### **Tuần 5 — Soft Launch Ads + Bắt Đầu Social Organic**

**Mục tiêu:** Ads chạy thật, social bắt đầu post organic.

**Việc của bạn:**
- **Publish Meta Ads** (đầu W5) — bắt đầu với budget thấp ($20–50/ngày) để học, không scale ngay
- **Publish Google Ads Search** — Brand keyword + 1 campaign non-brand priority
- Setup **organic posting calendar** Facebook + Instagram (3 post/tuần) — content tái sử dụng từ creative ads + behind-the-scene
- Setup **TikTok organic** (chưa ads) — 2–3 video/tuần để warm-up account, học content gì work
- Daily monitor: ads delivery, CTR, CPC, conversion (chỉ check, chưa optimize gấp — cần ≥7 ngày data)
- Setup **báo cáo tuần** (Looker Studio dashboard hoặc Google Sheet)

**Việc của khách:**
- ✅ **Daily check-in 15 phút** đầu tuần (nếu có thay đổi gấp)
- ✅ Cung cấp content/photo cho organic post (hoặc approve plan content do Rom đề xuất)
- ✅ Trả lời comment/inbox trên page (hoặc giao Rom làm community management — phải chốt scope)

**Deliverable cuối W5:**
- Ads chạy ổn định, có ≥3–5 ngày data
- Dashboard tracking live
- Content calendar 2 tuần tới (post organic)

**Risk W5:** Ads bị Meta/Google reject → delay 1–2 ngày. **Mitigation:** Submit early W5, có buffer.

---

### **Tuần 6 — Optimize Loop + Handover Operations**

**Mục tiêu:** Ads vào nhịp tối ưu hàng tuần, khách hiểu cách đọc số.

**Việc của bạn:**
- **Tuần optimize**: pause ad/audience CPA cao, scale ad performer (chỉ scale 20–30%/lần)
- A/B test creative bộ 2 (2 visual mới vs winner W5)
- Refine keyword Google Ads (negative keyword từ search term report)
- Tổ chức **Monthly Review meeting (60 phút)** với khách: kết quả 2 tuần đầu, learning, kế hoạch tháng tới
- Soạn **Operating Playbook** cho khách: ai làm gì hàng tuần, dashboard ở đâu, KPI nào quan trọng
- Quyết định Wave 2: TikTok ads + LinkedIn ads → bắt đầu W7 hay delay

**Việc của khách:**
- ✅ Tham gia Monthly Review
- ✅ Quyết định: tăng/giữ/giảm budget tháng tới
- ✅ Approve scope Wave 2 (TikTok + LinkedIn)

**Deliverable cuối W6:**
- `month-1-report.md` (KPI, learning, next actions)
- `operating-playbook.md` (cadence vận hành)
- Quyết định Wave 2 go/no-go

**🚪 Gate G6:** Khách approve performance + roadmap Wave 2.

---

## 4. Wave 2 — Mở Rộng TikTok + LinkedIn (W7–W10, optional)

| Tuần | Việc chính |
|---|---|
| **W7** | TikTok Ads account + Pixel; sản xuất 5 video TikTok-native (vertical, hook 1s, CTA cuối) |
| **W8** | TikTok Ads soft launch ($30–50/ngày, Spark Ads dùng organic post performer); LinkedIn page audit + tối ưu |
| **W9** | LinkedIn Ads setup (Sponsored Content + Lead Gen Form); creative LinkedIn (B2B tone, không reuse Meta) |
| **W10** | LinkedIn Ads soft launch; review toàn bộ 4 kênh, rebalance budget theo CPA |

**Lưu ý:** Wave 2 chỉ làm nếu Wave 1 (Meta + Google) đã có **CPA biết được + dòng tiền dương**. Nếu Meta/Google chưa profitable → ưu tiên fix trước, không scale rộng.

---

## 5. Bảng Phối Hợp Khách (Touchpoints)

| Tuần | Touchpoint | Thời lượng | Format | Ai cần có mặt |
|---|---|---|---|---|
| W0 | Gửi Discovery Questionnaire | — | Email + Google Doc | Decision maker |
| W1 | **Kickoff Call** | 90' | Video call | Decision maker + ai có domain knowledge |
| W1 | Cấp truy cập tools | — | Async (email/Loom hướng dẫn) | Người quản trị tài khoản |
| W2 | **Messaging Review** | 60' | Video call | Decision maker + marketing lead |
| W2 | **Wireframe Review** | 45' | Video call (share Figma) | Decision maker |
| W3 | Copy approval | — | Async (Google Doc comment) | Decision maker |
| W4 | **Website UAT** | 60' | Video call (share staging) | Decision maker + ≥1 user thử |
| W4 | **Creative Approval** | 45' | Video call (share creative board) | Decision maker |
| W5 | Daily check-in (nếu cần) | 15' | Slack/Zalo/text | Khách rep |
| W6 | **Monthly Review** | 60' | Video call | Decision maker |
| W7+ | Weekly sync | 30' | Video call | Khách rep |

**Tổng touchpoint sync:** ~7 buổi meeting trong 6 tuần.

---

## 6. Risks & Dependencies (cần điều khoản trong SOW)

| Risk | Khả năng | Impact | Mitigation |
|---|---|---|---|
| Khách trễ feedback/approve | Cao | Trượt deadline | SOW: "Mỗi ngày khách trễ approve = ads delay 1 ngày" |
| Khách không có brand asset | Trung bình | Ad creative yếu | Quote thêm phí chụp/design ($200–800) |
| Domain/hosting issue (DNS, SSL) | Trung bình | Website delay 1–3 ngày | Bắt đầu DNS prep từ W3, có rollback plan |
| Meta/Google ads bị reject | Trung bình | Delay 1–2 ngày | Submit ads từ chiều thứ 6 W4 để có buffer |
| Khách muốn add scope giữa chừng (vd: SEO, email) | Cao | Trượt timeline | SOW: change request → quote riêng, không nhét vào timeline gốc |
| Solo Rom ốm/bận | Trung bình | Slip 1 tuần | Buffer 1 tuần ở W6 (đã tính) — nếu trễ thì Wave 2 lùi |
| Website performance kém (page speed) | Trung bình | Ads CPA cao | W4 dành buổi cuối QA speed, KHÔNG cho live nếu mobile <70 |

---

## 7. Operating Cadence (sau W6 — vận hành dài hạn)

| Cadence | Việc | Time/tuần |
|---|---|---|
| Hàng ngày | Check ads delivery, pause ad lỗi, trả comment urgent | 30' |
| 2x/tuần | Post organic Facebook + Instagram | 1h |
| 3x/tuần | Post organic TikTok | 2h (có sản xuất video) |
| Hàng tuần | Optimize ads (creative test, audience, bid), báo cáo tuần | 3h |
| Hàng tháng | Monthly review với khách, plan tháng tới, refresh creative bộ mới | 4h |

**Tổng effort post-W6 cho 1 khách:** ~12–15h/tuần solo (vừa đủ cho 1–2 khách parallel).

---

## 8. KPI Framework (chốt với khách W1–W2)

**North Star (chọn 1 với khách):**
- Số leads/tháng (B2B/service)
- Doanh thu attributed từ ads (e-commerce)
- Số booking/contact (local business)

**Leading indicators (track tuần):**
- Meta: CTR, CPC, CPA, ROAS, frequency
- Google: CTR, CPC, Quality Score, conversion rate
- Social organic: reach, engagement rate, follower growth, save/share
- Website: sessions, conversion rate, bounce rate, page speed

**Reporting:**
- **Tuần:** dashboard tự động (Looker Studio) — khách tự xem
- **Tháng:** report PDF + meeting 60'

---

## 9. Checklist "Sẵn Sàng Bắt Đầu W1"

Trước khi ký kick-off, đảm bảo:

- [ ] SOW ký, có điều khoản về timeline + responsibility khách
- [ ] Discovery Questionnaire đã gửi khách
- [ ] Lịch Kickoff Call confirmed (decision maker xác nhận có mặt)
- [ ] Khách hiểu họ phải làm gì + khi nào (đã gửi bản tóm tắt 1 trang)
- [ ] Tool stack chuẩn bị: Notion/Slack workspace cho khách, Figma, GA4, GTM, Webflow/WP, Looker Studio template

---

## 10. Tóm Tắt 1 Câu

> **6 tuần W1–W6 = Discovery → Website MVP → Meta + Google Ads live + social organic.** Sau W6, vận hành always-on + scale TikTok + LinkedIn ở W7–W10 nếu Wave 1 đạt KPI.
