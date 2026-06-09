# Growth Playbook

> SaaS benchmarks, formulas, dashboard templates, and best practices for Pixel Metrics.
> For experiment design (hypothesis, ICE, MDE, sample size, decision rules), load `bmad-cro-sprint/references/experiment-design.md` — that file is the canonical source. This playbook only carries SaaS-stage benchmarks and formulas.

---

## SaaS Benchmarks by Stage

### Pre-PMF (0–$10K MRR)

| Metric | Acceptable | Good | Excellent |
|--------|------------|------|-----------|
| Monthly Churn | <15% | <10% | <7% |
| Activation Rate | >20% | >30% | >40% |
| NPS | >0 | >20 | >40 |
| Time to Value | <7 days | <3 days | <1 day |
| DAU/MAU | >10% | >15% | >20% |

**North Star focus:** Product-market fit signals (retention, engagement).
**Secondary KPIs:** Activation rate, time to value, user feedback score.

### PMF ($10K–$100K MRR)

| Metric | Acceptable | Good | Excellent |
|--------|------------|------|-----------|
| Monthly Churn | <8% | <5% | <3% |
| Net Revenue Retention | >90% | >100% | >110% |
| CAC Payback | <18 months | <12 months | <6 months |
| LTV/CAC | >2x | >3x | >5x |
| Activation Rate | >30% | >40% | >50% |

**North Star focus:** Revenue growth × retention balance.
**Secondary KPIs:** MRR growth, expansion revenue, churn cohorts.

### Scale ($100K+ MRR)

| Metric | Acceptable | Good | Excellent |
|--------|------------|------|-----------|
| Annual Churn | <10% | <7% | <5% |
| Net Revenue Retention | >100% | >110% | >120% |
| CAC Payback | <12 months | <9 months | <6 months |
| LTV/CAC | >3x | >4x | >6x |
| Rule of 40 | >30% | >40% | >50% |

**North Star focus:** Efficient growth (Rule of 40).
**Secondary KPIs:** NRR, CAC efficiency, channel mix.

---

## Essential Formulas

### Revenue metrics

```
MRR = Σ (Monthly recurring revenue from all customers)

ARR = MRR × 12

Net MRR Change = New MRR + Expansion MRR − Churned MRR − Contraction MRR

MRR Growth Rate = (MRR_current − MRR_previous) / MRR_previous × 100
```

### Retention metrics

```
Monthly Churn Rate = (Customers lost this month / Customers at start of month) × 100

Revenue Churn = (MRR lost this month / MRR at start of month) × 100

Net Revenue Retention (NRR) = ((MRR_start + Expansion − Contraction − Churn) / MRR_start) × 100

Gross Revenue Retention (GRR) = ((MRR_start − Contraction − Churn) / MRR_start) × 100
```

### Unit economics

```
Customer Acquisition Cost (CAC) = Total Sales & Marketing Spend / New Customers Acquired

Lifetime Value (LTV) = ARPU × Gross Margin % × (1 / Monthly Churn Rate)

LTV/CAC Ratio = LTV / CAC

CAC Payback (months) = CAC / (ARPU × Gross Margin %)

Magic Number = (QoQ ARR Growth) / (Previous Quarter S&M Spend)
```

### Engagement metrics

```
DAU/MAU = Daily Active Users / Monthly Active Users

Activation Rate = Users who complete key action / Total signups × 100

Feature Adoption = Users using feature / Total active users × 100

Time to Value = Median time from signup to first value moment
```

### Growth metrics

```
Rule of 40 = Revenue Growth Rate % + Profit Margin %

Quick Ratio = (New MRR + Expansion MRR) / (Churned MRR + Contraction MRR)

Burn Multiple = Net Burn / Net New ARR
```

---

## Funnel Benchmarks (B2B SaaS)

### Top of funnel

| Stage | Median | Top quartile |
|-------|--------|--------------|
| Visitor → Lead | 2–3% | 5%+ |
| Lead → MQL | 30–40% | 50%+ |
| MQL → SQL | 40–50% | 60%+ |

### Bottom of funnel

| Stage | Median | Top quartile |
|-------|--------|--------------|
| SQL → Opportunity | 50–60% | 70%+ |
| Opportunity → Close | 20–30% | 40%+ |
| Trial → Paid | 15–25% | 30%+ |
| Freemium → Paid | 2–5% | 8%+ |

### PLG-specific

