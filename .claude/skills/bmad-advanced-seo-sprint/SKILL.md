---
name: bmad-advanced-seo-sprint
description: Run advanced SEO work covering AI SEO/AEO/GEO, programmatic SEO, schema markup, site architecture, competitor/alternative pages, and ASO. Use when the user says "ASEO" or needs advanced SEO migration coverage.
---

# Advanced SEO Sprint Workflow

**Goal:** Extend the standard SEO sprint into modern discovery surfaces: AI answer engines, programmatic SEO, structured data, site architecture, competitor comparison pages, and app-store visibility.

**Your Role:** Workflow facilitator coordinating with the SEO Strategist, Content Architect, Growth Analyst, RevOps Strategist, and Launch Coordinator as needed.

## References

- `references/aso-audit-scorecard.md` — 6-dimension weighted scorecard, 3-tier brand maturity (Dominant/Established/Challenger), Apple-vs-Google indexing matrix, tier-conditional flag list. Required reading for Phase 5 step 3 (ASO Audit).

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

Execute each entry in `{workflow.activation_steps_prepend}`.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context. Load `file:` entries.

### Step 4: Load Config

Load `{project-root}/_bmad/performance-marketing/config.yaml` and resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{company_name}`, and `{marketing_artifacts}`.

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Ask which advanced surface matters most: AI answers, pSEO, schema/rich results, site architecture, competitor pages, or app-store listing.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/advanced-seo-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Discovery Surface Selection

**Lead agent:** bmad-seo-strategist

1. **Baseline & Goal** — Capture organic traffic, rankings, indexed pages, AI visibility, app-store presence, and business goal. → output: `advanced-seo-baseline.md`
2. **Surface Prioritization** — Score AI SEO, programmatic SEO, schema, IA, competitor pages, and ASO by impact, confidence, and effort. Present prioritized backlog and recommended phase order to user. → output: `advanced-seo-priorities.md` → gate: `user_approval`

### Phase 2: AI SEO / AEO / GEO

**Lead agent:** bmad-seo-strategist

1. **Citation Readiness** — Identify entity clarity, topical authority, source credibility, answerable pages, statistics, and quotable claims. → output: `ai-seo-readiness.md`
2. **Answer Assets** — Plan pages or sections optimized for direct answers, comparison, definitions, workflows, FAQs, and credible citations. → output: `answer-assets.md`
3. **AI Visibility Tracking** — Define prompts, tools, competitors, citation checks, and monitoring cadence. → output: `ai-visibility-tracking.md`

### Phase 3: Programmatic SEO & Site Architecture

**Lead agent:** bmad-seo-strategist + bmad-content-architect

1. **pSEO Opportunity Model** — Define template type, data source, keyword pattern, business relevance, uniqueness, and scale limits. → output: `programmatic-seo-model.md`
2. **Template & Data Requirements** — Specify page fields, unique copy logic, internal links, schema, indexability rules, and QA checks. → output: `pseo-template-spec.md`
3. **Site Architecture** — Map page hierarchy, navigation, URL patterns, breadcrumbs, hub/cluster structure, and internal-linking rules. → output: `site-architecture-plan.md`

### Phase 4: Structured Data & Rich Results

**Lead agent:** bmad-seo-strategist

1. **Schema Audit** — Identify required schema types: Organization, SoftwareApplication, Product, Review, FAQ, Article, Breadcrumb, HowTo, Event, or LocalBusiness. → output: `schema-audit.md`
2. **JSON-LD Plan** — Define entity IDs, required properties, validation checks, and page-level implementation rules. Validate every JSON-LD block against Google Rich Results Test and Schema.org validator before approving rollout. → output: `schema-implementation-plan.md` → gate: `schema_validation`

### Phase 5: Competitor Pages & ASO

**Lead agent:** bmad-seo-strategist + bmad-revops-strategist

1. **Alternative / VS Page Plan** — Prioritize singular alternative, plural alternatives, direct vs, and competitor-vs-competitor pages. → output: `competitor-page-plan.md`
2. **Battlecard Bridge** — Convert public comparison findings into sales enablement guardrails. → output: `seo-sales-battlecard-bridge.md`
3. **ASO Audit** — If an app store listing exists, audit title, subtitle, keywords, screenshots, ratings/reviews, conversion path, and competitor positioning. → output: `aso-audit.md`

### Completion

Append a final **Summary** to `outputFile` with prioritized implementation backlog and next workflow: `bmad-content-pipeline`, `bmad-revops-enablement-sprint`, or `bmad-growth-audit`.

