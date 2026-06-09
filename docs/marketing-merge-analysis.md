# Phân tích merge `marketingskills` vào `bmad-performance-marketing`

Ngày phân tích: 2026-05-05  
Repo nguồn: `/Users/rom/Projects/marketingskills`  
Repo đích: `/Users/rom/Projects/bmad-performance-marketing`  
Phạm vi: chỉ đọc hai repo nguồn/đích; báo cáo này là artifact duy nhất được tạo trong repo `research`.

## Executive Summary

`marketingskills` trưởng thành hơn về độ phủ nghiệp vụ marketing: 40 skill granular, nhiều reference playbook, nhiều eval fixture, bao phủ CRO, SEO, paid, lifecycle, RevOps, pricing, retention, referral, ASO, image/video và tool integrations. Evidence: README mô tả thư viện skill marketing rộng ở [marketingskills/README.md:3](/Users/rom/Projects/marketingskills/README.md:3), danh sách 40 skill ở [marketingskills/.claude-plugin/marketplace.json:15](/Users/rom/Projects/marketingskills/.claude-plugin/marketplace.json:15).

`bmad-performance-marketing` trưởng thành hơn về cấu trúc BMAD: module code, install variables, agent roster, `customize.toml`, menu codes, workflow skills, marketplace liệt kê explicit skills. Evidence: BMAD v6 module có 14 agent + 6 workflow ở [README.md:15](/Users/rom/Projects/bmad-performance-marketing/README.md:15), module variables và agents ở [skills/module.yaml:1](/Users/rom/Projects/bmad-performance-marketing/skills/module.yaml:1), manifest explicit skills ở [.claude-plugin/marketplace.json:22](/Users/rom/Projects/bmad-performance-marketing/.claude-plugin/marketplace.json:22).

Khuyến nghị merge: giữ `bmad-performance-marketing` làm khung chính; chuyển nghiệp vụ từ `marketingskills` thành capability dưới các agent/workflow BMAD hiện có hoặc agent mới khi capability là domain lớn. Không copy nguyên thư mục skill nguồn vào repo đích vì convention, activation, config path và artifact model khác nhau.

## 1. Khảo sát từng repo

### `marketingskills`

#### Cấu trúc cấp 1-2

| Đường dẫn | Mục đích |
|---|---|
| `.claude-plugin/marketplace.json` | Manifest plugin đơn giản, một plugin `marketing-skills`, mô tả 40 skill nhưng không liệt kê từng skill path explicit. |
| `.github/` | Issue/PR template, scripts, workflows cho maintenance repo. |
| `skills/<capability>/SKILL.md` | 40 skill độc lập theo Agent Skills spec, mỗi skill chứa frontmatter `name`, `description`, `metadata.version`, workflow nội tuyến. |
| `skills/<capability>/references/` | Reference playbooks, templates, platform specs, benchmarks. Không phải skill nào cũng có. |
| `skills/<capability>/evals/` | Evals JSON cho đa số skill nhưng không đầy đủ toàn bộ. |
| `tools/clis/` | CLI wrapper cho nhiều marketing tools/platforms. |
| `tools/integrations/` | Documentation tích hợp tool marketing. |
| `tools/composio/` | Mapping tool qua Composio. |
| `tools/REGISTRY.md` | Registry tool/integration. |

#### Phạm vi nghiệp vụ

Repo nguồn cover các nhóm sau:

- Foundation: `product-marketing-context`, được xem là context nền cho mọi skill ở [README.md:19](/Users/rom/Projects/marketingskills/README.md:19).
- SEO & discovery: `seo-audit`, `ai-seo`, `programmatic-seo`, `site-architecture`, `competitor-alternatives`, `competitor-profiling`, `schema-markup`, `aso-audit`, `directory-submissions`.
- CRO: `page-cro`, `signup-flow-cro`, `onboarding-cro`, `form-cro`, `popup-cro`, `paywall-upgrade-cro`.
- Content/copy/social: `content-strategy`, `copywriting`, `copy-editing`, `social-content`, `image`, `video`.
- Paid/measurement: `paid-ads`, `ad-creative`, `analytics-tracking`, `ab-test-setup`.
- Growth/retention/monetization: `churn-prevention`, `free-tool-strategy`, `referral-program`, `lead-magnets`, `pricing-strategy`, `marketing-ideas`, `marketing-psychology`.
- Sales/RevOps: `revops`, `sales-enablement`, `cold-email`, `email-sequence`.

#### Artifacts hiện có

- 40 `SKILL.md`.
- 62 reference files trong `skills/*/references`.
- 32 eval files trong `skills/*/evals`.
- Không có BMAD `module.yaml`, `module-help.csv`, `customize.toml`, agent roster, workflow folder theo BMAD.
- Không có workflow cross-agent top-level; workflow nằm trong từng skill.

#### Mức độ hoàn thiện

Đánh giá tĩnh: nghiệp vụ 4/5, cấu trúc BMAD 1/5.

Lý do: nhiều skill dài và có references/evals, ví dụ `seo-audit` 497 dòng, `copy-editing` 508 dòng, `marketing-psychology` 455 dòng. Nhưng convention là Agent Skills spec chứ không phải BMAD; skill trực tiếp đọc `.agents/product-marketing-context.md` như [product-marketing-context/SKILL.md:12](/Users/rom/Projects/marketingskills/skills/product-marketing-context/SKILL.md:12), không dùng `_bmad/performance-marketing/config.yaml`.

#### Convention

- Skill ID không có prefix `bmad-`, ví dụ `seo-audit` ở [seo-audit/SKILL.md:2](/Users/rom/Projects/marketingskills/skills/seo-audit/SKILL.md:2).
- Frontmatter có `metadata.version`, ví dụ [seo-audit/SKILL.md:4](/Users/rom/Projects/marketingskills/skills/seo-audit/SKILL.md:4).
- Workflow được viết trong một `SKILL.md` theo section như `Initial Assessment`, `Core Principles`, `Workflow`, không có `customize.toml`.
- Context foundation cố định vào `.agents/product-marketing-context.md`, xem [product-marketing-context/SKILL.md:3](/Users/rom/Projects/marketingskills/skills/product-marketing-context/SKILL.md:3) và [product-marketing-context/SKILL.md:18](/Users/rom/Projects/marketingskills/skills/product-marketing-context/SKILL.md:18).

### `bmad-performance-marketing`

#### Cấu trúc cấp 1-2

