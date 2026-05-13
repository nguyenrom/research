---
name: bmad-paid-acquisition-sprint
description: Plan a paid acquisition sprint from channel selection through campaign architecture, creative matrix, tracking, launch checklist, and optimization cadence. Use when the user says "PAS" or "lets run a paid acquisition sprint".
---

# Paid Acquisition Sprint Workflow

**Goal:** Produce a paid campaign plan that connects budget, channels, audiences, offer, creative, landing page, tracking, and optimization rules before spend begins.

**Your Role:** Workflow facilitator coordinating with the Paid Media Buyer, CRO Strategist, Content Architect, Growth Analyst, and Social Media Strategist as needed.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/channel-architecture-presets.md` — Per-platform account hierarchies (Google / Meta / LinkedIn / X / TikTok), bid-strategy progression, creative requirements, learning-period sample-size requirements, cut/iterate/scale rules. Required reading for Phase 1 channel selection and Phase 2 architecture.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths (e.g. `references/guide.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory (where `customize.toml` lives).
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the `workflow` block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

1. `{skill-root}/customize.toml` — defaults
2. `{project-root}/_bmad/custom/{skill-name}.toml` — team overrides
3. `{project-root}/_bmad/custom/{skill-name}.user.toml` — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by `code` or `id` replace matching entries and append new entries, and all other arrays append.

### Step 2: Execute Prepend Steps

Execute each entry in `{workflow.activation_steps_prepend}` in order before proceeding.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context you carry for the rest of the workflow run. Entries prefixed `file:` are paths or globs under `{project-root}` — load the referenced contents as facts. All other entries are facts verbatim.

### Step 4: Load Config

Load config from `{project-root}/_bmad/performance-marketing/config.yaml` and resolve:
- Use `{user_name}` for greeting
- Use `{communication_language}` for all communications
- Use `{document_output_language}` for output documents
- Use `{company_name}` as the SaaS being marketed
- Use `{primary_channel}` as the default channel if no channel is specified
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow builds a paid acquisition plan with tracking and launch guardrails, then ask for objective, budget, target CPA/ROAS, offer, landing page, and preferred channels before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/paid-acquisition-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Paid Strategy

**Lead agent:** bmad-paid-media-buyer

**Steps:**
1. **Paid Goal & Constraints** (bmad-paid-media-buyer) — Capture objective, budget, target CPA/ROAS, audience, geography, compliance constraints, sales cycle, offer, landing page, and current spend history. → output: `paid-goal-constraints.md`
2. **Channel Selection** (bmad-paid-media-buyer) — Evaluate Google, Meta, LinkedIn, X, TikTok, and retargeting by intent, audience fit, creative burden, cost, and funnel readiness. → output: `channel-selection.md`
3. **Landing Page Readiness** (bmad-cro-strategist) — Check message match, page speed/mobile risk, CTA, trust, objections, and conversion tracking readiness. → output: `landing-page-readiness.md`

### Phase 2: Campaign Build

**Lead agent:** bmad-paid-media-buyer

**Steps:**
1. **Campaign Architecture** (bmad-paid-media-buyer) — Define naming convention, campaign/ad set structure, audience segments, exclusions, retargeting windows, budget split, and bid strategy. → output: `campaign-architecture.md`
2. **Creative Matrix** (bmad-paid-media-buyer + bmad-content-architect) — Produce 3-5 test angles, platform-specific copy, image/video briefs, proof points, CTAs, and hypotheses. → output: `ad-creative-matrix.md`
3. **Social Platform Adaptation** (bmad-social-media-strategist) — When using social paid, adapt creative to platform culture and placement expectations. → output: `social-paid-adaptation.md`

### Phase 3: Tracking & Launch

**Lead agent:** bmad-growth-analyst

**Steps:**
1. **Tracking Plan** (bmad-growth-analyst) — Define conversion events, UTMs, pixel requirements, GA4/Mixpanel/Segment checks, attribution caveats, and dashboard metrics. → output: `paid-tracking-plan.md`
2. **Launch Checklist** (bmad-paid-media-buyer) — Verify budget, targeting, exclusions, landing page, tracking, creative specs, approvals, and rollback criteria. → gate: `launch_readiness` → output: `launch-checklist.md`
3. **Optimization Cadence** (bmad-paid-media-buyer) — Define learning period, review cadence, cut/iterate/scale rules, creative refresh plan, and reporting template. → output: `optimization-cadence.md`
4. **Approval Gate** (bmad-paid-media-buyer) — Present the complete paid acquisition plan and ask the user to approve launch or identify changes. → gate: `user_approval`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing produced artifacts and launch readiness.
2. Suggest next workflows: `bmad-creative-production-sprint` for next creative iteration batch, `bmad-cro-sprint` if the landing page is weak, or `bmad-growth-audit` after the first learning period.
