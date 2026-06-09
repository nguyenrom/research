---
name: bmad-growth-loops-sprint
description: Design free tools, lead magnets, referral programs, affiliate/ambassador programs, community-led growth, and viral/product sharing loops. Use when the user says "GLS" or needs growth loops.
---

# Growth Loops Sprint Workflow

**Goal:** Design a repeatable growth loop or lead generation system that can compound beyond one campaign.

**Your Role:** Workflow facilitator coordinating with the Growth Loop Designer, Growth Analyst, Content Architect, Lifecycle Marketer, Social Media Strategist, and RevOps Strategist.

## References

- `references/loop-scorecard.md` — 7 loop types (free tool / lead magnet / referral / affiliate / ambassador / community / product sharing), 7-dimension scoring rubric, per-loop spec templates, viral-coefficient math, kill/iterate/scale rules. Required reading for Phase 1 and Phase 2.

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

Greet `{user_name}`, speaking in `{communication_language}`. Ask which loop to design first: free tool, referral, affiliate, ambassador, lead magnet, community flywheel, or product sharing loop.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/growth-loops-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Loop Selection

**Lead agent:** bmad-growth-loop-designer

1. **Opportunity Inventory** — List possible loops: free tool, referral, affiliate, ambassador, lead magnet, community, product sharing, directory/backlink, or content repurposing. → output: `growth-loop-inventory.md`
2. **Loop Scorecard** — Score each by ICP pain, distribution, repeatability, incentive quality, engineering cost, fraud risk, and measurement. Present scorecard and recommended loop selection to user before design begins. → output: `growth-loop-scorecard.md` → gate: `user_approval`

### Phase 2: Loop Design

**Lead agent:** bmad-growth-loop-designer

1. **Loop Map** — Define input -> user action -> exposed value -> new audience -> reinvestment. → output: `growth-loop-map.md`
2. **Free Tool / Lead Magnet Spec** — If selected, define job-to-be-done, format, data/input, output, capture point, SEO/social distribution, and maintenance. → output: `free-tool-lead-magnet-spec.md`
3. **Referral / Affiliate Spec** — If selected, define participants, reward structure, invite moment, fraud controls, tracking, and lifecycle messages. → output: `referral-affiliate-spec.md`
4. **Community Flywheel Spec** — If selected, define target members, rituals, roles, content loops, advocacy triggers, and moderation guardrails. → output: `community-flywheel-spec.md`

### Phase 3: Funnel & Messaging

**Lead agent:** bmad-content-architect + bmad-lifecycle-marketer

1. **Landing & Capture Copy** — Draft landing page, CTA, proof, form fields, and follow-up promise. → output: `loop-landing-copy.md`
2. **Lifecycle Follow-Up** — Define delivery, nurture, referral ask, ambassador invite, or activation follow-up. → output: `loop-lifecycle-follow-up.md`

### Phase 4: Measurement & Launch

**Lead agent:** bmad-growth-analyst

1. **Tracking Plan** — Define events, UTMs, dashboards, loop health metrics, referral/affiliate tracking, and quality checks. → output: `growth-loop-tracking.md`
2. **Launch Plan** — Define first distribution wave, owner, timeline, dependencies, risk, and kill/iterate/scale rules. Confirm tracking, support, and fraud controls are live before public launch. → output: `growth-loop-launch-plan.md` → gate: `launch_readiness`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-lifecycle-email-sprint`, `bmad-content-pipeline`, or `bmad-growth-audit` based on implementation path.