| Đường dẫn | Mục đích |
|---|---|
| `.claude-plugin/marketplace.json` | Manifest BMAD plugin, explicit list 20 skill path. |
| `skills/module.yaml` | Metadata module, variables install-time, agent roster. |
| `skills/module-help.csv` | Catalog skill/menu code/phase/output. |
| `skills/orchestrator/bmad-marketing-orchestrator/` | Tier 1 marketing orchestrator. |
| `skills/leads/bmad-*` | Tier 2 leads: content, SEO, social, launch, growth. |
| `skills/specialists/bmad-*` | Tier 3 social/platform specialists. |
| `skills/workflows/bmad-*` | 6 cross-functional workflow skills. |
| `_memory/<agent-sidecar>/` | Memory/instruction template sidecars. |
| `legacy/agents`, `legacy/workflows` | Legacy v1 layout/reference. |

#### Phạm vi nghiệp vụ

- Strategy/orchestration: Marketing Orchestrator, Marketing Strategy workflow.
- Content: Content Architect, Content Pipeline.
- SEO: SEO Strategist, SEO Sprint.
- Social: Social Media Strategist + Twitter, Reddit, LinkedIn, YouTube, Discord, Instagram, TikTok, Pinterest specialists; Social Campaign workflow.
- Launch: Launch Coordinator, Launch Sequence workflow.
- Analytics/growth: Growth Analyst, Growth Audit workflow.

#### Artifacts hiện có

- 14 agent skills with `SKILL.md` + `customize.toml`.
- 6 workflow skills with `SKILL.md` + `customize.toml`.
- `module.yaml`, `module-help.csv`.
- Root `_memory` sidecar templates.
- Legacy YAML/XML-like agents and YAML workflows retained as reference.

#### Mức độ hoàn thiện

Đánh giá tĩnh: nghiệp vụ 3/5, cấu trúc BMAD 4/5.

Lý do: module và activation chuẩn BMAD rõ ràng; mỗi agent có `customize.toml` chứa persona/menu. Nhưng nghiệp vụ hiện tập trung vào strategy/content/SEO/social/launch/analytics, thiếu nhiều capability sâu từ `marketingskills` như paid ads, CRO suite, lifecycle email, RevOps, pricing, referral, ASO, AI SEO, pSEO. Workflow còn inline trong `SKILL.md`, ví dụ phases/steps của Marketing Strategy nằm ở [bmad-marketing-strategy/SKILL.md:71](/Users/rom/Projects/bmad-performance-marketing/skills/workflows/bmad-marketing-strategy/SKILL.md:71), chưa tách `step-NN-*.md`.

#### Convention

- Skill ID prefix `bmad-*`, ví dụ [bmad-content-architect/SKILL.md:2](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/SKILL.md:2).
- Activation bắt buộc resolve customization qua `_bmad/scripts/resolve_customization.py`, xem [bmad-content-architect/SKILL.md:23](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/SKILL.md:23).
- Config path chuẩn module: `_bmad/performance-marketing/config.yaml`, xem [bmad-content-architect/SKILL.md:49](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/SKILL.md:49).
- Persona/menu tách trong `customize.toml`, ví dụ menu `CC`, `CB`, `BS`, `LP` ở [bmad-content-architect/customize.toml:47](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/customize.toml:47).
- Output artifacts đi qua `{marketing_artifacts}`, định nghĩa ở [skills/module.yaml:34](/Users/rom/Projects/bmad-performance-marketing/skills/module.yaml:34).

## 2. Phân tích đối chiếu

### Overlap

| Vùng | `marketingskills` | `bmad-performance-marketing` | Nhận xét |
|---|---|---|---|
| Marketing strategy | `marketing-ideas`, `marketing-psychology`, `customer-research`, `pricing-strategy`, `launch-strategy` | `bmad-marketing-orchestrator`, `bmad-marketing-strategy` | Target có orchestration; source có framework cụ thể. |
| Content strategy/copy | `content-strategy`, `copywriting`, `copy-editing`, `lead-magnets` | `bmad-content-architect`, `bmad-content-pipeline` | Source sâu về writing/editing; target sâu về agent persona/workflow. |
| SEO | `seo-audit`, `ai-seo`, `programmatic-seo`, `schema-markup`, `site-architecture`, `competitor-alternatives` | `bmad-seo-strategist`, `bmad-seo-sprint` | Target có sprint; source có subdomain SEO hiện đại hơn. |
| Social | `social-content`, `community-marketing`, `video`, `image` | Social lead + 8 platform specialists + `bmad-social-campaign` | Target có agent platform; source có generalized generation specs. |
| Launch | `launch-strategy`, `directory-submissions` | `bmad-launch-coordinator`, `bmad-launch-sequence` | Target có J-14 workflow; source có directory/Product Hunt supporting knowledge. |
| Analytics/testing | `analytics-tracking`, `ab-test-setup` | `bmad-growth-analyst`, `bmad-growth-audit` | Target có audit; source có implementation/tracking/test rigor. |

### Complementary

| Có ở source, thiếu rõ ở target | Tác động khi merge |
|---|---|
| CRO suite: page/signup/onboarding/form/popup/paywall | Cần agent/workflow `bmad-cro-strategist` hoặc mở rộng Growth Analyst/Content Architect. |
| Paid ads + ad creative | Cần Paid Media Buyer và Performance Creative workflow. |
| Lifecycle/cold email | Cần Lifecycle Marketer/Outbound Specialist hoặc workflow email. |
| RevOps + Sales Enablement | Cần Revenue Operations/Enablement capability. |
| Pricing/packaging | Cần Monetization Strategist hoặc menu trong Marketing Orchestrator. |
| Referral/affiliate/free tool/lead magnets | Cần Growth Engineering / Acquisition Loops workflow. |
| AI SEO, pSEO, ASO, schema, competitor pages | Nên bổ sung vào SEO Strategist hoặc tạo sub-workflows SEO. |
| Tool integrations/CLIs | Có thể giữ ngoài BMAD skill layer làm `references/tools` hoặc docs phụ trợ. |

### Conflict cụ thể

