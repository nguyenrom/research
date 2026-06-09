# Project Context — Databricks-P1

> File này là **single source of truth** cho mọi thông tin dự án Databricks-P1.
> Cập nhật ở đây mỗi khi có thay đổi → sau đó sync vào `_generate_docs.py` (các CONSTANT ở đầu file) → regenerate 4 file Word.
> Mọi câu hỏi của Claude trong các phiên sau sẽ tham chiếu file này trước.

**Last updated**: 2026-05-13
**Maintained by**: Nguyen Le (Blue Coral CEO/PO)
**Language preference**: Vietnamese
**Response style**: Ngắn gọn, đi thẳng vấn đề. Không liệt kê dài dòng trừ khi cần.

---

## 0. Operational Playbook (cho Claude — đọc trước khi xử lý request)

> Section này giúp Claude xử lý request nhanh hơn ở các phiên sau.

### 0.1 Workflow chuẩn cho mọi thay đổi

```
1. Đọc PROJECT_CONTEXT.md để hiểu state hiện tại
2. Edit _generate_docs.py (constants ở đầu hoặc nội dung function)
3. Edit PROJECT_CONTEXT.md (sync state mới + thêm vào Decision Log + Change Log)
4. Chạy: source .venv-docx/bin/activate && python3 docs/databricks-pm/_generate_docs.py
5. Báo cáo ngắn: file nào thay đổi, đổi gì, có cần user confirm gì không
```

### 0.2 Pattern thường gặp & cách xử lý

| User nói | Cần edit | Files |
|---|---|---|
| "Thêm/đổi tên người X làm Y" | Constants block + Snapshot table + Stakeholder Matrix + Permission Matrix nếu áp dụng | `_generate_docs.py` + `PROJECT_CONTEXT.md` Section 3 |
| "Đổi timeline / milestone" | Constants dates + Charter Section 6 Timeline | `_generate_docs.py` + `PROJECT_CONTEXT.md` Section 4 |
| "Thêm/sửa folder SharePoint" | Doc 03 Section 2/3/4/7 + path references trong doc 02/04 | `_generate_docs.py` + `PROJECT_CONTEXT.md` Section 6.1 |
| "Đổi footer / owner" | `add_footer_note()` default + các call site (replace_all) | `_generate_docs.py` |
| "Cập nhật scope WS" | Charter Section 4 In-Scope + Charter Section 3 Objectives | `_generate_docs.py` |
| "Đổi cadence meeting" | Working Agreement Section 4 + Comm Plan Section 3/4 | `_generate_docs.py` |

### 0.3 Constants block location

`_generate_docs.py` lines **13–40** chứa tất cả tham số có thể đổi (tên 2 bên, project code, dates, cloud, người). Đổi ở đây trước, regenerate, KHÔNG sửa từng nơi trong function nếu có constant.

### 0.4 User communication preferences (đã quan sát qua các phiên)

- Vietnamese → respond Vietnamese
- Confirm ngắn ("Y", "OK", "skip") → đừng hỏi lại
- "Cập nhật giúp tôi" = làm luôn, không cần plan dài
- "Ngắn gọn" / "diễn giải ngắn" → giới hạn 4–6 bullet, không có table giải thích dài dòng
- Khi assume thông tin (vd: phía nào của person) → ghi rõ "tôi đang assume X — confirm hoặc đổi"
- Batch update tốt hơn round trip: gather hết info → update 1 lần → regenerate 1 lần

### 0.5 Anti-patterns (đã thử và không nên lặp)

- ❌ Sửa từng nơi trong function khi có constant tương ứng → dùng constant
- ❌ Regenerate sau MỖI edit → đợi gom đủ rồi regenerate 1 lần
- ❌ Quên sync `PROJECT_CONTEXT.md` sau khi đổi script → mất single source of truth
- ❌ Hỏi user về thứ có thể đoán từ file context (vd: tên người đã biết)
- ❌ Trả lời dài với table so sánh khi user xin "diễn giải ngắn"

---

## 1. Project Identity

| Field | Value |
|---|---|
| Project Code | `Databricks-P1` |
| Project Full Name | VinaCapital Core Data Platform — Phase 1 (Assessment + Foundation + PoC) |
| Phase | 1 of N (multi-phase data modernization program) |
| Cloud Platform | Azure |
| Tenant | Tenant VinaCapital |
| Working Mode | Hybrid (onsite VinaCapital office + remote) |
| Engagement Model | _TBD_ |
| Budget Ceiling | _TBD / sensitive_ |

---

## 2. Parties

| Party | Name | Short | Role |
|---|---|---|---|
| Vendor | Blue Coral | BC | Implementation partner |
| Customer | VinaCapital | VC | Asset / fund management group (financial services) |

---

