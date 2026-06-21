# PSYC7302 — Research and Quantitative Methods in Psychology

## Course Info

- **Code:** PSYC7302
- **Title:** Research and quantitative methods in psychology
- **MSocSc(Psy) Compulsory:** Yes (one of 8)
- **BPsych Equiv:** PSYC1004 + PSYC2060 (advanced)
- **Self-Study Month:** 1–5 (spine — built across all months; pairs with PSYC7301)
- **Estimated Study Hours:** 80–100 hours (advanced stats)

## Learning Objectives

By the end of this course, you should be able to:

1. Choose and apply appropriate inferential statistical tests
2. Interpret statistical output (p-values, effect sizes, confidence intervals)
3. Conduct and interpret multiple regression analyses
4. Conduct basic ANOVA (one-way, factorial)
5. Calculate and interpret effect sizes (Cohen's d, η², r²)
6. Perform power analyses to determine sample size
7. Use statistical software (JASP, R, or Python)
8. Identify violations of statistical assumptions and apply alternatives
9. Report quantitative results in APA format
10. Critically evaluate quantitative claims in published research

## Topic Outline

### Topic 1: Review of Descriptive + Inferential Basics (4 hours)
- Recap from PSYC7301
- Distributions and the normal curve
- z-scores, sampling distributions, standard error
- Logic of null hypothesis significance testing (NHST)

### Topic 2: t-Tests (8 hours)
- Independent samples t-test
- Paired samples t-test
- One-sample t-test
- Assumptions (normality, homogeneity of variance, independence)
- Effect size: Cohen's d
- Reporting: t(df) = value, p = value, d = value
- Non-parametric alternative: Mann-Whitney U, Wilcoxon

### Topic 3: ANOVA I — One-Way (8 hours)
- One-way ANOVA logic (variance partitioning)
- F-distribution
- Post-hoc tests (Tukey HSD, Bonferroni)
- Effect size: η² (eta-squared), partial η²
- Reporting: F(df_between, df_within) = value, p = value, η² = value
- Kruskal-Wallis (non-parametric alternative)

### Topic 4: ANOVA II — Factorial (8 hours)
- Factorial designs (2×2, 2×3)
- Main effects and interactions
- Visualizing interactions
- Simple effects analysis
- Effect sizes for interactions

### Topic 5: Correlation (6 hours)
- Pearson's r
- Correlation matrix
- Significance testing for r
- Effect size: r² (coefficient of determination)
- Assumptions (linearity, homoscedasticity, normality)
- Non-parametric: Spearman's rho
- Visualization: scatterplot matrix

### Topic 6: Regression I — Simple Linear (6 hours)
- Linear regression model
- Ordinary least squares (OLS)
- Interpreting coefficients (intercept, slope)
- R² (variance explained)
- Residual analysis
- Assumptions (linearity, independence, homoscedasticity, normality)

### Topic 7: Regression II — Multiple (10 hours)
- Multiple regression
- Standardized vs. unstandardized coefficients
- Multicollinearity (VIF)
- Hierarchical vs. simultaneous entry
- Model comparison
- Adjusted R²
- Reporting in APA

### Topic 8: Categorical Data Analysis (6 hours)
- Chi-square test of independence
- Chi-square goodness of fit
- Phi coefficient, Cramér's V
- Assumptions (expected frequencies ≥ 5)
- Fisher's exact test (small samples)

### Topic 9: Effect Sizes and Power (6 hours)
- Why effect sizes matter (beyond p-values)
- Cohen's conventions: small (d = 0.2, r = 0.1), medium (0.5, 0.3), large (0.8, 0.5)
- Power analysis using G*Power
- Sample size determination
- Post-hoc power (controversial — use cautiously)
- Confidence intervals as effect size info

### Topic 10: Statistical Assumptions and Violations (6 hours)
- Normality (Shapiro-Wilk, Q-Q plots)
- Homogeneity of variance (Levene's test)
- Independence (Durbin-Watson)
- Outliers (box plots, z-scores, Mahalanobis distance)
- Transformations (log, square root)
- Non-parametric alternatives

### Topic 11: Advanced Topics (8 hours)
- Logistic regression (binary outcomes)
- Factor analysis intro (EFA)
- Reliability analysis (Cronbach's α, McDonald's ω)
- Multilevel modeling intro
- Structural equation modeling (SEM) — overview only

### Topic 12: Statistical Software and Reproducibility (8 hours)
- JASP for quick analyses
- R for reproducible scripts (R Markdown / Quarto)
- Python (pingouin, statsmodels, scipy) for custom analyses
- Version control (Git) for analysis scripts
- Reporting results in APA format

## Required Resources

### Textbooks
- **"Learning Statistics with JASP"** — Navarro & Foxcroft — Chapters 7–14
- **"Statistical Methods for the Social Sciences"** — Agresti (alternative, more comprehensive)
- **"Research Methods in Psychology"** — OpenStax — Chapters 12–14

### Videos
- **StatQuest (YouTube, Josh Starmer)** — best stats explainer on the web
- **Khan Academy** — Inferential statistics
- **Coursera "Statistics with R"** (Duke)

### Software (free)
- **JASP** (jasp-stats.org) — primary tool for learning
- **R + RStudio** — for reproducible capstone analysis
- **Python** (pandas, scipy, statsmodels, pingouin) — for your Data Science workflow
- **G*Power** — for power analysis

### Key Papers (Statistical)
- Cohen (1988) — "Statistical power analysis for the behavioral sciences" (foundational)
- Wasserstein & Lazar (2016) — "The ASA's statement on p-values"
- Cumming (2014) — "The new statistics"
- Wilkinson (1999) — "Statistical methods in psychology journals"

## Key Concepts Glossary

| Term | Definition |
|---|---|
| Effect size | Standardized measure of the magnitude of an effect (independent of sample size) |
| Cohen's d | Standardized mean difference: (M1 - M2) / SD_pooled |
| η² (eta-squared) | Proportion of variance explained (for ANOVA) |
| r² | Proportion of variance explained (for correlation/regression) |
| Power (1 - β) | Probability of correctly rejecting a false null hypothesis (typically 0.80) |
| α (alpha) | Probability of Type I error (typically 0.05) |
| β (beta) | Probability of Type II error |
| Confidence interval | Range within which the true population parameter likely falls (typically 95% CI) |
| Multicollinearity | High correlation among predictors in regression (VIF > 10 problematic) |
| Homoscedasticity | Equal variance of residuals across levels of IV |
| Effect coding | Coding categorical variables as -1 and +1 (vs. dummy coding 0 and 1) |
| Interaction | The effect of one IV depends on the level of another IV |
| Non-parametric test | Statistical test that doesn't assume normal distribution (e.g., Mann-Whitney) |

## Self-Check Questions

1. A researcher compares anxiety scores across 3 therapy conditions (n=20 per group). Which test? What assumptions must be checked?
2. Explain the difference between Type I and Type II errors. Which is worse in your capstone context?
3. You get F(2, 87) = 4.32, p = .016, η² = 0.09. Interpret this fully in plain English.
4. A regression has R² = 0.15. Is this "good"? What does it mean?
5. When would you choose non-parametric over parametric tests? List 3 situations.
6. Why are effect sizes more informative than p-values alone? Give an example.
7. You're designing a study with d = 0.5, α = 0.05, power = 0.80. How many participants do you need?
8. Multiple regression with 5 predictors, R² = 0.42, adjusted R² = 0.38. Why does adjusted differ? What does this tell you?
9. A correlation matrix shows r = 0.05, p < 0.001 (n = 10,000). Is this meaningful? Why or why not?
10. Explain why "post-hoc power analysis" is problematic. What should you do instead?

## Connection to Capstone

This is the **statistical engine** of your capstone. You'll use:
- **t-test or ANOVA** to compare groups (engineer vs. non-engineer, trader vs. non-trader)
- **Correlation + regression** to predict outcomes from predictors (Big Five → decision style)
- **Reliability (Cronbach's α)** to validate your scales
- **Effect sizes** to report the magnitude of findings
- **Power analysis** to justify your sample size (in your proposal)
- **Assumption checks** to defend your methods (in your report)

**Capstone tool stack:** JASP (initial exploration) + R or Python (reproducible final analysis) — use at least 2 tools per `capstone/README.md` spec.

## Sample Discussion Questions

- A psychology paper reports F(1, 98) = 12.5, p < .001, η² = 0.11. Critically evaluate this finding.
- A colleague says "p > 0.05 means no effect." Why is this wrong? Use a confidence interval to illustrate.
- Compare and contrast: Bonferroni vs. Tukey HSD for post-hoc tests. When would you use each?
- Your regression has one significant predictor and two non-significant ones. What are 3 possible explanations?
- Why has the field moved away from purely NHST toward effect sizes + CIs? What's the philosophical shift?

## Progress Tracker

- [ ] Topics 1–2 completed
- [ ] Topics 3–4 completed
- [ ] Topics 5–7 completed
- [ ] Topics 8–10 completed
- [ ] Topics 11–12 completed
- [ ] Power analysis practiced in G*Power
- [ ] At least 1 analysis done in JASP
- [ ] At least 1 analysis done in R or Python
- [ ] Self-check questions: ___/10
- [ ] Discussion questions answered in writing
- [ ] Statistical plan written for capstone
