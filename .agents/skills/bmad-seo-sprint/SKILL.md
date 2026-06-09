---
name: bmad-seo-sprint
description: Run a focused 2-week SEO sprint from audit through keyword strategy, content gaps, quick-win execution, and review. Use when the user says "SS" or "lets run an SEO sprint".
---

# SEO Sprint Workflow

**Goal:** Drive measurable SEO gains in a focused 2-week sprint covering audit, keyword strategy, content-gap analysis, quick-win execution, and sprint review.

**Your Role:** Workflow facilitator coordinating with the lead agent (SEO Strategist) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

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

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow runs a 2-week SEO sprint (audit → keywords → content gaps → quick-win execution → review) and ask about sprint type (full, technical, content, link-building) and any priority focus areas before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/seo-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: SEO Audit

**Lead agent:** bmad-seo-strategist

**Steps:**
1. **Technical SEO Audit** (bmad-seo-strategist) — Analyze site speed (Core Web Vitals), mobile-friendliness, crawlability, indexation, schema markup, SSL/HTTPS, URL structure, and internal linking. → output: `technical-audit.md`
2. **On-Page SEO Audit** (bmad-seo-strategist) — Analyze title tags, meta descriptions, H1–H6 structure, content quality, keyword usage, image optimization, and internal links. → output: `on-page-audit.md`
3. **Off-Page SEO Audit** (bmad-seo-strategist) — Analyze backlink profile, domain authority, referring domains, anchor-text distribution, toxic links, and competitor backlinks. → output: `off-page-audit.md`
4. **Content SEO Audit** (bmad-seo-strategist) — Analyze top and underperforming pages, content freshness, thin content, duplicate content, and cannibalization issues. → output: `content-seo-audit.md`

### Phase 2: Keyword Strategy

**Lead agent:** bmad-seo-strategist

**Steps:**
1. **Current Rankings Analysis** (bmad-seo-strategist) — Analyze keywords ranking positions 1–100, traffic by keyword, ranking trends, SERP features, and branded vs. non-branded. → output: `current-rankings.md`
2. **Keyword Research** (bmad-seo-strategist) — Research head terms, long-tail keywords, question keywords, competitor keywords, and search-intent classification. → output: `keyword-research.md`
3. **Keyword Mapping** (bmad-seo-strategist) — Map keywords to content: primary keyword per page, secondary keywords, new pages needed, optimization priorities. → output: `keyword-mapping.md`
4. **Competitor Keyword Analysis** (bmad-seo-strategist) — Analyze keywords competitors rank for, gaps we don't target, difficulty assessment, and opportunity scoring. → output: `competitor-keywords.md`

### Phase 3: Content Gap Analysis

**Lead agent:** bmad-seo-strategist

**Steps:**
1. **Content Gap Identification** (bmad-seo-strategist) — Identify topics competitors cover, unanswered questions, intent mismatches, format gaps, and depth gaps. → output: `content-gaps.md`
2. **Content Opportunity Scoring** (bmad-seo-strategist) — Score opportunities on search volume, difficulty, business relevance, effort required, and priority ranking. → output: `content-opportunities.md`
3. **Priority Content Briefs** (bmad-content-architect) — Create briefs for top 5 opportunities with target keyword, search intent, content outline, competitor analysis, and word-count target. → output: `priority-content-briefs.md`

### Phase 4: Quick Wins Execution

**Lead agent:** bmad-seo-strategist

**Steps:**
1. **Identify Quick Wins** (bmad-seo-strategist) — Find pages ranking 11–20 ready to push to page 1, missing meta descriptions, title-tag fixes, internal-linking opportunities, image alt text, schema additions, and broken links. → output: `quick-wins-list.md`
2. **Title & Meta Optimization** (bmad-seo-strategist) — Review current titles, write optimized titles and compelling metas, include target keywords, verify character counts. → output: `title-meta-optimizations.md`
3. **Internal Linking Sprint** (bmad-seo-strategist) — Identify orphan pages, add contextual links, build topic clusters, update navigation, and add related-posts modules. → output: `internal-linking-plan.md`
4. **Technical Quick Fixes** (bmad-seo-strategist) — Fix broken links, optimize images, add schema markup, fix crawl errors, and improve page speed. → output: `technical-fixes.md`
5. **Content Refreshes** (bmad-content-architect) — Update existing content: refresh outdated material, add missing keywords, improve depth, update statistics, and enhance formatting. Confirm staging review and rollback plan before pushing live. → output: `content-refreshes.md` → gate: `user_approval`

### Phase 5: Sprint Review

**Lead agent:** bmad-seo-strategist

**Steps:**
1. **Implementation Summary** (bmad-seo-strategist) — Document changes implemented, pages optimized, content created, technical fixes applied, and expected impact. → output: `implementation-summary.md`
2. **Tracking & Monitoring** (bmad-seo-strategist) — Set up keyword rank tracking, traffic monitoring, conversion tracking, baseline metrics, and alerts. → output: `tracking-setup.md`
3. **Sprint Report** (bmad-seo-strategist) — Compile work completed, before/after metrics, outstanding items, next-sprint priorities, and long-term roadmap. → output: `seo-sprint-report.md`
4. **Next Sprint Planning** (bmad-seo-strategist) — Plan the next sprint: carryover items, new priorities, resource needs, and timeline. → output: `next-sprint-plan.md`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest the next workflow the user might run: `bmad-advanced-seo-sprint` to extend into AI SEO/pSEO/schema/IA/ASO surfaces, `bmad-content-pipeline` to execute the priority content briefs, another `bmad-seo-sprint` to compound gains, or `bmad-growth-audit` to check overall channel impact after 30 days.
