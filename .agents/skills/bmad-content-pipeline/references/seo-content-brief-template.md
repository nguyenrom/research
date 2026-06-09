# SEO Content Brief Template

> Reference loaded by `bmad-content-pipeline` Phase 1 step 3 (Create Content Brief). The canonical structure for every brief that goes into the writer's hands.

## Why this exists

A weak brief is the #1 cause of weak content. Writers can only ship what they're briefed on. The brief should leave zero ambiguity about: who reads this, what they want, what we promise, what the structure is, what the SEO target is, what the conversion path is.

## The brief schema

```markdown
# Brief: [Working title]

## Metadata
- **Target keyword:** [primary keyword] (volume: X, KD: Y, intent: Z)
- **Secondary keywords:** [3-7 LSI / supporting terms]
- **Search intent:** Informational / Navigational / Commercial / Transactional
- **Funnel stage:** Awareness / Consideration / Decision / Implementation
- **Target length:** [word count + range, e.g. 2,000-2,500]
- **Format:** Blog article / Pillar / Listicle / Comparison / How-to / Case study
- **Persona:** [from marketing-context.md Section 3]
- **Funnel objective:** [primary CTA — newsletter signup / demo / trial / specific download]
- **Deadline:** [date]
- **Owner:** [writer name]

## Unique angle
What makes this article different from the top 10 SERP results?
Don't ship a brief without a clear answer here. Specificity beats originality —
"a deeper take on [aspect competitors gloss over]" is enough.

## Reader promise
"After reading this article, you will [know / be able to / understand] ..."
One sentence. The reader should be able to verify whether the article delivered.

## Outline

### H1: [Optimized title — primary keyword in first 6 words]

### H2: Introduction (~200 words)
- Hook (specific number, contrarian observation, or named pain)
- Problem context (1-2 sentences)
- Promise (one line)
- "What you'll learn" preview (3-5 bullets)

### H2: [Main section 1] (~400-600 words)
- H3: Sub-point A
- H3: Sub-point B
- H3: Sub-point C
- Internal link target: [URL on our site]
- External link target: [authoritative source]

### H2: [Main section 2] (~400-600 words)
- ... same shape

### H2: [Main section 3] (~400-600 words)
- ... same shape

### H2: Conclusion + CTA (~200 words)
- Recap of 3 key points
- Primary CTA tied to funnel objective
- Secondary CTA (newsletter / related guide)

## Questions to answer (PAA)
Pulled from Google's "People Also Ask" + AnswerThePublic + customer support tickets:
1. [Q1]
2. [Q2]
3. [Q3]
4. [Q4]
5. [Q5]

## Customer language to use
From `marketing-context.md` Section 9:
- USE: [list of phrases / spellings]
- AVOID: [jargon / internal terminology]

## Proof points to include
From `marketing-context.md` Section 11:
- [Specific stat / customer / case study to cite]
- [Specific stat / customer / case study to cite]

## CTA wording
- **Primary:** "[exact button copy + destination URL]"
- **Secondary:** "[exact text + destination]"

## References / sources for the writer
- [URL 1 — what to extract]
- [URL 2 — what to extract]
- [internal doc URL]

## SEO checklist (handoff to seo-strategist for Phase 2 review)
- [ ] Primary keyword in title, H1, first 100 words, last 100 words
- [ ] Secondary keywords distributed across H2s
- [ ] Internal links to 3-5 related pieces
- [ ] External links to 1-2 authoritative sources
- [ ] Featured snippet target: [question, paragraph format, list, or table]
- [ ] Meta title: < 60 chars, ends with brand
- [ ] Meta description: < 160 chars, includes primary keyword + value prop + CTA
- [ ] Schema type: Article (or HowTo / FAQ if applicable)

## Quality bar (writer must meet before submitting)
- [ ] Every section delivers on the promise (can verify)
- [ ] Every claim has a citation OR a "based on our experience" disclaimer
- [ ] Reading level matches persona (Flesch 50-60 for B2B SaaS)
- [ ] One CTA per scroll-screen, not 5 in the same paragraph
- [ ] Skim-test: a reader can scan H2/H3/bolded only and still get value
```

## 4-stage keyword modifier matrix

For SEO sprint planning, map keywords to funnel stage by modifier:

| Funnel stage | Common modifiers | Content type |
|--------------|------------------|--------------|
| Awareness | "what is", "guide to", "definition", "intro to" | Foundational guide, definition page |
| Consideration | "best", "vs", "alternatives to", "compared to" | Comparison, listicle, review |
| Decision | "pricing", "free trial", "demo", "[brand] review" | Product page, pricing page, case study |
| Implementation | "templates", "examples", "checklist", "how to do X with Y" | Templates, tutorials, integrations |

A balanced editorial calendar covers all 4 stages. If 90% of briefs are awareness, the funnel will leak — bottom-funnel pieces are the conversion engine.

## 4-factor weighted scoring (which brief to write first)

For each candidate brief in the backlog:

| Factor | Weight | Score 1-10 |
|--------|--------|-----------|
| Customer impact (reader's job) | 40% | |
| Business fit (closeness to revenue) | 30% | |
| Search opportunity (volume × KD) | 20% | |
| Resource cost (writing + design effort) | 10% | |

`weighted_score = Σ (factor × weight)`

Sort backlog by descending weighted score. Top 5 go into the next sprint.

## Searchable vs. shareable doctrine

| Type | Purpose | Format |
|------|---------|--------|
| Searchable | Captures intent, ranks long-term | Pillar, comparison, how-to, FAQ |
| Shareable | Drives social/email mentions, links | Opinion, contrarian, deep dive, original research |

Healthy mix: ~60% searchable / ~40% shareable. Pure-searchable plans win SEO but lose mindshare; pure-shareable plans go viral but don't compound.

## Output

For each brief, save to `{marketing_artifacts}/content/briefs/<keyword-slug>.md` using this template. Track all briefs in `{marketing_artifacts}/content/brief-log.md`.

## Cross-references

- For copy editing post-draft → `bmad-copy-conversion-sprint/references/seven-sweeps.md`.
- For the 12-section marketing context → `bmad-create-marketing-context/references/twelve-section-template.md`.