| Conflict | Evidence source | Evidence target | Hướng xử lý |
|---|---|---|---|
| Skill naming | Source dùng `seo-audit`, `paid-ads`, `page-cro` không prefix, ví dụ [seo-audit/SKILL.md:2](/Users/rom/Projects/marketingskills/skills/seo-audit/SKILL.md:2). | Target dùng `bmad-*`, manifest explicit `./skills/leads/bmad-seo-strategist` ở [.claude-plugin/marketplace.json:25](/Users/rom/Projects/bmad-performance-marketing/.claude-plugin/marketplace.json:25). | Đặt lại skill ID theo `bmad-<verb>-<object>` hoặc `bmad-agent-<role>`. |
| Context artifact | Source coi `.agents/product-marketing-context.md` là foundation ở [product-marketing-context/SKILL.md:12](/Users/rom/Projects/marketingskills/skills/product-marketing-context/SKILL.md:12). | Target dùng `{marketing_artifacts}` và `_bmad/performance-marketing/config.yaml` ở [module.yaml:34](/Users/rom/Projects/bmad-performance-marketing/skills/module.yaml:34), [bmad-content-architect/SKILL.md:49](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/SKILL.md:49). | Tạo `bmad-create-marketing-context`, output vào `{marketing_artifacts}/marketing-context.md`, và cho agents load artifact này. |
| Manifest model | Source manifest chỉ có `source: "./"` và mô tả 40 skills ở [marketplace.json:14](/Users/rom/Projects/marketingskills/.claude-plugin/marketplace.json:14). | Target manifest explicit list 20 skills ở [marketplace.json:22](/Users/rom/Projects/bmad-performance-marketing/.claude-plugin/marketplace.json:22). | Mọi skill/agent mới phải thêm explicit vào target manifest. |
| Agent/workflow separation | Source không có agent persona riêng; skill tự chứa role/workflow, ví dụ `Paid Ads` tự nói "You are an expert..." ở [paid-ads/SKILL.md:10](/Users/rom/Projects/marketingskills/skills/paid-ads/SKILL.md:10). | Target tách identity/menu vào `customize.toml`, ví dụ [bmad-content-architect/customize.toml:32](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/customize.toml:32). | Convert source content thành prompt/menu/reference dưới agent hoặc workflow, không giữ nguyên role text. |
| Workflow granularity | Source workflow nằm trong từng skill; target workflow cũng inline phase/steps trong `SKILL.md`, ví dụ [bmad-marketing-strategy/SKILL.md:71](/Users/rom/Projects/bmad-performance-marketing/skills/workflows/bmad-marketing-strategy/SKILL.md:71). | Yêu cầu merge mong muốn format `step-NN-<name>.md`; target hiện chưa có folder step files. | Trước khi merge lớn, chuẩn hóa workflow mới thành `steps/step-NN-*.md` hoặc quyết định giữ convention inline hiện tại. |
| Memory path | Target repo layout có root `_memory` ở [README.md:129](/Users/rom/Projects/bmad-performance-marketing/README.md:129). | `customize.toml` lại append/load `{project-root}/_bmad/_memory/...` ở [bmad-content-architect/customize.toml:21](/Users/rom/Projects/bmad-performance-marketing/skills/leads/bmad-content-architect/customize.toml:21). | Xác nhận install process copy root `_memory` vào `_bmad/_memory`; nếu không, sửa path convention trước khi merge. |
| Ngôn ngữ legacy | Legacy agents dùng nhiều tiếng Pháp trong persona/prompts. | Current v2 skill dùng English, config language runtime. | Không merge legacy content trừ khi cần history; tránh đưa French artifact vào workflow mới. |

## 3. Tracking Table

Thang điểm hoàn thiện: 1 = ý tưởng/sơ khai, 3 = dùng được nhưng cần refactor/test/convention, 5 = production-ready theo target BMAD. Điểm dựa trên phân tích tĩnh artifacts, line count, references/evals và mức khớp convention BMAD.

### Agents

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái | Độ hoàn thiện ms | Độ hoàn thiện bpm | Hành động đề xuất khi merge | Ghi chú conflict |
|---|---|---|---|---:|---:|---|---|
| Marketing Orchestrator | Không | `bmad-marketing-orchestrator` | unique bpm | 1 | 4 | Keep làm entrypoint. | Source có strategy skills nhưng không có orchestrator. |
| Content Architect | `content-strategy`, `copywriting`, `copy-editing`, `lead-magnets` | `bmad-content-architect` | overlap/complement | 4 | 4 | Keep agent, import source references thành menu/subskills. | Cần tránh duplicate `CB` menu code nếu thêm campaign brief. |
| SEO Strategist | `seo-audit`, `ai-seo`, `programmatic-seo`, `schema-markup`, `site-architecture`, `competitor-*`, `aso-audit` | `bmad-seo-strategist` | overlap/complement | 4 | 4 | Extend agent + thêm workflow SEO subdomain. | `ai-seo`, `ASO`, pSEO chưa rõ trong target. |
| Social Media Strategist | `social-content`, `community-marketing`, `video`, `image` | `bmad-social-media-strategist` | overlap | 4 | 4 | Keep, import generic social-content as lead playbook. | Target có platform specialists, source là generic social skill. |
| Launch Coordinator | `launch-strategy`, `directory-submissions` | `bmad-launch-coordinator` | overlap/complement | 4 | 4 | Keep, import directory/PH/hunter supporting templates. | Source directory submissions là separate skill. |
| Growth Analyst | `analytics-tracking`, `ab-test-setup`, `churn-prevention` | `bmad-growth-analyst` | overlap/complement | 4 | 4 | Keep, import analytics implementation + A/B stats references. | Target growth audit thiếu tracking implementation detail. |
| Twitter/X Specialist | Trong `social-content` | `bmad-twitter-ghostwriter` | overlap bpm richer | 3 | 4 | Keep target; source platform-limits/templates làm references. | Không cần agent mới. |
| Reddit Specialist | `community-marketing`, `social-content` | `bmad-reddit-growth-hacker` | overlap bpm richer | 3 | 4 | Keep target, import community strategy guardrails. | Cần moderation/non-spam constraints từ source nếu có. |
| LinkedIn Specialist | `social-content`, `sales-enablement` | `bmad-linkedin-creator` | overlap bpm richer | 3 | 4 | Keep target, import B2B copy rules. | Không cần agent mới. |
| YouTube Specialist | `video`, `social-content` | `bmad-youtube-strategist` | overlap/complement | 3 | 4 | Keep target, import AI/programmatic video references. | Source video thiên production tools. |
| Discord Community Manager | `community-marketing` | `bmad-discord-community-manager` | overlap bpm richer | 3 | 4 | Keep target, import community-led growth strategy. | Source không giới hạn Discord. |
| Instagram/TikTok/Pinterest Specialists | `social-content`, `video`, `image` | `bmad-instagram-strategist`, `bmad-tiktok-creator`, `bmad-pinterest-strategist` | overlap bpm richer | 3 | 4 | Keep target; source cung cấp generic templates/specs. | Không copy nguyên social-content thành agent cạnh tranh. |
| Paid Media Buyer | `paid-ads`, `ad-creative` | Không | unique ms | 4 | 1 | Tạo agent mới `bmad-agent-paid-media-buyer`. | Domain lớn, không nên nhét hết vào Growth Analyst. |
| CRO Strategist | `page-cro`, `signup-flow-cro`, `onboarding-cro`, `form-cro`, `popup-cro`, `paywall-upgrade-cro` | Không rõ agent riêng | unique ms | 4 | 1 | Tạo agent mới `bmad-agent-cro-strategist`. | Có overlap nhỏ với Content/Growth nhưng cần owner riêng. |
| Lifecycle/Email Marketer | `email-sequence`, `cold-email`, `churn-prevention` | Không | unique ms | 4 | 1 | Tạo agent mới hoặc specialist dưới Growth. | Cold outbound và lifecycle email có logic khác nhau. |
| RevOps/Sales Enablement | `revops`, `sales-enablement` | Không | unique ms | 4 | 1 | Tạo `bmad-agent-revops-architect` hoặc split RevOps/Sales Enablement. | Cần quyết định phạm vi sales-led GTM. |
| Monetization Strategist | `pricing-strategy`, `paywall-upgrade-cro` | Không | unique ms | 4 | 1 | Tạo `bmad-agent-monetization-strategist` hoặc menu trong Orchestrator. | Pricing có thể là strategy gate. |

