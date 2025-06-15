1. **Problem Definition:**
Company focus: JAEGER RDX produces high-performance respiratory protection filters like the Microgard II PFT filter, designed for use in laboratory and industrial settings to protect workers from hazardous particles, gases, and vapors.

These filters need regular replacement depending on:

- Lab activity level

- Contamination exposure

- Filter age and type

- Compliance and safety regulations

Failure to replace them on time leads to:

- Safety risks

- Operational downtime

- Failed inspections

- Unplanned costs

2. **AI's Role in Operations
**
-Identify repetitive or error-prone manual processes

- Use AI to forecast, optimize, and automate tasks

- Support decision-making with predictive analytics and KPIs

3.** Problem Statement (Framed for AI in Operations)**
"Can we build an AI-based model to forecast how many respiratory filters will need to be replaced next month in each lab, based on historical usage, environmental risk, and compliance data — to support inventory planning, reduce unplanned replacements, and improve operational performance?"

4.**High-Level Feature Brainstorming**

These features will be **simulated** to train your AI model:

| Feature                    | Why it matters                                   |
| -------------------------- | ------------------------------------------------ |
| `avg_usage_hours_per_day`  | More usage = faster wear                         |
| `contamination_level`      | Higher contamination = faster filter degradation |
| `filter_age_avg`           | Older filters are closer to end-of-life          |
| `compliance_score`         | Non-compliant labs may delay replacements        |
| `service_calls_last_month` | Indicates possible malfunctioning filters        |
| `stock_available`          | Stock level affects replacement decisions        |
| `lab_type`                 | Different labs have different usage patterns     |

---

