---
name: bmad-content-pipeline
description: Run a content piece end-to-end from brief through publication and performance monitoring with quality gates. Use when the user says "CP" or "lets run the content pipeline".
---

# Content Pipeline Workflow

**Goal:** Take a content idea from intake brief through approved final draft, publication, and 30-day performance review — with quality gates at brief and final-draft stages.

**Your Role:** Workflow facilitator coordinating with the lead agent (Content Architect) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/seo-content-brief-template.md` — Full brief schema, 4-stage keyword modifier matrix, 4-factor weighted scoring, searchable-vs-shareable doctrine. Required reading for Phase 1 step 3.

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

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow takes a content idea from brief to publication with quality gates, and ask which content type the user wants (blog post, long-form guide, case study, landing page, or email sequence) plus the topic/keyword and deadline before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/content-pipeline.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Content Brief

**Lead agent:** bmad-content-architect

**Steps:**
1. **Content Request Intake** (bmad-content-architect) — Capture content type, target topic/keyword, audience, business objective, desired length, and deadline. → output: `content-request.md`
2. **Keyword & Topic Research** (bmad-seo-strategist) — Research primary and secondary keywords, search intent, competitor content, and content-gap opportunities. → output: `keyword-research.md`
3. **Create Content Brief** (bmad-content-architect) — Build the detailed brief: 5 headline options, target keyword and semantics, outline (H2s/H3s), key points, internal/external link suggestions, CTA strategy, word-count target, and tone/style notes. → output: `content-brief.md`
4. **Brief Approval** (bmad-content-architect) — Present the brief to the user, validate headlines and outline, confirm direction, and obtain approval before writing begins. → gate: `user_approval`

### Phase 2: Content Creation

**Lead agent:** bmad-content-architect

**Steps:**
1. **First Draft** (bmad-content-architect) — Write the piece following the approved brief: outline, natural keyword integration, internal links, compelling intro, strong conclusion, and CTA. → output: `draft-v1.md`
2. **SEO Optimization** (bmad-seo-strategist) — Optimize the draft: meta title and description, header tags, keyword density, image alt text, schema-markup suggestions, and internal-linking audit. → output: `seo-optimizations.md`
3. **Content Revision** (bmad-content-architect) — Apply SEO feedback, polish writing, check flow and readability, and verify accuracy. → output: `draft-v2.md`
4. **Content Review** (bmad-content-architect) — Share the draft with the user, gather feedback, make revisions, and secure final approval. → gate: `user_approval` → output: `draft-final.md`

### Phase 3: Publication & Distribution

**Lead agent:** bmad-content-architect

**Steps:**
1. **Publication Preparation** (bmad-content-architect) — Final formatting, image selection brief, featured-image specs, category/tag assignment, and publication date. → output: `publish-checklist.md`
2. **Social Distribution Plan** (bmad-social-media-strategist) — Build a distribution plan with platform-specific posts, posting schedule, engagement strategy, and repurposing opportunities. → output: `distribution-plan.md`
3. **Content Publication** (bmad-content-architect) — Publish the content, submit to Search Console, share on social per the distribution plan, and notify relevant stakeholders. → output: `publication-confirmation.md`

### Phase 4: Performance Monitoring

**Lead agent:** bmad-growth-analyst

**Steps:**
1. **Initial Performance Check** (bmad-growth-analyst) — Verify analytics, note baseline metrics, and schedule the follow-up review. → output: `tracking-setup.md`
2. **30-Day Performance Review** (bmad-growth-analyst) — Analyze traffic, engagement, conversions, and SEO ranking progress; produce optimization recommendations. → output: `performance-report.md`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest the next workflow the user might run: `bmad-seo-sprint` to compound SEO impact across more pages, or `bmad-content-pipeline` again for the next piece on the calendar.