### Skills

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái | Độ hoàn thiện ms | Độ hoàn thiện bpm | Hành động đề xuất khi merge | Ghi chú conflict |
|---|---|---|---|---:|---:|---|---|
| product-marketing-context | Có | Không rõ | conflict/foundation | 4 | 1 | Rewrite thành `bmad-create-marketing-context`. | Source output `.agents`, target output `{marketing_artifacts}`. |
| customer-research | Có | Trong Marketing Strategy gián tiếp | complement | 4 | 2 | Thêm menu research cho Orchestrator/Mary hoặc new skill. | Không có owner rõ trong target. |
| marketing-ideas | Có | Orchestrator channel prioritization | complement | 4 | 3 | Refactor thành reference cho Orchestrator. | Tránh skill độc lập gây trùng strategy. |
| marketing-psychology | Có | Không rõ | complement | 4 | 1 | Import làm reference/template dùng bởi copy/CRO/ads. | Không nên tạo agent riêng. |
| content-strategy | Có | `bmad-content-architect` | overlap | 4 | 4 | Merge vào Content Architect menus/references. | Target đã có `CC`, `CB`, `BS`, `LP`. |
| copywriting | Có | `bmad-content-architect` | complement | 4 | 3 | Thêm menu `CW` hoặc reference copy frameworks. | `LP` đã cover landing copy một phần. |
| copy-editing | Có | Không rõ | complement | 4 | 1 | Thêm menu `CE` Content Architect. | Có thể cần editorial review workflow. |
| lead-magnets | Có | Không rõ | complement | 3 | 1 | Thêm vào Content Architect hoặc Growth Engineering. | Output lead magnet templates. |
| seo-audit | Có | `bmad-seo-strategist`, `bmad-seo-sprint` | overlap | 4 | 4 | Merge audit framework into SEO Sprint. | Source có implementation limitations line refs. |
| ai-seo | Có | Không rõ | unique/complement | 4 | 1 | Tạo menu `AI` trong SEO Strategist hoặc `bmad-optimize-ai-search`. | AI search là domain mới. |
| programmatic-seo | Có | Không rõ | unique/complement | 4 | 1 | Tạo workflow pSEO dưới SEO Strategist. | Cần template data/schema. |
| schema-markup | Có | Mention trong SEO Sprint | complement | 4 | 2 | Thêm subskill/reference implementation. | Target chỉ mention, source có examples. |
| site-architecture | Có | SEO/content gián tiếp | complement | 4 | 2 | Add workflow step before content/SEO. | Cần preserve URL/IA constraints. |
| competitor-alternatives | Có | Orchestrator/SEO gián tiếp | complement | 4 | 2 | Add skill `bmad-create-competitor-page`. | Nối sales enablement + SEO. |
| competitor-profiling | Có | Marketing Strategy competitor analysis | complement | 3 | 2 | Add research step/template. | Source yêu cầu scraping/live data. |
| aso-audit | Có | Không | unique ms | 3 | 1 | Optional specialist/skill `bmad-run-aso-audit`. | Chỉ cần nếu marketing module target mobile apps. |
| directory-submissions | Có | Launch Coordinator mentions directories | complement | 3 | 3 | Import directory list as launch reference. | Không cần agent riêng. |
| social-content | Có | Social lead + specialists | overlap | 4 | 4 | Split platform limits/templates into specialists. | Source generic, target platform-specific. |
| image | Có | Không rõ | unique/complement | 3 | 1 | Add to Content/Social production references. | Could depend on AI image tools. |
| video | Có | YouTube/TikTok partly | complement | 3 | 3 | Import AI video production into YouTube/TikTok. | Production vs strategy distinction. |
| paid-ads | Có | Không | unique ms | 4 | 1 | Create Paid Media Buyer agent/workflow. | Major missing acquisition channel. |
| ad-creative | Có | Không | unique ms | 4 | 1 | Add Performance Creative menu/workflow under Paid Media. | Could also serve social paid. |
| analytics-tracking | Có | Growth Analyst | complement | 4 | 3 | Import implementation/checklist into Growth Analyst. | Source is more technical. |
| ab-test-setup | Có | Growth Analyst | complement | 4 | 3 | Import statistical/test design references. | Target has menu AB but less reference-rich. |
| page-cro | Có | Content/Growth overlap | unique-ish ms | 4 | 1 | Create CRO Strategist; link Content/Growth. | Landing page copy overlap with Content Architect. |
| signup-flow-cro | Có | Growth Analyst funnel overlap | complement | 4 | 2 | Add CRO workflow step. | Product activation, not marketing page only. |
| onboarding-cro | Có | Growth Analyst retention overlap | complement | 4 | 2 | Add activation workflow. | Needs product data. |
| form-cro | Có | CRO missing | unique ms | 4 | 1 | Add as CRO subskill. | Not signup forms. |
| popup-cro | Có | CRO missing | unique ms | 4 | 1 | Add as CRO subskill. | High risk UX/compliance. |
| paywall-upgrade-cro | Có | Monetization/CRO missing | unique ms | 4 | 1 | Add to Monetization + CRO. | Conflicts with pricing owner. |
| churn-prevention | Có | Growth Analyst retention partly | complement | 4 | 2 | Add retention workflow under Growth/Lifecycle. | Dunning/payment tools references useful. |
| email-sequence | Có | Launch Sequence has email mention | complement | 4 | 2 | Create lifecycle email workflow. | Launch email is not lifecycle email. |
| cold-email | Có | Không | unique ms | 4 | 1 | Add Outbound/SDR capability. | Could sit under RevOps/Sales Enablement. |
| free-tool-strategy | Có | Không | unique ms | 4 | 1 | Add Growth Engineering workflow. | Needs tech feasibility handoff. |
| referral-program | Có | Launch/growth maybe | complement | 4 | 1 | Add referral/affiliate workflow under Growth. | Incentive/compliance decisions. |
| pricing-strategy | Có | Orchestrator budget/strategy indirect | unique ms | 4 | 1 | Add Monetization strategy skill. | Required before paywall work. |
| revops | Có | Growth Analyst only metrics | unique ms | 4 | 1 | Create RevOps agent. | Sales systems are outside current target. |
| sales-enablement | Có | Content/LinkedIn partial | unique ms | 4 | 1 | Create Sales Enablement workflow or RevOps subskill. | Could overlap with competitor pages. |

