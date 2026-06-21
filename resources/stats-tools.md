# Resources — Statistics & Data Tools (Python-Friendly Edition)

> **Updated:** June 2026 — Python elevated to co-primary tool alongside JASP, reflecting your Data Science Python certificate.

## Philosophy

Use the **right tool for the job**:
- **JASP** for quick analyses + APA-formatted output
- **R** for reproducibility + advanced stats (SEM, psychometrics)
- **Python** for your existing strengths + custom analysis + integration with AI agents

You don't need to master all three. Pick one primary + one backup.

---

## Tool 1: JASP (free, GUI) — RECOMMENDED PRIMARY FOR LEARNING

- **URL:** https://jasp-stats.org
- **Why:** Psychology's most user-friendly stats tool. Point-and-click, APA-formatted output, Bayesian options built-in.
- **Install:** macOS, Windows, Linux. ~200MB.

### JASP Workflow (Month 1+)

| Analysis | JASP Module | When |
|---|---|---|
| Descriptive stats | Descriptives | Always first |
| T-test | T-Tests | 2-group comparisons |
| ANOVA | ANOVA | 3+ group comparisons |
| Correlation | Regression → Correlation Matrix | Variable relationships |
| Chi-square | Frequencies → Contingency Tables | Categorical data |
| Regression | Regression | Prediction |
| Factor analysis | Factor | Questionnaire validation |
| Reliability (Cronbach's α) | Reliability | Scale validation |
| SEM | SEM (advanced module) | Month 5+ if needed |

---

## Tool 2: R + RStudio (free, powerful) — RECOMMENDED FOR CAPSTONE

- **URL:** https://cran.r-project.org + https://posit.co/download/rstudio-desktop/
- **Why:** Industry standard for advanced stats + reproducibility. Quarto/R Markdown for publication-quality reports.

### Key R Packages for Psychology

```r
install.packages(c(
  "psych",      # psychometrics, factor analysis, reliability
  "lavaan",     # SEM, confirmatory factor analysis
  "lme4",       # mixed-effects models
  "ggplot2",    # publication-quality plots
  "dplyr",      # data wrangling
  "tidyr",      # data tidying
  "broom",      # tidy model output
  "papaja",     # APA-style R Markdown
  "osfr",       # OSF integration
  "effectsize", # effect sizes (Cohen's d, eta-squared, etc.)
  "pwr",        # power analysis
  "corrplot"    # correlation matrices
))
```

### When to Use R vs JASP

| Task | Tool |
|---|---|
| Quick descriptives, basic tests | **JASP** (faster) |
| Reproducible analysis script | **R** (script = audit trail) |
| Custom plots for report | **R** (ggplot2) |
| Factor analysis / SEM | **R** (psych, lavaan) |
| Power analysis | **R** (pwr package) |
| Bayesian stats | **JASP** (built-in) or R (brms) |
| APA-formatted manuscript | **R** (papaja) |

---

## Tool 3: Python (you already know it) — CO-PRIMARY FOR YOUR WORKFLOW

- **Why:** Your Data Science Python certificate is a real asset. Don't abandon it for R.
- **Use cases:** Custom analysis, web scraping for survey recruitment, NLP on open-ended responses, integration with AI agents

### Key Python Packages for Psychology Stats

```bash
pip install pandas numpy scipy statsmodels pingouin matplotlib seaborn scikit-learn jupyter
```

### Package Cheat Sheet

| Package | Use |
|---|---|
| **pandas** | Data wrangling, CSV/Excel reading |
| **numpy** | Numerical computing |
| **scipy.stats** | t-test, ANOVA, chi-square, non-parametric tests |
| **statsmodels** | Regression, GLM, time series, detailed output |
| **pingouin** | Psychology-specific stats (Cronbach's α, ICC, Bayesian t-tests, effect sizes) |
| **matplotlib + seaborn** | Visualization (publication-quality with effort) |
| **scikit-learn** | ML, clustering (for subfield like psychometrics) |
| **jupyter** | Interactive notebooks for analysis |
| **factor_analyzer** | Exploratory + confirmatory factor analysis |
| **semopy** | SEM in Python (if you want to avoid R) |

### Python Quick-Start for Psych Stats

```python
import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('capstone/data/processed/analysis-ready.csv')

# Descriptives
print(df.describe())

# Cronbach's alpha
alpha, ci = pg.cronbach_alpha(df[['item1', 'item2', 'item3', 'item4', 'item5']])
print(f"Cronbach's α = {alpha:.3f} (95% CI: {ci[0]:.3f} - {ci[1]:.3f})")

# Correlation matrix with p-values
corr = pg.pairwise_corr(df, columns=['big5_O', 'big5_C', 'decision_style_analytical'])
print(corr)

# T-test
ttest = pg.ttest(df[df['group'] == 'engineer']['risk'],
                 df[df['group'] == 'non_engineer']['risk'])
print(ttest)
```

### When to Use Python vs R vs JASP

| Task | Best Tool |
|---|---|
| Quick learning + first analyses | **JASP** |
| Reproducible capstone analysis | **R** (more psych-specific packages) |
| Custom analysis (your own algorithms, web scraping, NLP) | **Python** |
| Factor analysis / SEM (advanced) | **R** (more mature packages) |
| Effect sizes + Bayesian | **JASP** or **Python (pingouin)** |
| Data wrangling | **Python (pandas)** or **R (dplyr)** — pick one |
| Publication-quality plots | **R (ggplot2)** > Python (matplotlib) |
| Integration with your AI agents | **Python** (no contest) |

### Recommended Path

- **Month 1:** JASP only (learn stats concepts)
- **Month 2:** Add R for one analysis
- **Month 3:** Add Python for one analysis
- **Month 4+:** Pick your primary based on capstone needs
- **Capstone:** Use the tool that gets you a publication-quality report fastest

---

## Survey Tools

| Tool | Free Tier | Use |
|---|---|---|
| **Google Forms** | Unlimited | Quick pilots, simple designs |
| **Qualtrics** | Limited (HKU alumni may have access) | Pro research, branching |
| **Tally.so** | Generous free | Modern, mobile-first |
| **Prolific** | Pay-per-respondent | Recruitment for capstone (better than MTurk) |

For capstone: **Qualtrics (if available) or Tally + Prolific**.

---

## Data Repositories (for practice + capstone literature)

| Repo | Content |
|---|---|
| **OSF** | https://osf.io — datasets + preregistrations |
| **Kaggle** | https://kaggle.com/datasets — search "psychology", "mental health", "personality" |
| **ICPSR** | https://icpsr.umich.edu — major social science archive |
| **UK Data Service** | https://ukdataservice.ac.uk — UK longitudinal studies |
| **AddHealth** | https://addhealth.cpc.unc.edu — adolescent health (US) |
| **MIDUS** | https://midus.wisc.edu — midlife in US |

---

## Reproducibility Stack (Month 5+)

- **RStudio Projects** — one project per analysis
- **Python virtualenv / conda** — environment isolation
- **Git** — version control for analysis scripts (this repo!)
- **OSF** — preregister capstone hypotheses
- **Quarto** — reproducible reports in R + Python (best of both worlds)
- **renv** — R package version pinning
- **pip-tools** — Python dependency pinning

---

## Power Analysis (Before Capstone)

You'll need a power analysis to justify your sample size. Use:
- **G*Power** (free, GUI, Windows/Mac) — most common in psychology
- **R `pwr` package** — for scripted power analyses
- **Python `statsmodels.stats.power`** — for programmatic

Standard targets:
- Effect size: Cohen's d = 0.5 (medium) or f² = 0.15 (medium)
- Alpha: 0.05
- Power: 0.80
- For multiple regression with 5 predictors: N ≥ 92
- For t-test (2 groups): N ≥ 64 per group
- For correlation: N ≥ 84 to detect r = 0.30
