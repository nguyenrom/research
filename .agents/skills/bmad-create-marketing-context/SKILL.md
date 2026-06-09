---
name: bmad-create-marketing-context
description: Create or refresh the shared marketing context artifact that all performance-marketing agents use. Use when the user says "MC", "create marketing context", "set up positioning", or wants to avoid repeating product, ICP, messaging, and proof-point details.
---

# Marketing Context Foundation Workflow

**Goal:** Produce a validated shared marketing context for `{company_name}` so downstream strategy, content, SEO, social, paid, CRO, launch, and analytics work uses the same product, ICP, positioning, customer language, objections, and proof points.

**Your Role:** Workflow facilitator coordinating with the Marketing Orchestrator and relevant specialist agents.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/twelve-section-template.md` — Canonical 12-section structure for the marketing-context.md artifact (Overview / Audience / Personas / Problems / Competitive / Differentiation / Objections / Switching / Customer Language / Voice / Proof / Goals). Required reading for Phase 3.

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
- Use `{primary_channel}` as the default social channel
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow creates the shared marketing context artifact used by every performance-marketing workflow, then ask whether to auto-draft from existing project materials or interview from scratch.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/marketing-context.md`
- `summaryFile` = `{marketing_artifacts}/positioning-summary.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Context Discovery

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Check Existing Context** (bmad-marketing-orchestrator) — Look for `{marketing_artifacts}/marketing-context.md`, `.agents/product-marketing-context.md`, `.claude/product-marketing-context.md`, README files, landing-page copy, docs, and product briefs. Summarize what exists and what is missing. → output: `context-inventory.md`
2. **Product & GTM Intake** (bmad-marketing-orchestrator) — Capture one-liner, product category, product type, business model, pricing, GTM motion, primary conversion action, and current business goal. → output: `product-gtm-intake.md`
3. **Audience & Persona Intake** (bmad-marketing-orchestrator) — Capture target companies, decision makers, users, champions, financial buyers, jobs-to-be-done, primary use cases, and anti-personas. → output: `audience-intake.md`

### Phase 2: Positioning Synthesis

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Problems & Switching Forces** (bmad-marketing-orchestrator) — Capture core pain, why alternatives fall short, cost of inaction, emotional tension, push, pull, habit, and anxiety. → output: `switching-forces.md`
2. **Competitive Landscape** (bmad-growth-analyst) — Identify direct, secondary, and indirect competitors; note differentiators, weaknesses, and positioning opportunities. → output: `competitive-landscape.md`
3. **Customer Language & Proof** (bmad-content-architect) — Capture verbatim customer language, words to use/avoid, proof points, testimonials, results, logos, and claim support. → output: `customer-language-proof.md`

### Phase 3: Validation & Publishing

**Lead agent:** bmad-marketing-orchestrator

**Steps:**
1. **Draft Marketing Context** (bmad-marketing-orchestrator) — Compile the shared artifact with sections for product overview, target audience, personas, pains, competitive landscape, differentiation, objections, switching dynamics, customer language, brand voice, proof points, goals, and current metrics. → output: `marketing-context-draft.md`
2. **User Validation Gate** (bmad-marketing-orchestrator) — Present the draft, ask for corrections to facts, claims, audience, positioning, and proof. Do not publish until the user approves. → gate: `user_approval`
3. **Publish Context** (bmad-marketing-orchestrator) — Save the approved artifact to `outputFile` and a concise summary to `summaryFile`. Tell downstream agents to load `marketing-context.md` before strategic recommendations. → output: `marketing-context.md`, `positioning-summary.md`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing source materials used and decisions made.
2. Suggest next workflows: `bmad-marketing-strategy`, `bmad-cro-sprint`, `bmad-paid-acquisition-sprint`, or `bmad-seo-sprint`.
