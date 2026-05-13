---
name: bmad-marketing-strategy
description: Orchestrate a comprehensive marketing strategy across all channels and produce a unified 90-day plan. Use when the user says "MS" or "lets build a marketing strategy".
---

# Marketing Strategy Workflow

**Goal:** Produce a unified marketing strategy spanning positioning, content, SEO, social, launches, and KPIs, culminating in an approved 90-day action plan.

**Your Role:** Workflow facilitator coordinating with the lead agent (Marketing Orchestrator) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/bullseye-channel-selection.md` — Bullseye 3-ring framework, channel-stage fit matrix, budget × stage filter, ICE scoring, sprint cycle. Required reading for Phase 2 channel selection.

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
- Use `{primary_channel}` as the default social channel for any social-media phase
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow will produce a complete marketing strategy with positioning, channel plans, a 90-day roadmap, and KPI framework — and ask any clarifying questions needed before phase 1 (e.g. business goals, budget, timeline).

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/marketing-strategy.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Discovery & Analysis

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Gather Business Context** (bmad-marketing-orchestrator) — Interview the user to capture the offering, ICP, current marketing status, goals, budget constraints, and timeline expectations. → output: `context-brief.md`
2. **Market & Competitor Analysis** (bmad-growth-analyst) — Analyze market size and trends, competitor landscape, positioning opportunities, and channel-effectiveness benchmarks. → output: `market-analysis.md`
3. **Current Marketing Audit** (bmad-growth-analyst) — Audit existing website performance, content assets, social presence, SEO standing, and email list/engagement. → output: `current-state-audit.md`

### Phase 2: Strategy Development

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Positioning & Messaging** (bmad-marketing-orchestrator) — Define unique value proposition, key messaging pillars, brand voice/tone, and competitive differentiation. → output: `positioning-strategy.md`
2. **Content Strategy** (bmad-content-architect) — Set content pillars, formats, editorial calendar framework, and distribution strategy. → output: `content-strategy.md`
3. **SEO Strategy** (bmad-seo-strategist) — Define target keyword clusters, technical SEO priorities, link-building approach, and content-gap opportunities. → output: `seo-strategy.md`
4. **Social Media Strategy** (bmad-social-media-strategist) — Plan platform prioritization, content mix per platform, engagement strategy, and community-building approach. → output: `social-strategy.md`

### Phase 3: Action Planning

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Quarterly Marketing Plan** (bmad-marketing-orchestrator) — Consolidate everything into a 90-day plan with monthly themes, key campaigns, resource allocation, and milestone targets. → output: `quarterly-plan.md`
2. **Launch & Campaign Planning** (bmad-launch-coordinator) — If applicable, plan upcoming product launches, major campaigns, and the promotional calendar. → output: `launch-calendar.md`
3. **KPIs & Metrics Framework** (bmad-growth-analyst) — Define the north-star metric, leading indicators, tracking setup, and reporting cadence. → output: `metrics-framework.md`

### Phase 4: Strategy Synthesis

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Compile Marketing Strategy** (bmad-marketing-orchestrator) — Synthesize all outputs into an executive summary, strategy overview, channel strategies, 90-day action plan, KPIs/success metrics, and budget allocation. → output: `marketing-strategy-v1.md`
2. **Strategy Review** (bmad-marketing-orchestrator) — Walk the user through key decisions, gather feedback, refine, and obtain explicit approval before activating execution workflows. → output: `strategy-approved.md` → gate: `user_approval`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest next workflows the user might run: `bmad-content-pipeline` for content execution, `bmad-seo-sprint` for the first SEO push, `bmad-social-campaign` to activate the social plan, `bmad-launch-sequence` if a major launch is in scope, `bmad-monetization-sprint` if pricing is a strategy lever, or `bmad-growth-loops-sprint` to design durable acquisition loops.
