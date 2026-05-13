---
name: bmad-revops-enablement-sprint
description: Build RevOps lifecycle, lead scoring/routing, CRM handoff, sales enablement, battlecards, one-pagers, pitch decks, and demo scripts. Use when the user says "RES" or needs RevOps/sales enablement.
---

# RevOps Enablement Sprint Workflow

**Goal:** Turn marketing demand into reliable revenue operations and seller-ready enablement assets.

**Your Role:** Workflow facilitator coordinating with the RevOps Strategist, Marketing Orchestrator, Content Architect, SEO Strategist, Lifecycle Marketer, and Growth Analyst.

## References

- `references/sales-enablement-asset-templates.md` — Concrete templates for the 9 standard assets: pitch deck (10-12 slide framework), one-pager, demo script (20-30 min flow), battlecard, objection doc (acknowledge → reframe → proof), persona card, ROI calculator, case study brief, sales playbook. Required reading for Phase 3.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the workflow block from base, team, and user customization files using BMad structural merge rules.

### Step 2: Execute Prepend Steps

Execute `{workflow.activation_steps_prepend}`.

### Step 3: Load Persistent Facts

Treat `{workflow.persistent_facts}` as foundational context. Load `file:` entries.

### Step 4: Load Config

Load `{project-root}/_bmad/performance-marketing/config.yaml` and resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{company_name}`, and `{marketing_artifacts}`.

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Ask whether the sprint should focus on lead lifecycle, scoring/routing, CRM hygiene, sales collateral, competitor battlecards, demo scripts, or pipeline reporting.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/revops-enablement-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Revenue Motion Diagnosis

**Lead agent:** bmad-revops-strategist

1. **Current Flow Map** — Map source -> lead capture -> qualification -> handoff -> sales action -> opportunity -> closed/won/lost. → output: `revenue-flow-map.md`
2. **Breakage Audit** — Diagnose lead quality, missing fields, routing gaps, SLA gaps, duplicate data, low follow-up, objection gaps, and poor sales materials. → output: `revops-breakage-audit.md`

### Phase 2: Systems Design

**Lead agent:** bmad-revops-strategist + bmad-growth-analyst

1. **Lifecycle Definitions** — Define subscriber, lead, MQL, SQL, SAL, opportunity, customer, expansion, and churn-risk criteria. → output: `lifecycle-definitions.md`
2. **Lead Scoring & Routing** — Define score signals, thresholds, routing rules, owners, SLAs, and feedback loops. Get sales-ops sign-off on thresholds and SLA before CRM rollout. → output: `lead-scoring-routing.md` → gate: `user_approval`
3. **CRM Field Spec** — Define required CRM fields, allowed values, automation triggers, data hygiene rules, and dashboards. → output: `crm-field-spec.md`

### Phase 3: Sales Enablement Assets

**Lead agent:** bmad-revops-strategist + bmad-content-architect

1. **Enablement Inventory** — Identify required assets by sales moment: discovery, demo, procurement, competitor, expansion, renewal. → output: `enablement-inventory.md`
2. **Battlecards & Comparison Assets** — Create competitor battlecards and public/private comparison asset guidance. → output: `battlecards.md`
3. **Deck / One-Pager / Demo Script** — Draft seller-ready structure and copy for the highest-priority asset. → output: `sales-enablement-assets.md`

### Phase 4: Handoff & Measurement

**Lead agent:** bmad-growth-analyst

1. **SLA & Reporting** — Define SLA dashboard, stage conversion, lead response time, pipeline created, win rate, and attribution caveats. → output: `revops-reporting.md`
2. **Implementation Backlog** — Prioritize CRM, automation, training, enablement, and data cleanup tasks. Confirm sequencing with engineering and sales leadership before kickoff. → output: `revops-implementation-backlog.md` → gate: `user_approval`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-lifecycle-email-sprint` for follow-up messaging or `bmad-customer-research-sprint` if evidence is weak.