### Workflows

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái | Độ hoàn thiện ms | Độ hoàn thiện bpm | Hành động đề xuất khi merge | Ghi chú conflict |
|---|---|---|---|---:|---:|---|---|
| Marketing Strategy | Capabilities scattered | `bmad-marketing-strategy` | overlap bpm foundation | 2 | 4 | Keep target, add source research/positioning inputs. | Workflow inline not step files. |
| Content Pipeline | Skill-level content flow | `bmad-content-pipeline` | overlap bpm foundation | 3 | 4 | Keep target, import source copy/edit/lead magnet templates. | Need final publishing/monitoring gates. |
| Social Campaign | `social-content` workflow | `bmad-social-campaign` | overlap bpm richer | 3 | 4 | Keep target, import platform specs. | Target covers more specialists. |
| Launch Sequence | `launch-strategy`, `directory-submissions` | `bmad-launch-sequence` | overlap bpm richer | 4 | 4 | Keep target, import source directory/Product Hunt assets. | Need dedupe Product Hunt logic. |
| Growth Audit | Analytics/testing/churn source skills | `bmad-growth-audit` | overlap/complement | 4 | 4 | Keep, import analytics implementation + retention diagnostics. | Target audit broad but less implementation. |
| SEO Sprint | SEO source skills | `bmad-seo-sprint` | overlap/complement | 4 | 4 | Keep, extend with AI SEO/pSEO/schema/site architecture. | AI SEO absent. |
| Marketing Context Foundation | `product-marketing-context` | Không | unique ms required | 4 | 1 | Add required gate workflow. | Must change output path. |
| CRO Sprint | CRO skills | Không | unique ms | 4 | 1 | Add workflow. | Needs agent owner. |
| Paid Acquisition Sprint | `paid-ads`, `ad-creative` | Không | unique ms | 4 | 1 | Add workflow. | Needs budget/platform/tracking gate. |
| Lifecycle Revenue | `email-sequence`, `cold-email`, `churn-prevention`, `revops` | Không | unique ms | 4 | 1 | Add workflow(s), maybe split lifecycle vs outbound. | Scope decision needed. |
| Monetization & Pricing | `pricing-strategy`, `paywall-upgrade-cro` | Không | unique ms | 4 | 1 | Add workflow. | Pricing before paywall gate. |
| Growth Engineering Loop | `free-tool-strategy`, `referral-program`, `lead-magnets`, `programmatic-seo` | Không | unique ms | 4 | 1 | Add optional acquisition loop workflow. | Needs engineering dependencies. |

### Templates / References

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái | Độ hoàn thiện ms | Độ hoàn thiện bpm | Hành động đề xuất khi merge | Ghi chú conflict |
|---|---|---|---|---:|---:|---|---|
| Skill references | 62 files | Gần như không có `references/` trong current skills | complement ms richer | 4 | 1 | Move selected references into target skill folders. | Avoid dumping all; curate per agent/workflow. |
| Evals | 32 eval files | Không thấy evals trong target skills | complement | 3 | 1 | Keep/adapt evals for converted capabilities. | Need BMAD-compatible eval runner decision. |
| Tool integrations | `tools/clis`, `tools/integrations` | Không | complement | 3 | 1 | Store under `references/tools` or separate docs, not activation path. | Some CLIs may need maintenance/security review. |
| Memory sidecars | Không | `_memory/*` | unique bpm | 1 | 3 | Keep target. | Path install ambiguity noted above. |

### Configs / Docs

| Hạng mục | Có ở marketingskills | Có ở bmad-performance-marketing | Trạng thái | Độ hoàn thiện ms | Độ hoàn thiện bpm | Hành động đề xuất khi merge | Ghi chú conflict |
|---|---|---|---|---:|---:|---|---|
| Plugin manifest | Simple marketplace plugin | BMAD marketplace explicit skills | conflict | 2 | 4 | Use target manifest; append new skill paths. | Do not copy source manifest. |
| BMAD module metadata | Không | `skills/module.yaml` | unique bpm | 1 | 4 | Extend agents/help variables only. | Add new variables if paid/CRO need budget/site_url. |
| Help catalog | Không | `skills/module-help.csv` | unique bpm | 1 | 4 | Add every new agent/workflow/skill with menu code. | Keep CSV consistent with manifest. |
| Readme | Broad skill library docs | BMAD module docs | overlap/conflict | 3 | 4 | Update target README after merge. | Source install docs are not BMAD-specific. |
| Legacy | Không | Legacy v1 agents/workflows | unique bpm legacy | 1 | 2 | Keep as reference only or drop after migration. | French content/convention mismatch. |

## 4. Đánh giá tổng kết

### Repo nào trưởng thành hơn?

- Nghiệp vụ: `marketingskills` hơn. Nó có 40 skill, references/evals, và coverage dày ở những mảng performance marketing mà target còn thiếu.
- Cấu trúc: `bmad-performance-marketing` hơn. Nó có BMAD v6 module, agent hierarchy, customize layer, module-help catalog và workflow skills.
- Sẵn sàng merge trực tiếp: không repo nào đủ để copy nguyên xi. Target là skeleton đúng; source là content/capability reservoir.

### Top 5 conflict nghiêm trọng nhất

1. Context foundation path/model: `.agents/product-marketing-context.md` vs `{marketing_artifacts}` và `_bmad/performance-marketing/config.yaml`.
2. Naming/registration: source skill IDs không `bmad-*`, source manifest không explicit skill paths.
3. Ownership domain: source skill tự đóng vai chuyên gia; target cần agent persona + menu + workflow facilitator.
4. Workflow format: yêu cầu mong muốn `step-NN-*.md`, target hiện inline trong `SKILL.md`, source cũng inline.
5. Missing target owners cho paid, CRO, lifecycle, RevOps, pricing: nếu merge vào Content/Growth hiện tại sẽ phình agent và giảm clarity.