## 3. Key People

### 3.1 VinaCapital (VC)

| Role | Name | Notes |
|---|---|---|
| Project Owner | **Khiem Pham** | Sponsor + final approver phía VC |
| Tech Lead | **Hien Vo** | Architecture & technical decision phía VC |
| SME — PMS | _TBD_ | Nominate at Kickoff |
| SME — MarketS | _TBD_ | Nominate at Kickoff |
| SME — MIO | _TBD_ | |
| SME — Salesforce | _TBD_ | |
| SME — Distributor | _TBD_ | |
| SME — Custodian | _TBD_ | |
| SME — Excel reports | _TBD_ | |
| SME — VSDC | _TBD_ | |
| SME — ESM | _TBD_ | |
| SME — Datahub | _TBD_ | |
| Security / Compliance | _TBD_ | |
| IT Infra (for access) | _TBD_ | Critical for Entra B2B onboarding |

### 3.2 Blue Coral (BC)

| Role | Name | Notes |
|---|---|---|
| CEO / Project Owner | **Nguyen Le** | Also document preparer; **footer owner of all PM artifacts** |
| Project Manager | **Tin Huynh** | Day-to-day delivery |
| Tech Lead / Architect | **Dung Phan** | Solution design + WS3 leadership |
| Finance BA | **Tess Pham** | Business analysis Finance domain — workshop với VC Finance SME cho PMS, ESM, Custodian, VSDC |
| WS1 Lead | _TBD_ | Assessment PMS & MarketS |
| WS2 Lead | _TBD_ | Assessment 8 source systems |
| Data Engineer(s) | _TBD_ | Allocation TBD |
| DevOps Engineer | _TBD_ | Allocation TBD |

---

## 4. Timeline

| Date | Event | Notes |
|---|---|---|
| 18/05/2026 (T2) | **Project Start** — work begins, 3 WS song song | |
| 19/05/2026 (T3) | **Kickoff Meeting** (formal) | |
| 09/07/2026 (T5) | **Target Sign-off** | |
| 10/07/2026 (T6) | Project end (buffer) | |

### 4.1 Workstream timing (parallel from 18/05)

| WS | Tên | Bắt đầu | Kết thúc |
|---|---|---|---|
| WS1 | Landscape Assessment: PMS System & MarketS | 18/05/2026 | 12/06/2026 |
| WS2 | Landscape Assessment: 8 source systems + Consolidate | 18/05/2026 | 26/06/2026 (+ Consolidate 29/06–03/07) |
| WS3 | Design & Setup Core Data Platform + PoC + Demo | 18/05/2026 | 03/07/2026 |
| WS3.1 | — Design | 18/05/2026 | 08/06/2026 |
| WS3.2 | — Setup | 01/06/2026 | 15/06/2026 |
| WS3.3 | — PoC Implementation | 08/06/2026 | 29/06/2026 |
| WS3.4 | — Demo PoC | 29/06/2026 | 03/07/2026 |
| WS4 | Closure Meeting | 06/07/2026 | 10/07/2026 (target 09/07) |

### 4.2 Milestones

| ID | Milestone | Date | Workstream |
|---|---|---|---|
| M0 | Project Start | 18/05/2026 | Tất cả |
| M0.1 | Kickoff Meeting | 19/05/2026 | Tất cả |
| M1 | WS1 Complete (PMS+MarketS assessment) | 12/06/2026 | WS1 |
| M2 | WS3 Design Done | 08/06/2026 | WS3 |
| M3 | WS3 Setup Done (workspace ready) | 15/06/2026 | WS3 |
| M4 | WS3 PoC Implementation Done | 29/06/2026 | WS3 |
| M5 | WS2 Assessment Done (8 systems) | 26/06/2026 | WS2 |
| M6 | Consolidate Roadmap + PoC Demo | 03/07/2026 | WS2 + WS3 |
| M7 | Closure Sign-off | 09/07/2026 (buffer 10/07) | WS4 |

---

## 5. Scope

### 5.1 In-Scope

**WS1 — Landscape Assessment: PMS System & MarketS**
- Khảo sát hiện trạng PMS và các MarketS
- Phỏng vấn người dùng, thu thập tài liệu, phân tích luồng dữ liệu
- Xây dựng roadmap tích hợp

**WS2 — Landscape Assessment: 8 Source Systems**
1. MIO
2. Salesforce
3. Distributor
4. Custodian
5. Excel (reports / spreadsheets)
6. Depository (VSDC — Vietnam Securities Depository)
7. ESM
8. Datahub

Plus: Consolidate findings WS1 + WS2 → final integrated roadmap.

