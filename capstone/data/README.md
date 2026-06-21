# Data Folder

> This folder holds capstone data — both raw and processed.

## IMPORTANT: Data Hygiene

- **DO NOT commit raw data** (PII risk, file size, ethical concerns)
- `.gitignore` in the repo root excludes everything except this README
- Use **synthetic / anonymized** versions in version control
- Keep **raw data** in encrypted local storage (e.g., `~/psych-capstone-data/`)

## File Organization

```
data/
├── README.md                    ← you are here
├── data-dictionary.md           ← variable definitions
├── raw/                         ← DO NOT COMMIT
│   └── (exported survey CSVs)
├── processed/                   ← Cleaned + scored (anonymized)
│   └── analysis-ready.csv
└── codebook.md                  ← All measures + scoring keys
```

## Anonymization Checklist

Before committing any dataset:
- [ ] No email addresses
- [ ] No names
- [ ] No IP addresses
- [ ] No precise timestamps (round to day)
- [ ] No free-text responses that might identify someone
- [ ] Remove demographic combinations that could re-identify (e.g., age + job title + city)
