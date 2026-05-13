---
name: bmad-cro-sprint
description: Run a focused CRO sprint across pages, signup, onboarding, forms, popups, or paywalls. Use when the user says "CRO" or "lets run a CRO sprint".
---

# CRO Sprint Workflow

**Goal:** Diagnose conversion leaks, prioritize hypotheses, design experiments, and produce implementation-ready CRO recommendations with tracking requirements.

**Your Role:** Workflow facilitator coordinating with the CRO Strategist, Growth Analyst, Content Architect, and specialist agents as needed.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/experiment-design.md` — Hypothesis template (Because-We Believe-Will Cause-For), ICE scoring, sample-size math + MDE table, peeking-problem rule, guardrail metrics, decision rules, velocity targets, playbook entry schema. Required reading whenever an experiment is being designed.

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
- Use `{primary_channel}` as the default acquisition channel
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow diagnoses conversion leaks and produces a prioritized experiment backlog, then ask for the conversion surface, URL or flow description, baseline metric, traffic source, and goal before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/cro-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Intake & Baseline

**Lead agent:** bmad-cro-strategist

**Steps:**
1. **CRO Sprint Brief** (bmad-cro-strategist) — Capture surface type, URL/screens, target audience, primary conversion goal, traffic sources, baseline conversion rate, desired lift, constraints, and known issues. → output: `cro-sprint-brief.md`
2. **Marketing Context Check** (bmad-marketing-orchestrator) — Load `{marketing_artifacts}/marketing-context.md` if available; identify missing positioning, ICP, or proof facts that could affect recommendations. → output: `context-check.md`
3. **Measurement Readiness** (bmad-growth-analyst) — Confirm events, funnel steps, analytics access, sample size risk, and data-quality gaps. → output: `measurement-readiness.md`

### Phase 2: Diagnosis

**Lead agent:** bmad-cro-strategist

**Steps:**
1. **Value & Message Match Audit** (bmad-cro-strategist) — Audit five-second clarity, headline, offer, traffic-message match, CTA hierarchy, trust, objections, and scannability. → output: `value-message-audit.md`
2. **Friction Audit** (bmad-cro-strategist) — Audit form effort, flow steps, navigation distraction, mobile issues, page speed risk, error states, and unclear next steps. → output: `friction-audit.md`
3. **Copy Alternatives** (bmad-content-architect) — Draft alternative headlines, CTAs, proof blocks, FAQ/objection copy, and section rewrites for high-impact issues. → output: `copy-alternatives.md`

### Phase 3: Prioritization & Testing

**Lead agent:** bmad-cro-strategist

**Steps:**
1. **Hypothesis Backlog** (bmad-cro-strategist) — Convert findings into hypotheses with expected impact, evidence, primary metric, and affected surface. → output: `hypothesis-backlog.md`
2. **Experiment Design** (bmad-growth-analyst) — Define A/B or qualitative test setup, sample-size caveats, success criteria, guardrail metrics, and decision rules. → output: `experiment-plan.md`
3. **Prioritized Action Plan** (bmad-cro-strategist) — Split recommendations into Quick Wins, High-Impact Changes, and Test Ideas with impact/effort/confidence. → output: `cro-action-plan.md`
4. **Approval Gate** (bmad-cro-strategist) — Present the sprint findings and ask the user to approve the next implementation batch. → gate: `user_approval`

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing produced artifacts and approved next actions.
2. Suggest next workflows: `bmad-copy-conversion-sprint` if copy is the lever, `bmad-monetization-sprint` if paywall/pricing is the conversion break, `bmad-paid-acquisition-sprint` if traffic will be bought, or `bmad-growth-audit` to review broader funnel metrics.
