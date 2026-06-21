# PSYC2061 — Advanced Quantitative Methods in Psychology

## Course Info (from HKU Catalog)

- **Code:** PSYC2061
- **Title:** Advanced quantitative methods in psychology
- **Credits:** 6
- **HKU Catalog Description:** (For psychology as a first major) This course aims to extend the learning of students from previous research method courses (e.g., PSYC1004 and PSYC2060) to cover more advanced quantitative methods used in psychological research. Students will learn to apply the quantitative methods to analyse data, interpret the results, and report the findings. The knowledge and skills acquired from this course will enable students to conduct empirical research more independently. This course also aims to enhance students' abilities to evaluate psychological research critically.
- **Prerequisites:** PSYC1001 and PSYC1004 and PSYC2060
- **Assessment:** 100% coursework
- **Notes:** Restricted to psych first majors; most advanced undergrad quant

## Learning Objectives

By the end of this course, you should be able to:

1. Apply advanced statistical methods (factor analysis, SEM intro, multilevel)
2. Conduct and interpret psychometrics
3. Use R or advanced SPSS for analysis
4. Handle complex data structures
5. Critically evaluate advanced quantitative claims
6. Plan sophisticated analyses

## Topic Outline

### Topic 1: Review of Advanced Methods (3 hours)
- ANOVA, regression recap
- Power and effect size

### Topic 2: Factor Analysis (5 hours)
- Exploratory factor analysis (EFA)
- Factor extraction and rotation
- Interpretation
- Confirmatory factor analysis (CFA) intro

### Topic 3: Psychometric Analysis (5 hours)
- Cronbach's α
- McDonald's ω
- Test-retest reliability
- Inter-rater reliability
- Item analysis

### Topic 4: Mediation and Moderation (5 hours)
- Baron & Kenny method
- Bootstrapping
- Moderation analysis
- Conditional process analysis (Hayes PROCESS)

### Topic 5: Logistic Regression (4 hours)
- Binary outcomes
- Odds ratios
- Model interpretation
- Assumptions

### Topic 6: Multilevel Modeling (5 hours)
- Nested data (e.g., students in schools)
- Random effects
- Intraclass correlation
- Basic MLM in R (`lme4`)

### Topic 7: Structural Equation Modeling (SEM) (4 hours)
- Path analysis
- Measurement models
- Structural models
- Fit indices
- SEM in R (`lavaan`)

### Topic 8: Bayesian Statistics (4 hours)
- Bayes' theorem
- Priors and posteriors
- Bayesian t-tests (JASP)
- Bayes factors
- Reporting

### Topic 9: Missing Data (3 hours)
- MCAR, MAR, MNAR
- Multiple imputation
- Full information maximum likelihood
- Sensitivity analysis

### Topic 10: Advanced Software (3 hours)
- R for advanced methods
- Quarto/R Markdown for reproducible reports
- Git for version control

## Required Resources

### Textbooks
- **Tabachnick & Fidell, "Using Multivariate Statistics"**
- **Field, "Discovering Statistics Using R"**
- **Hayes, "Introduction to Mediation, Moderation, and Conditional Process Analysis"**

### R Packages
- `psych`, `lavaan`, `lme4`, `brms`, `mice`

## Key Concepts Glossary

| Term | Definition |
|---|---|
| Factor analysis | Identifying clusters of related variables |
| EFA | Exploratory (no a priori structure) |
| CFA | Confirmatory (test a priori structure) |
| Mediation | Causal chain through third variable |
| Moderation | Effect depends on third variable |
| Multilevel modeling | Handles nested data |
| Intraclass correlation | Within-group similarity |
| Bayesian | Updates beliefs with evidence |
| Prior | Initial belief about parameter |
| Posterior | Updated belief after seeing data |
| Missing data | Incomplete observations |
| MCAR | Missing completely at random |
| MAR | Missing at random |

## Self-Check Questions

1. Conduct an EFA. How do you decide on number of factors?
2. Compute and interpret Cronbach's α for a 10-item scale.
3. Explain the difference between mediation and moderation. Use a diagram.
4. When would you use multilevel modeling?
5. Compare frequentist and Bayesian approaches to hypothesis testing.

## Capstone Connection

**Highly relevant** for advanced capstones:
- Mediation/moderation analyses
- Factor analysis of your survey
- Bayesian alternatives

**Tip:** If your capstone has nested data (e.g., multiple responses per person), use MLM.

## Progress Tracker

- [ ] Topics 1–4 completed
- [ ] Topics 5–7 completed
- [ ] Topics 8–10 completed
- [ ] EFA / CFA in R
- [ ] Self-check questions: ___/5
