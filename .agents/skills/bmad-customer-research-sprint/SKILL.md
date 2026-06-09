---
name: bmad-customer-research-sprint
description: Run customer, ICP, VOC, JTBD, review-mining, community-mining, and competitor-profiling research to produce usable marketing context. Use when the user says "CRS" or "lets run customer research".
---

# Customer Research Sprint Workflow

**Goal:** Convert customer evidence, market signals, competitor profiles, reviews, interviews, communities, and support data into marketing context that downstream BMAD marketing agents can use.

**Your Role:** Workflow facilitator coordinating with the Marketing Orchestrator, Content Architect, SEO Strategist, Growth Analyst, and RevOps Strategist as needed.

## References

- `references/voc-mining-protocols.md` — Source inventory ranked by signal density, Reddit / G2 query patterns, frequency × intensity ranking formula, JTBD synthesis template, persona anti-pattern checklist. Required reading for Phase 2.

## Prerequisites

This workflow PRODUCES the shared marketing context (`{marketing_artifacts}/marketing-context.md`). It does not require `bmad-create-marketing-context` first — it can run in parallel with or supersede that workflow. If a marketing-context.md already exists, this workflow updates and enriches it rather than overwriting.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the `workflow` block yourself from `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/{skill-name}.toml`, and `{project-root}/_bmad/custom/{skill-name}.user.toml` using BMad structural merge rules.

### Step 2: Execute Prepend Steps

Execute each entry in `{workflow.activation_steps_prepend}` in order.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context. Load `file:` entries from `{project-root}`.

### Step 4: Load Config

Load `{project-root}/_bmad/performance-marketing/config.yaml` and resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{company_name}`, and `{marketing_artifacts}`.

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Explain that this workflow produces evidence-backed marketing context, then ask which evidence sources are available: interviews, surveys, support tickets, reviews, forums, Reddit, sales notes, CRM, competitor URLs, or existing research.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/customer-research-sprint.md`
- `contextOutput` = `{marketing_artifacts}/marketing-context.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Research Scope

**Lead agent:** bmad-marketing-orchestrator

1. **Objective & Decision** — Define the marketing decision this research must support: positioning, ICP, copy, channel strategy, churn, pricing, launch, or sales enablement. → output: `research-scope.md`
2. **Evidence Inventory** — List available sources, source quality, freshness, bias, and gaps. → output: `evidence-inventory.md`
3. **Research Plan** — Choose research mode: analyze existing assets, gather online VOC, profile competitors, or synthesize mixed evidence. Present scope and method to user before fielding. → output: `research-plan.md` → gate: `user_approval`

### Phase 2: Voice of Customer

**Lead agent:** bmad-content-architect

1. **Customer Language Mining** — Extract jobs, pains, anxieties, desired outcomes, trigger events, objections, and exact phrases. Rank themes by frequency × intensity so the loudest signals lead. Build persona sketches (and explicit persona anti-patterns). → output: `voc-mining.md`
2. **JTBD & Segments** — Group evidence into jobs-to-be-done, buyer segments, use cases, and switching triggers. → output: `jtbd-segments.md`
3. **Copy Inputs** — Convert VOC into value propositions, proof needs, objection handling, message angles, and CTA language. → output: `copy-inputs.md`

### Phase 3: Competitive Intelligence

**Lead agent:** bmad-seo-strategist + bmad-revops-strategist

1. **Competitor Profiles** — For each competitor, summarize positioning, ICP, pricing signals, feature promises, proof, traffic/channel clues, and weak spots. → output: `competitor-profiles.md`
2. **Comparison Opportunities** — Identify alternative/vs pages, sales battlecard opportunities, and competitor objections to address. → output: `comparison-opportunities.md`
3. **Market Map** — Categorize competitors and alternatives by buyer job, category frame, and switching reason. → output: `market-map.md`

### Phase 4: Synthesis

**Lead agent:** bmad-marketing-orchestrator

1. **Marketing Context Update** — Produce or update the shared context with product, ICP, positioning, objections, proof, competitive alternatives, and customer language. Present synthesis for review before publishing. → output: `marketing-context.md` → gate: `user_approval`
2. **Opportunity Backlog** — Convert findings into prioritized actions for content, SEO, CRO, paid, lifecycle, RevOps, monetization, and growth loops. → output: `research-backed-backlog.md`
3. **Evidence Confidence** — Tag each major recommendation as strong, medium, weak, or assumption. → output: `evidence-confidence.md`

### Completion

When complete, append a final **Summary** to `outputFile`, update `contextOutput`, and recommend the next workflow based on the highest-confidence opportunity.

