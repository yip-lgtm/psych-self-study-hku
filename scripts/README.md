# scripts/ — Auto-generators

> Two scripts that automate weekly progress tracking using OpenClaw cron logs + memory notes.

## Files

| Script | Purpose | When to run |
|---|---|---|
| `auto-weekly-review.py` | Generate pre-filled weekly review markdown | Sunday evening 20:00 HKT |
| `auto-weekly-review.sh` | Bash wrapper (calls Python, copies to latest) | Same |

---

## Usage

### Generate current week (auto-fills past days, blanks remaining)

```bash
python3 /app/psych-self-study-hku/scripts/auto-weekly-review.py --week-offset 0
# Output: progress/weekly-review-W{N}.md
```

### Generate last week (offset -1)

```bash
python3 /app/psych-self-study-hku/scripts/auto-weekly-review.py --week-offset -1
# Output: progress/weekly-review-W{N}-retro-{YYYYMMDD}.md
```

### Generate for specific Monday

```bash
python3 /app/psych-self-study-hku/scripts/auto-weekly-review.py --week-start 2026-07-13
```

### Print to stdout (don't write file)

```bash
python3 /app/psych-self-study-hku/scripts/auto-weekly-review.py --print-only
```

---

## Auto-fill sections

| Section | Source | Manual fill? |
|---|---|---|
| Title + date range | Computed | No |
| Total hours | Cron activity estimates | ⚠️ Verify |
| Wins 🎉 | Auto-prefix only | ✅ Fill in 1-3 specific wins |
| Misses 😞 | Empty | ✅ Fill in |
| Learnings 🧠 | PSY/iStructE topics auto-extracted | ✅ Add personal reflections |
| Stats Check | Computed (cron-derived) | ✅ Fill in reading/papers/Anki |
| Next Week's Plan | Empty | ✅ Fill in 3 specific tasks |
| Mood/Energy/Health | Empty | ✅ Fill in |
| Open Questions | Empty | ✅ Fill in |
| Reflection | Empty | ✅ Fill in |

---

## Cron job

Set up a cron that fires Sunday 20:00 HKT (12:00 UTC):

```bash
openclaw cron add \
  --name "Weekly Review Generator" \
  --cron "0 12 * * 0" \
  --tz "UTC" \
  --session isolated \
  --light-context \
  --message "Trigger Weekly Review Generator. Steps:

1. Run /app/psych-self-study-hku/scripts/auto-weekly-review.sh to generate
   last week's review (offset -1).
2. Verify file written: progress/weekly-review-W{N}-retro-{YYYYMMDD}.md
3. Generate CURRENT week (offset 0): progress/weekly-review-W{N}.md
4. Read both files and send Telegram summary (≤400 chars) with:
   - Last week's hours + key PSY topics
   - Current week's hours so far (in-progress)
   - Reminder: 'Edit subjective sections (wins, mood, plan)'
5. No greeting, start with '📋 Weekly Review'." \
  --announce \
  --channel telegram \
  --to "8475453959"
```

---

## Hour estimation logic

Per-day hours from cron presence:

| Cron fired | Hours added |
|---|---|
| PSY-Lunch | +0.5 |
| Any iStructE-* | +1.5 |
| BME-Weekend | +6 |
| PHYS-Weekend | +4 |
| FSI | +0.3 |

**Caveat:** These are *upper-bound estimates* based on cron activity. Actual
study time may be lower (e.g., didn't actually read for 30 min despite
cron firing). Always verify against your own log.

---

## What to do after generation

1. **Open the file** in your editor.
2. **Fill subjective sections** (Wins / Misses / Learnings / Mood / Plan / Reflection).
3. **Verify Stats Check** — update reading/papers/Anki/survey numbers.
4. **Commit + push**:
   ```bash
   cd /app/psych-self-study-hku
   git add progress/weekly-review-W{N}*.md
   git commit -m "Fill Week N review"
   git push
   ```