### Risk khi merge và mitigation

| Risk | Mức độ | Mitigation |
|---|---|---|
| Agent bloat: nhồi 40 skill vào 5 leads hiện có | Cao | Tạo agent mới cho domain lớn: Paid, CRO, Lifecycle, RevOps/Monetization. |
| Convention drift: vừa Agent Skills spec vừa BMAD spec | Cao | Rewrite theo target convention; source chỉ làm domain content/reference. |
| Artifact path mismatch làm agent không đọc context chung | Cao | Chuẩn hóa `marketing-context.md` trong `{marketing_artifacts}` trước. |
| Duplicate menu codes | Trung bình | Duy trì registry code trong `module-help.csv`; kiểm tra code unique trước merge. |
| Tool integrations chưa review bảo mật/maintainability | Trung bình | Không đưa CLI vào activation; đưa vào references trước, runtime tool sau. |
| Evals mất giá trị khi rewrite | Trung bình | Adapt evals theo skill mới ngay sau mỗi capability migration. |
| Workflow thiếu gates | Trung bình | Mỗi workflow mới phải định rõ required/optional, approval gate, input/output. |

## 5. Đề xuất Naming cho Agent / Skill mới

| Capability gốc (ms) | Loại | Tên đề xuất | Skill ID | Menu code | Persona nếu agent | Lý do |
|---|---|---|---|---|---|---|
| product-marketing-context | skill/workflow | Create Marketing Context | `bmad-create-marketing-context` | `MC` | N/A | Foundation bắt buộc; đổi output từ `.agents` sang `{marketing_artifacts}`. Alternatives: `bmad-create-positioning-context`, `bmad-build-marketing-context`. |
| customer-research | skill | Synthesize Customer Research | `bmad-synthesize-customer-research` | `CR` | Có thể dùng Mary hoặc Orchestrator | Research là analysis phase, không cần agent mới nếu Mary/Max sở hữu. |
| CRO suite | agent | Casey Convert — CRO Strategist | `bmad-agent-cro-strategist` | `CRO` | Conversion optimization lead for pages, signup, onboarding, forms, popups, paywalls. | Domain đủ lớn và cross-functional; alternatives: Connie Flow, Victor Convert. |
| page-cro | skill | Optimize Marketing Page | `bmad-optimize-marketing-page` | `OP` | Casey Convert | Cụ thể hơn `page-cro`, tránh conflict với Content Architect landing copy. |
| signup/onboarding/form/popup/paywall CRO | workflow | Run CRO Sprint | `bmad-cro-sprint` | `CS` | Casey Convert | Gom các CRO artifacts thành sprint có test plan + analytics gate. |
| paid-ads | agent | Piper Spend — Paid Media Buyer | `bmad-agent-paid-media-buyer` | `PMB` | Paid acquisition specialist across Google, Meta, LinkedIn, X, retargeting and budget optimization. | Paid media là kênh acquisition lớn, cần owner riêng. Alternatives: Adrian Bid, Paula Media. |
| ad-creative | skill | Create Performance Ads | `bmad-create-performance-ads` | `PA` | Piper Spend hoặc Content Architect | Creative gắn paid workflow nhưng cũng cần copy framework. |
| analytics-tracking | skill | Audit Tracking Plan | `bmad-audit-tracking-plan` | `AT` | Pixel Metrics | Nâng Growth Analyst từ audit metrics sang implementation tracking. |
| ab-test-setup | skill | Design Experiment | `bmad-design-experiment` | `EX` | Pixel Metrics | Đúng verb-object, reuse Growth Analyst AB menu. |
| lifecycle email | agent | Ellie Lifecycle — Lifecycle Marketer | `bmad-agent-lifecycle-marketer` | `LCM` | Lifecycle and retention email strategist for onboarding, nurture, win-back, churn prevention. | Lifecycle khác social/content; cần own sequences. |
| cold-email | skill | Write Cold Outreach | `bmad-write-cold-outreach` | `CO` | Ellie Lifecycle hoặc RevOps | Outbound thuộc revenue motion, không phải lifecycle warm email. |
| email-sequence | skill/workflow | Create Lifecycle Email Sequence | `bmad-create-lifecycle-email-sequence` | `ES` | Ellie Lifecycle | Clear output: sequence map + email copy + triggers. |
| churn-prevention | workflow | Reduce Churn | `bmad-reduce-churn` | `RC` | Ellie Lifecycle + Pixel Metrics | Cần retention diagnosis + save offers + dunning. |
| revops | agent | Riley Revenue — RevOps Architect | `bmad-agent-revops-architect` | `RO` | Revenue systems specialist for lifecycle stages, scoring, routing, CRM handoff. | RevOps là systems owner, khác Growth Analyst. Alternatives: Rhea Ops, Morgan Pipeline. |
| sales-enablement | skill/workflow | Create Sales Enablement Kit | `bmad-create-sales-enablement-kit` | `SE` | Riley Revenue hoặc Content Architect | B2B sales collateral cần workflow riêng. |
| pricing-strategy | agent/skill | Morgan Monetize — Monetization Strategist | `bmad-agent-monetization-strategist` | `MON` | Pricing, packaging, paywall and upgrade strategist. | Pricing/paywall đủ quan trọng để có owner hoặc specialist. |
| referral/free-tool/lead magnets | workflow | Build Acquisition Loop | `bmad-build-acquisition-loop` | `AL` | Max Growth + Pixel Metrics | Gom growth engineering loops, referral, free tool, lead magnet. |
| programmatic-seo | workflow | Build Programmatic SEO System | `bmad-build-programmatic-seo` | `PSO` | Quinn Crawler | pSEO cần dataset/template/indexing gates. |
| ai-seo | skill | Optimize AI Search Visibility | `bmad-optimize-ai-search-visibility` | `AIS` | Quinn Crawler | Giữ dưới SEO, không tạo agent mới ban đầu. |
| aso-audit | skill | Run ASO Audit | `bmad-run-aso-audit` | `ASO` | Quinn Crawler hoặc ASO Specialist | Optional; chỉ cần agent mới nếu mobile apps là target core. |
| competitor-profiling/pages | workflow | Build Competitive Positioning Assets | `bmad-build-competitive-positioning-assets` | `CPA` | Max Growth + Quinn + Riley | Kết nối research, SEO pages, battlecards. |
| image/video production | skill | Create Marketing Media Brief | `bmad-create-marketing-media-brief` | `MM` | Content Architect/Social specialists | Nên là production brief, không phải generic media agent ngay. |