| Stage | Median | Top quartile |
|-------|--------|--------------|
| Signup → Activation | 20–30% | 40%+ |
| Activation → Paid | 5–10% | 15%+ |
| Free → Team Plan | 10–15% | 25%+ |

---

## Dashboard Templates

### Weekly growth dashboard

```
═══════════════════════════════════════════════
WEEKLY GROWTH REPORT — Week of [DATE]
═══════════════════════════════════════════════

📊 NORTH STAR
┌─────────────────────────────────────────────┐
│ [Metric Name]: [Value]                      │
│ WoW: [+/-X%] | vs Target: [+/-X%]           │
└─────────────────────────────────────────────┘

💰 REVENUE
┌─────────────┬─────────┬─────────┬──────────┐
│ Metric      │ This Wk │ Last Wk │ WoW      │
├─────────────┼─────────┼─────────┼──────────┤
│ MRR         │ $XXX    │ $XXX    │ +X%      │
│ New MRR     │ $XXX    │ $XXX    │ +X%      │
│ Expansion   │ $XXX    │ $XXX    │ +X%      │
│ Churn       │ $XXX    │ $XXX    │ -X%      │
└─────────────┴─────────┴─────────┴──────────┘

🎯 FUNNEL
┌─────────────┬─────────┬─────────┬──────────┐
│ Stage       │ Volume  │ Conv %  │ vs Bench │
├─────────────┼─────────┼─────────┼──────────┤
│ Visitors    │ XXX     │ -       │ -        │
│ Signups     │ XXX     │ X%      │ +/-X%    │
│ Activated   │ XXX     │ X%      │ +/-X%    │
│ Paid        │ XXX     │ X%      │ +/-X%    │
└─────────────┴─────────┴─────────┴──────────┘

🔬 EXPERIMENTS IN FLIGHT
• [Test name]: Day X/Y, [current result]
• [Test name]: Day X/Y, [current result]

⚠️ ALERTS
• [Issue requiring attention]

✅ ACTIONS THIS WEEK
1. [Action item]
2. [Action item]
```

### Monthly cohort analysis

```
COHORT RETENTION (% of users still active)
═══════════════════════════════════════════════

         M0    M1    M2    M3    M4    M5    M6
Jan     100%   45%   38%   35%   33%   32%   31%
Feb     100%   48%   40%   36%   34%   33%   -
Mar     100%   50%   42%   38%   35%   -     -
Apr     100%   52%   44%   40%   -     -     -
May     100%   55%   46%   -     -     -     -
Jun     100%   58%   -     -     -     -     -
Jul     100%   -     -     -     -     -     -

Trend: ▲ Improving (M1 retention +13pp vs 6 months ago)
```

---

## Analytics Stack Recommendations

### Pre-PMF (keep it simple)

| Function | Tool | Why |
|----------|------|-----|
| Product analytics | Mixpanel free / Amplitude free | Event tracking, funnels |
| Web analytics | Plausible / Fathom | Privacy-friendly, simple |
| Session recording | Hotjar free | Understand user behavior |
| Dashboards | Google Sheets | Free, flexible |

### PMF (add depth)

| Function | Tool | Why |
|----------|------|-----|
| Product analytics | Mixpanel / Amplitude | Full feature set |
| Revenue analytics | ProfitWell / ChartMogul | Subscription metrics |
| BI layer | Metabase / Mode | Custom queries |
| CDP | Segment / Rudderstack | Data unification |

### Scale (enterprise grade)

| Function | Tool | Why |
|----------|------|-----|
| Data warehouse | Snowflake / BigQuery | Central source of truth |
| ETL | Fivetran / Airbyte | Automated pipelines |
| BI | Looker / Tableau | Advanced visualization |
| Experimentation | Statsig / Eppo | Rigorous A/B testing |

---

## Red Flags & Warning Signs

### Revenue
- MRR growth declining 3+ consecutive months.
- Churn rising while acquisition is flat.
- Expansion revenue < 20% of new revenue.
- CAC rising without LTV improvement.

### Engagement
- DAU/MAU declining steadily.
- Time to value getting longer.
- Feature adoption flat despite launches.
- Support tickets / user trending up.

### Funnel
- Top of funnel shrinking while costs are stable.
- Conversion rates declining across stages.
- Sales cycle lengthening.
- Win rate dropping.

### Data quality
- > 10% of events with null critical properties.
- Significant discrepancies between tools (GA4 vs. Mixpanel vs. server logs).
- Tracking gaps in critical user journeys.
- No documented event taxonomy (load `bmad-growth-audit/references/tracking-plan-template.md`).
