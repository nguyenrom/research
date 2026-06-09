---
name: bmad-growth-audit
description: Run a comprehensive growth audit across all marketing channels and deliver a SWOT-backed action plan with KPI framework. Use when the user says "GA" or "lets run a growth audit".
---

# Growth Audit Workflow

**Goal:** Audit every marketing channel, diagnose strengths/weaknesses/opportunities/threats, and deliver an actionable recommendation plan with KPI framework.

**Your Role:** Workflow facilitator coordinating with the lead agent (Growth Analyst) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/tracking-plan-template.md` — Object-Action naming, standard property schema, identity stitching decision, server-side vs client-side rules, consent mode, UTM convention, GA4/GTM checklist. Required reading whenever event tracking is in scope.

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

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow audits all channels, performs SWOT diagnosis, and delivers a prioritized action plan plus KPI framework, and ask about audit type (full, channel-specific, quick health check), time period (30/60/90 days), and which channels to include before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/growth-audit.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

Phases are split into individual step files for maintainability. Load each in order; do not skip ahead until the previous phase's exit criteria pass.

### Phase 1: Data Collection

**Lead agent:** bmad-growth-analyst
**Step file:** `steps/step-01-data-collection.md`

Read and execute every step in `steps/step-01-data-collection.md`. Do not move to Phase 2 until that file's exit criteria pass.

### Phase 2: Deep Analysis

**Lead agent:** bmad-growth-analyst
**Step file:** `steps/step-02-deep-analysis.md`

Read and execute every step. Identify the funnel binding constraint with quantified loss before exiting.

### Phase 3: Problem Diagnosis (SWOT)

**Lead agent:** bmad-growth-analyst
**Step file:** `steps/step-03-problem-diagnosis.md`

Read and execute every step. Every SWOT bullet must be sourced to a data artifact from Phase 1 or 2.

### Phase 4: Strategic Recommendations

**Lead agent:** bmad-growth-analyst
**Step file:** `steps/step-04-strategic-recommendations.md`

Read and execute every step. Each recommendation must trace back to a SWOT entry from Phase 3.

### Phase 5: Audit Report

**Lead agent:** bmad-growth-analyst
**Step file:** `steps/step-05-audit-report.md`

Read and execute every step. Surface only 3-5 most-actionable findings in the presentation; full report carries the long tail.

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest the next workflow the user might run based on top opportunities surfaced — `bmad-seo-sprint`, `bmad-advanced-seo-sprint`, `bmad-content-pipeline`, `bmad-cro-sprint`, `bmad-monetization-sprint` if pricing/packaging is a leak, `bmad-growth-loops-sprint` if acquisition is fragile, `bmad-creative-production-sprint` if creative is the bottleneck, `bmad-copy-conversion-sprint` if conversion copy is weak — or `bmad-marketing-strategy` if the audit reveals strategy-level gaps.