## 6. Đề xuất Workflow còn thiếu

### Workflow: Marketing Context Foundation
- Phase: 1-analysis
- Trigger: Trước mọi strategy/content/SEO/paid/CRO workflow trong project mới hoặc khi positioning thay đổi.
- Steps:
  1. `step-01-discover-product-context.md` - Thu thập product, ICP, use cases, GTM motion, pricing, competitors.
  2. `step-02-mine-existing-assets.md` - Đọc README/site/copy/docs hiện có để auto-draft context.
  3. `step-03-synthesize-positioning.md` - Tạo positioning, messaging pillars, customer language, differentiators.
  4. `step-04-user-validation-gate.md` - User review và sửa facts critical.
  5. `step-05-publish-marketing-context.md` - Lưu `{marketing_artifacts}/marketing-context.md`.
- Inputs: repo docs/site copy, user interview, competitor notes.
- Outputs: `marketing-context.md`, `positioning-summary.md`.
- After: none. Before: `bmad-marketing-strategy`, `bmad-content-pipeline`, `bmad-paid-acquisition-sprint`, `bmad-cro-sprint`.
- Required: yes.

### Workflow: CRO Sprint
- Phase: 3-execution
- Trigger: Khi page/signup/onboarding/form/paywall có conversion issue hoặc cần experiment backlog.
- Steps:
  1. `step-01-cro-intake.md` - Xác định surface, conversion goal, traffic source, baseline metrics.
  2. `step-02-diagnose-friction.md` - Audit clarity, friction, trust, UX, offer-message fit.
  3. `step-03-prioritize-hypotheses.md` - ICE/RICE scoring hypotheses.
  4. `step-04-design-experiments.md` - A/B or qualitative test plan, sample size, success metric.
  5. `step-05-ship-copy-and-ui-recommendations.md` - Deliver copy, UX changes, analytics events.
  6. `step-06-review-results.md` - Analyze outcomes and next iteration.
- Inputs: URL/screenshots, funnel metrics, analytics events, marketing context.
- Outputs: `cro-audit.md`, `experiment-backlog.md`, `variant-copy.md`, `tracking-plan.md`.
- After: `bmad-create-marketing-context`, optionally `bmad-audit-tracking-plan`. Before: implementation/dev story.
- Required: no, but required gate before major paid spend to unproven landing pages.

### Workflow: Paid Acquisition Sprint
- Phase: 2-planning / 3-execution
- Trigger: Khi chuẩn bị chạy paid campaigns hoặc cần optimize existing spend.
- Steps:
  1. `step-01-define-paid-goal.md` - Goal, budget, CPA/ROAS target, geography, constraints.
  2. `step-02-select-channels.md` - Pick Google/Meta/LinkedIn/X/TikTok based on intent and ICP.
  3. `step-03-build-offer-and-landing-fit.md` - Align offer, landing page, funnel, tracking.
  4. `step-04-create-ad-creative-matrix.md` - Headlines, primary text, image/video brief, variants.
  5. `step-05-launch-checklist.md` - Pixel/events, UTMs, budget caps, exclusions.
  6. `step-06-optimization-cadence.md` - Reporting, learning agenda, cut/scale rules.
- Inputs: marketing context, offer, landing page, budget, analytics access.
- Outputs: `paid-channel-plan.md`, `ad-creative-matrix.md`, `launch-checklist.md`, `optimization-rules.md`.
- After: `bmad-create-marketing-context`, `bmad-audit-tracking-plan`, optionally `bmad-cro-sprint`. Before: campaign launch.
- Required: no.

### Workflow: Lifecycle Revenue System
- Phase: 3-execution
- Trigger: Khi cần nurture, onboarding, win-back, cold outreach hoặc reduce churn.
- Steps:
  1. `step-01-map-lifecycle-stages.md` - Define lead/customer stages, triggers, segmentation.
  2. `step-02-identify-revenue-leaks.md` - Analyze activation, trial conversion, churn, handoff gaps.
  3. `step-03-design-sequences.md` - Welcome, nurture, activation, win-back, dunning or outbound sequence.
  4. `step-04-write-email-assets.md` - Subject lines, body copy, CTAs, personalization.
  5. `step-05-configure-tracking-and-handoff.md` - Events, CRM states, MQL/SQL handoff.
  6. `step-06-review-performance.md` - Open/click/reply/conversion/churn review.
- Inputs: CRM/lifecycle data, ICP, product value props, current email assets.
- Outputs: `lifecycle-map.md`, `email-sequences.md`, `revops-handoff.md`, `retention-plan.md`.
- After: `bmad-create-marketing-context`. Before: RevOps implementation.
- Required: no; required if sales-led or lifecycle email is primary channel.

### Workflow: Competitive Positioning Assets
- Phase: 1-analysis / 2-planning
- Trigger: Khi cần competitor profiles, alternatives pages, battlecards, sales pages.
- Steps:
  1. `step-01-define-competitor-set.md` - Confirm competitor URLs/categories and decision criteria.
  2. `step-02-profile-competitors.md` - Research positioning, pricing, features, reviews, SEO footprint.
  3. `step-03-map-differentiation.md` - Compare against own product strengths/weaknesses.
  4. `step-04-select-asset-types.md` - Alternatives page, versus page, battlecard, sales one-pager.
  5. `step-05-draft-assets.md` - Produce SEO copy + sales enablement docs.
  6. `step-06-legal-factual-review-gate.md` - Validate claims and source traceability.
- Inputs: competitor URLs, marketing context, sales objections, keyword data.
- Outputs: `competitor-profiles/`, `comparison-page-brief.md`, `battlecards.md`.
- After: `bmad-create-marketing-context`. Before: content/SEO/sales enablement execution.
- Required: no; required before public competitor comparison pages.

### Workflow: Monetization & Packaging Review
- Phase: 2-planning
- Trigger: Pricing changes, paywall redesign, upgrade funnel issues, packaging decisions.
- Steps:
  1. `step-01-capture-business-model.md` - Plans, ARPU, CAC, LTV, churn, sales motion.
  2. `step-02-research-value-metrics.md` - Value metric, personas, usage patterns, willingness-to-pay.
  3. `step-03-benchmark-competitors.md` - Pricing/packaging competitor scan.
  4. `step-04-design-package-options.md` - Tier structure, limits, features, upgrade paths.
  5. `step-05-plan-paywall-tests.md` - Paywall/upgrade hypotheses and metrics.
  6. `step-06-approval-gate.md` - User decision on pricing direction.