**WS3 — Design & Setup Core Data Platform**
- Solution architecture (Lakehouse medallion)
- Security design (IAM, network, encryption, Unity Catalog policy)
- Setup Workspace, Unity Catalog, CI/CD baseline trên Azure Databricks
- PoC implementation
- Demo framework cho VC

**WS4 — Closure**
- Closure meeting
- Nghiệm thu deliverable
- Ký biên bản kết thúc Phase 1

### 5.2 Out-of-Scope (Phase 1)

- Ingest production data từ source systems (→ Phase 2)
- Pipeline ETL/ELT production cho từng hệ thống (→ Phase 2)
- Migration BI dashboard hiện hữu (→ Phase sau)
- ML model production (→ Phase sau)
- Mua sắm license Databricks / Azure subscription (VC tự chịu)
- Hỗ trợ 24/7 dài hạn (cần MSA riêng nếu có nhu cầu)
- Training end-user sâu (chỉ có KT cho team kỹ thuật)

---

## 6. Toolchain & Access

| Tool | Tenant | Access Model | Notes |
|---|---|---|---|
| Microsoft Teams | VC | BC guest (Entra B2B) | Communication, meeting, channels theo WS |
| SharePoint Online | VC | BC guest — Contributor | Document repository (cấu trúc per WS) |
| Azure DevOps | VC | BC — Stakeholder + Basic | Backlog, Repo (code/notebook/IaC), Wiki |
| Azure Key Vault | VC | BC — Read via managed identity | Secrets, không bao giờ commit |
| Databricks Workspace | VC | BC — Workspace user, UC scoped | Build & run |
| Email | Mỗi bên dùng tenant riêng | — | Of-record formal comm |

### 6.1 SharePoint Folder Structure

Site name: `Databricks-P1 — VC x BC` (gắn Teams cùng tên, host trên tenant VC).

```
/00_Read_First/         — Onboarding pack (đọc đầu tiên): Start Here, One-Pager, Team Directory,
                          Where-To-Find-What, Glossary, Tools Access Guide, FAQ
/01_Governance/         — Charter, Working Agreement, Comm Plan, Steerco, RAID, CR, Templates
/02_WS1_Assessment_PMS_MarketS/
/03_WS2_Assessment_Sources/
    /01_MIO/ /02_Salesforce/ /03_Distributor/ /04_Custodian/
    /05_Excel/ /06_VSDC/ /07_ESM/ /08_Datahub/
    /09_Consolidated_Findings/ /10_Roadmap_Final/
/04_WS3_Design_Setup_PoC/
/05_WS4_Closure/
/06_Shared_References/
/07_Reports/
/99_Archive/
```

**Numbering convention**:
- `00` = Read First (onboarding, đọc trước khi vào folder khác)
- `01` = Governance (quy trình & artifact chính)
- `02–05` = 4 Workstream theo timeline
- `06` = Shared references
- `07` = Reports
- `99` = Archive (luôn nằm cuối khi sort)

### 6.2 Teams Channels

- `#general` — announcement, pinned doc
- `#daily-sync` — daily standup + EOD summary
- `#ws1-assessment-pms` — WS1 discussion
- `#ws2-assessment-sources` — WS2 discussion
- `#ws3-core-platform` — WS3 technical discussion
- `#governance` — Steerco material, formal announcement

---

## 7. Governance & Cadence

| Forum | Cadence | Attendees | Decisions |
|---|---|---|---|
| Daily Sync 3 WS | Daily (T2–T6) 09:00, 15–20' | Tin Huynh + 3 WS Lead (+ Hien Vo opt) | Blocker, dependency |
| WS Workshop | On-demand per system | WS Lead + VC SME | Assessment findings |
| Architecture Review | Per milestone | Dung Phan + Hien Vo | ADR, design decisions |
| Weekly Status | Weekly (T6) 16:00, 45' | Tin Huynh + Khiem Pham (+ Hien Vo) | Schedule, RAID review |
| WS Milestone Review | Per milestone | WS Lead + Khiem Pham + Tin Huynh | Accept deliverable |
| Steering Committee | Bi-weekly, 45' | Nguyen Le + Khiem Pham + Tin Huynh | Scope, escalation |
| PoC Demo | 29/06–03/07/2026 | Full team + VC stakeholders | Acceptance Demo |
| Closure Meeting | 06/07–10/07/2026 | Full team + Sponsors | Sign-off |

### 7.1 Escalation Path

L1: Team → WS Lead / Dung Phan
L2: → Tin Huynh (BC PM)
L3: → Khiem Pham (VC PO) hoặc Nguyen Le (BC escalation)
L4: → Steerco (Sev1 escalate ngay)

---

## 8. Key Risks (initial register)

| # | Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| R1 | Chậm cấp Azure access / Databricks workspace cho BC | High | Medium | Pre-flight checklist tuần 0, escalate VC IT |
| R2 | 9 system owner phía VC không sắp xếp được lịch | High | High | Khiem Pham pre-block calendar, escalate Steerco |
| R3 | Tài liệu hệ thống nguồn thiếu/lỗi thời | Medium | High | Interview bổ sung, best-effort cho Phase 1 |
| R4 | 3 WS song song gây quá tải coordination | Medium | Medium | Daily sync chia per WS, WS owner model |
| R5 | PoC scope creep từ VC business team | Medium | Medium | Lock PoC scope sau Design, CR bắt buộc |
| R6 | Compliance review (SSC/SBV) phát sinh | Medium | Low | Engage VC Security sớm trong WS3 Design |
| R7 | Timeline 7.5 tuần không buffer rework | High | Medium | Weekly RAG, sớm flag để negotiate |

---

## 9. Decisions Log

> Ghi lại các quyết định quan trọng. Format: `YYYY-MM-DD | Decision | Decided by | Rationale`

| Date | Decision | Decided by | Rationale |
|---|---|---|---|
| 2026-05-12 | Cloud platform = Azure | VC + BC | VC tenant Microsoft sẵn có |
| 2026-05-12 | Hybrid working mode (onsite + remote) | VC + BC | Cần onsite cho assessment workshop |
| 2026-05-12 | SharePoint host trên tenant VC | VC + BC | Tránh migrate sau project close |
| 2026-05-12 | Footer owner mọi PM artifact = Nguyen Le (PO) | BC | PO accountability |
| 2026-05-12 | Thêm folder `00_Read_First` làm onboarding pack; renumber `00_Governance` → `01_Governance` | BC | Tốc độ onboard team mới khi parallel 3 WS chạy gấp |
| _add new..._ | | | |

---

## 10. Open Questions / TBD

> Câu hỏi chưa có câu trả lời. Bổ sung khi clarify.

- [ ] WS1 Lead phía BC là ai?
- [ ] WS2 Lead phía BC là ai?
- [ ] Team size BC (số người fulltime / parttime)?
- [ ] VC IT Infra contact (cho Entra B2B onboarding)?
- [ ] VC Security / Compliance contact?
- [ ] VC SME 9 hệ thống nguồn — danh sách + thời gian available?
- [ ] Engagement model: Fixed price / T&M / Outcome-based?
- [ ] VC business unit chính là stakeholder? (Asset Mgmt / Real Estate / Venture / VFM / DCVFM / VOF)
- [ ] Compliance constraint cụ thể (SSC/SBV, data residency)?
- [ ] Lịch nghỉ phép VC trong 18/05–10/07/2026?
- [ ] Hard deadline reason cho 09/07?
- [ ] Tenant domain cụ thể của VC (custom domain hay onmicrosoft.com)?

---

## 11. Deliverable Artifacts

| File | Mục đích | Path |
|---|---|---|
| Project Charter | Charter chính thức ký 2 bên | `01_Project_Charter_Template.docx` |
| Working Agreement | Quy tắc phối hợp 2 bên | `02_Working_Agreement.docx` |
| SharePoint Folder Structure | Design tài liệu repo | `03_SharePoint_Folder_Structure.docx` |
| Communication Plan | Cadence + channel matrix | `04_Communication_Plan.docx` |
| Generator script | Regenerate 4 file trên | `_generate_docs.py` |

### 11.1 Regenerate command

```bash
cd /Users/rom/Projects/research
source .venv-docx/bin/activate
python3 docs/databricks-pm/_generate_docs.py
```

### 11.2 Cách update file Word

1. Edit `_generate_docs.py` — các constant ở đầu file (VENDOR, CUSTOMER, dates, people)
2. Hoặc edit nội dung section trong từng function
3. Chạy script → file `.docx` được overwrite

---

## 12. Change Log

| Date | Change | By |
|---|---|---|
| 2026-05-12 | Initial context document created | Claude (Nguyen Le's request) |
| 2026-05-12 | Section 6.1: Thêm `00_Read_First` folder, renumber `00_Governance` → `01_Governance` | Claude |
| 2026-05-12 | Section 3.2: Thêm Tess Pham (BC Finance BA) — confirmed by user | Claude |
| 2026-05-13 | Thêm Section 0 Operational Playbook + cập nhật constants line refs (13–40) | Claude |
| _add new..._ | | |

---

## 13. Cross-References

- Memory: `/Users/rom/.claude/projects/-Users-rom-Projects-research/memory/databricks_p1_blue_coral_vinacapital.md`
- Output folder: `/Users/rom/Projects/research/docs/databricks-pm/`
- Generator: `_generate_docs.py` (constants block at top — **lines 13–40**)
- venv: `/Users/rom/Projects/research/.venv-docx/` (python-docx 1.2.0)