- Inputs: revenue metrics, product plans, competitor pricing, churn/paywall data.
- Outputs: `pricing-strategy.md`, `packaging-options.md`, `paywall-test-plan.md`.
- After: `bmad-create-marketing-context`, optionally `bmad-growth-audit`. Before: `bmad-cro-sprint` for paywall execution.
- Required: no; required before pricing changes.

### Workflow: Growth Engineering Loop
- Phase: 2-planning / 3-execution
- Trigger: Khi muốn free tool, referral program, lead magnet, pSEO asset, directory launch loop.
- Steps:
  1. `step-01-select-loop-type.md` - Free tool, referral, affiliate, pSEO, lead magnet, directory submission.
  2. `step-02-estimate-growth-mechanics.md` - Acquisition source, viral/referral coefficient, SEO potential, conversion path.
  3. `step-03-design-asset-or-loop.md` - Tool specs, incentive model, template pages, lead magnet outline.
  4. `step-04-define-technical-and-tracking-needs.md` - Engineering scope, events, dashboards, QA.
  5. `step-05-launch-and-distribute.md` - Distribution plan, directories, social/content/SEO support.
  6. `step-06-measure-and-iterate.md` - Performance review and backlog.
- Inputs: marketing context, channel constraints, engineering capacity, analytics.
- Outputs: `growth-loop-brief.md`, `technical-scope.md`, `distribution-plan.md`, `measurement-plan.md`.
- After: `bmad-marketing-strategy`. Before: implementation stories/dev work.
- Required: no.

### Workflow: AI & Programmatic Search Expansion
- Phase: 2-planning / 3-execution
- Trigger: Khi SEO strategy cần AI search visibility, pSEO, schema, or scalable pages.
- Steps:
  1. `step-01-audit-search-surface.md` - Traditional SEO, AI answers, schema, existing content.
  2. `step-02-map-query-patterns.md` - AI citation queries, pSEO patterns, competitor SERPs.
  3. `step-03-design-content-architecture.md` - Topic clusters, template pages, structured data.
  4. `step-04-build-template-and-data-plan.md` - Data fields, page templates, quality thresholds.
  5. `step-05-publish-quality-gate.md` - Thin-content, duplication, factuality, indexability checks.
  6. `step-06-monitor-visibility.md` - Rankings, citations, crawl/index, conversion.
- Inputs: site data, keyword data, product/competitor context, content inventory.
- Outputs: `ai-search-plan.md`, `pseo-template-spec.md`, `schema-plan.md`, `quality-gate.md`.
- After: `bmad-seo-sprint` or `bmad-marketing-strategy`. Before: content/dev execution.
- Required: no.

## 7. Merge Strategy high-level

### Thứ tự merge

1. Foundation: tạo `bmad-create-marketing-context`; chuẩn hóa artifact path và load pattern.
2. Config/catalog: cập nhật `module.yaml`, `module-help.csv`, `.claude-plugin/marketplace.json` cho capability mới đã chốt.
3. Agents: thêm agent domain lớn trước: CRO, Paid Media, Lifecycle, RevOps/Monetization nếu được chấp nhận.
4. Skills/references: migrate từng source skill thành menu prompt, reference file, hoặc child skill theo agent owner.
5. Workflows: thêm workflow theo thứ tự business impact: CRO Sprint, Paid Acquisition, Lifecycle Revenue, Competitive Positioning, Monetization, Growth Engineering, AI/pSEO.
6. Templates/evals: chuyển references/evals source tương ứng sau mỗi workflow, không bulk copy.
7. Docs: cập nhật README, module-help, usage examples.

### Keep / Refactor / Rewrite / Drop

| Nhóm | Quyết định | Lý do |
|---|---|---|
| Target BMAD module structure | Keep | Là khung chính đúng mục tiêu. |
| Target current agents/workflows | Keep + extend | Có persona/menu/workflow tốt. |
| Source domain content | Refactor | Nghiệp vụ tốt nhưng convention không BMAD. |
| Source `SKILL.md` frontmatter/name | Rewrite | Không dùng `bmad-*`, không có customize layer. |
| Source references | Keep curated | Giá trị cao, nhưng cần đặt đúng owner. |
| Source evals | Refactor | Cần map sang skill mới. |
| Source tools/clis | Keep as docs/reference first | Chưa nên đưa runtime vào activation. |
| Target legacy | Drop from merge path | Chỉ dùng reference; convention/language cũ. |

### Cách xử lý conflict cụ thể

- Naming: tất cả capability mới dùng `bmad-*`, không giữ source ID nguyên bản.
- Context: thay `.agents/product-marketing-context.md` bằng `{marketing_artifacts}/marketing-context.md`.
- Agent ownership: một source skill chỉ có một primary owner trong target; nếu nhiều owner, workflow điều phối thay vì duplicate.
- Workflow format: quyết định trước một chuẩn. Nếu muốn đúng prompt `step-NN-*.md`, tạo `steps/` trong từng workflow mới và sau đó refactor 6 workflow hiện có dần.
- Manifest/catalog: mọi skill mới phải thêm vào `.claude-plugin/marketplace.json` và `skills/module-help.csv`.
- Memory: xác nhận `_memory` install path trước khi thêm sidecars mới.

### Câu hỏi cần quyết định trước triển khai

1. Có muốn refactor toàn bộ workflow target sang `steps/step-NN-*.md` ngay, hay chỉ áp dụng cho workflow mới?
2. Có chấp nhận thêm 4 agent mới ngay: CRO, Paid Media, Lifecycle, RevOps/Monetization?
3. Target module tập trung SaaS web only hay cũng support mobile app/ASO?
4. Tool integrations từ `marketingskills/tools` chỉ đưa vào docs trước hay muốn runtime CLI support?
5. Evals sẽ chạy theo framework nào trong repo target?
6. Có cần giữ compatibility với source skill invocation như `/seo-audit`, hay bắt buộc đổi sang `/bmad-*`?

## Recommended next step

Chốt phạm vi merge đợt 1:

1. Foundation `bmad-create-marketing-context`.
2. Migrate SEO source into existing `bmad-seo-strategist`/`bmad-seo-sprint`.
3. Add CRO agent + CRO Sprint.
4. Add Paid Media Buyer + Paid Acquisition Sprint.

Lý do: foundation unlock toàn module; SEO là overlap dễ nhất; CRO và Paid là hai gap business-impact lớn nhất trong target hiện tại.
