#!/usr/bin/env python3
"""
auto-weekly-review.py

Auto-generates a weekly review markdown file for the psych-self-study
bootcamp, prefilling objective sections (hours, wins from cron, stats)
and leaving subjective sections (mood, plan, questions, reflection) blank.

Usage:
    python3 auto-weekly-review.py                  # current week
    python3 auto-weekly-review.py --week-offset -1  # last week
    python3 auto-weekly-review.py --week-offset -2  # 2 weeks ago
    python3 auto-weekly-review.py --week-start 2026-07-13

Output:
    /app/psych-self-study-hku/progress/weekly-review-W{n}.md
    where n = ISO week number, or W{n}-retro-{date} if past weeks.
"""

import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

# ---------- Config ----------
CRON_DIR = '/home/node/.openclaw/cron/runs/'
MEM_DIR = '/app/data-intelligence-architect/memory/'
REPO_DIR = '/app/psych-self-study-hku/'
PROGRESS_DIR = os.path.join(REPO_DIR, 'progress')

JOBID_TO_NAME = {
    '96b75c9c-4bf7-4da9-b645-8a30052553e8': 'FSI',
    '5e383ae9-333e-46f9-a2b0-fb6ec61a0022': 'iStructE-Morning',
    'b402411f-9203-485a-9082-f370f68f4469': 'AIRI-Health',
    'b2ce0ea6-9edf-4688-bf1e-d7d87c6c522c': 'iStructE-2000HKT',
    'a118c5b1-6fa0-4c73-923a-888de12e4ef8': 'iStructE-Sun',
    'db268a03-3d14-446f-9c6b-285b9645c71e': 'iStructE-Mon',
    '57a039f0-3179-42c4-86ce-a17dbe2b37df': 'iStructE-Wed',
    '713d6948-d2fe-4be6-ae8d-80ec73c40a26': 'iStructE-Thr',
    'ab93c61c-9978-44f8-bb6e-14afa5a108b0': 'Bootcamp-Orch',
    '623a38d7-a64b-41f4-be10-c2ef6985c29f': 'iStructE-Evening',
    '17599b96-9606-4a10-8e0c-5e2ba28b3608': 'BME-Weekend',
    'c87fe592-9f90-455f-9ae2-3426596b5f90': 'PHYS-Weekend',
    'faa355dc-bc96-466c-950a-0f02b0100043': 'PSY-Lunch',
    '08d3c21f-938f-44a4-ae9c-7c44f840279a': 'Psych-Weekly',
}

# ---------- Date helpers ----------
def get_week_bounds(d: date):
    """Return (Monday, Sunday) of the week containing d."""
    monday = d - timedelta(days=d.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday


def get_week_number(d: date):
    """Bootcamp week number (Week 1 = Mon 22 Jun 2026 = Day 2 onwards, with
    21 Jun being Day 1)."""
    start = date(2026, 6, 21)  # Day 1 = Sunday 21 Jun 2026
    return ((d - start).days // 7) + 1


# ---------- Cron parsing ----------
def parse_cron_runs(start: date, end: date):
    """Returns day_data dict for [start, end] inclusive."""
    day_data = defaultdict(lambda: {
        'crons': set(),
        'psy_topics': [],
        'istructe_topics': [],
        'memory_notes': [],
    })

    if not os.path.isdir(CRON_DIR):
        return day_data

    for fn in os.listdir(CRON_DIR):
        if not fn.endswith('.jsonl'):
            continue
        jobid = fn[:-6]
        name = JOBID_TO_NAME.get(jobid, jobid[:8])
        path = os.path.join(CRON_DIR, fn)
        try:
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        d = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if d.get('action') != 'finished':
                        continue
                    ts = datetime.fromtimestamp(d['runAtMs'] / 1000, tz=timezone.utc)
                    day = ts.date()
                    if day < start or day > end:
                        continue
                    day_data[day]['crons'].add(name)
                    summary = (d.get('summary', '') or '').replace('\n', ' ')
                    if name == 'PSY-Lunch':
                        topic = extract_psy_topic(summary)
                        if topic:
                            day_data[day]['psy_topics'].append(topic)
                    elif name == 'iStructE-Evening':
                        topic = extract_istructe_topic(summary)
                        if topic:
                            day_data[day]['istructe_topics'].append(topic)
        except OSError:
            continue

    # Memory notes
    if os.path.isdir(MEM_DIR):
        for fn in os.listdir(MEM_DIR):
            if not fn.endswith('.md'):
                continue
            try:
                day = datetime.strptime(fn[:10], '%Y-%m-%d').date()
            except ValueError:
                continue
            if day < start or day > end:
                continue
            day_data[day]['memory_notes'].append(fn)

    return day_data


def extract_psy_topic(summary: str) -> str:
    """Extract PSY course + topic from cron summary text."""
    if 'PSYC7303' in summary:
        if 'Behavioral Genetics' in summary:
            return 'PSYC7303 Bio — Behavioral Genetics'
        if 'Neurophysiology' in summary:
            return 'PSYC7303 Bio — Neurophysiology'
        if 'Topic 3' in summary or 'Neuron & Synaptic' in summary:
            return 'PSYC7303 Bio — Neuron & Synaptic'
        if 'Topic 2' in summary or 'Neuroanatomy' in summary:
            return 'PSYC7303 Bio — Neuroanatomy'
        return 'PSYC7303 Bio'
    if 'PSYC7302' in summary:
        if 'JASP' in summary:
            return 'PSYC7302 Quant — JASP Ch 1-6'
        if 'Topics 1' in summary or 'Day 16' in summary:
            return 'PSYC7302 Quant — Descriptive stats + NHST'
        return 'PSYC7302 Quant'
    if 'PSYC7301' in summary:
        if 'Measurement' in summary or 'Reliability' in summary:
            return 'PSYC7301 — Measurement & Reliability'
        if 'Day 24' in summary or 'Survey' in summary:
            return 'PSYC7301 — Survey design'
        return 'PSYC7301'
    if 'PSYC7304' in summary or 'Perception' in summary:
        return 'PSYC7304 Cog — Perception & Attention'
    return ''


def extract_istructe_topic(summary: str) -> str:
    s = summary.lower()
    if 'concrete' in s or 'c40/50' in s:
        return 'Concrete (RC, C40/50)'
    if 'steel' in s:
        return 'Steel connections'
    if 'foundation' in s or 'seismic' in s:
        return 'Foundation/Seismic'
    if 'wind' in s:
        return 'Wind Load'
    if 'mock' in s or 'q3 2019' in s:
        return 'Q3 2019 timed mock'
    if 'q1' in s or 'q2' in s:
        return 'Past paper'
    if 'letter' in s:
        return 'Section 1(b) Letter'
    return ''


# ---------- Hour estimation ----------
def estimate_day_hours(day_info):
    crons = day_info['crons']
    hours = 0
    if 'PSY-Lunch' in crons:
        hours += 0.5
    if any(c.startswith('iStructE') for c in crons):
        hours += 1.5
    if 'BME-Weekend' in crons:
        hours += 6
    if 'PHYS-Weekend' in crons:
        hours += 4
    if 'FSI' in crons:
        hours += 0.3
    return hours


# ---------- Markdown generation ----------
def build_weekly_review(monday: date, sunday: date, week_num: int, day_data: dict) -> str:
    """Build the weekly review markdown."""
    total_hours = 0.0
    psy_hours = 0.0
    psy_days = []
    istructe_days = []
    bme_days = []
    phys_days = []
    fsi_days = 0
    mem_notes = []

    for i in range(7):
        d = monday + timedelta(days=i)
        info = day_data.get(d, {'crons': set(), 'psy_topics': [], 'istructe_topics': [], 'memory_notes': []})
        h = estimate_day_hours(info)
        total_hours += h
        if info['psy_topics']:
            psy_hours += 0.5
            psy_days.append((d, info['psy_topics']))
        if any(c.startswith('iStructE') for c in info['crons']):
            istructe_days.append((d, info['istructe_topics']))
        if 'BME-Weekend' in info['crons']:
            bme_days.append(d)
        if 'PHYS-Weekend' in info['crons']:
            phys_days.append(d)
        if 'FSI' in info['crons']:
            fsi_days += 1
        mem_notes.extend(info['memory_notes'])

    pct = (total_hours / 20) * 100
    pct_str = f'{pct:.0f}%'

    md = f"""# Weekly Review — Week {week_num} ({monday.strftime('%a %-d %b')} — {sunday.strftime('%a %-d %b %Y')})

> **Week of:** {monday.strftime('%a %-d %b')} — {sunday.strftime('%a %-d %b %Y')}
> **Total hours studied:** {total_hours:.1f} / 20 target ({pct_str})
> **PSY bootcamp Day {(monday - date(2026, 6, 21)).days + 1}-{(sunday - date(2026, 6, 21)).days + 1} / 180**

---

## 1. Wins 🎉
What went well this week? Be specific.

- [Auto: {len(psy_days)}/7 weekdays with PSY lunch delivery]
- [Auto: {len(bme_days)} BME weekend days, {len(phys_days)} PHYS weekend days]
- [Win 1 — fill in]
- [Win 2 — fill in]
- [Win 3 — fill in]

---

## 2. Misses 😞
What didn't happen? Why?

- [Miss 1 — Reason: ___]
- [Miss 2 — Reason: ___]

---

## 3. Learnings 🧠
What did I actually learn? (Not just "covered" — what STUCK?)

"""
    if psy_days:
        md += f"### PSY topics delivered (auto)\n"
        for d, topics in psy_days:
            md += f"- **{d.strftime('%a %-d %b')}**: {', '.join(set(topics))}\n"
        md += "\n"
    if istructe_days:
        md += f"### iStructE topics (auto)\n"
        for d, topics in istructe_days:
            if topics:
                md += f"- **{d.strftime('%a %-d %b')}**: {', '.join(set(topics))}\n"
        md += "\n"
    md += """- [Learning 1 — fill in]
- [Learning 2 — fill in]

---

## 4. Stats Check
- Hours studied: """ + f"{total_hours:.1f}" + f"""
- PSY lunch days: """ + f"{len(psy_days)}/7" + f"""
- PSY-specific hours: {psy_hours:.1f}
- BME weekend days: {len(bme_days)}
- PHYS weekend days: {len(phys_days)}
- FSI routine days: {fsi_days}/7
- Memory notes generated: {len(mem_notes)}
- Pages read: __
- Papers read: __
- Anki cards reviewed: __
- Survey responses: __

---

## 5. Next Week's Plan
Top 3 priorities (specific, achievable):

1. [Specific task 1 — e.g., "Read OpenStax Ch 3 and take notes"]
2. [Specific task 2 — e.g., "Run first JASP t-test on mental health dataset"]
3. [Specific task 3 — e.g., "Draft 3 survey items for my own survey"]

---

## 6. Mood / Energy / Health
- Mood (1–10): ___
- Energy (1–10): ___
- Sleep avg: ___ hrs
- Workout sessions: ___

> If mood/energy/sleep are consistently low → adjust study load. The plan serves you, not the other way around.

---

## 7. Open Questions / To Ask AI
- [Question 1]
- [Question 2]

---

**Reflection (1–2 sentences):**

> [How do you feel about this week? On track? Need to adjust?]
"""
    return md


def main():
    parser = argparse.ArgumentParser(description='Auto-generate weekly review for psych-self-study')
    parser.add_argument('--week-offset', type=int, default=0,
                        help='Weeks before current (negative for past, e.g., -1 = last week)')
    parser.add_argument('--week-start', type=str,
                        help='Monday of week to generate (YYYY-MM-DD)')
    parser.add_argument('--output', type=str,
                        help='Output path (default: progress/weekly-review-W{n}.md)')
    parser.add_argument('--print-only', action='store_true',
                        help='Print to stdout instead of writing file')
    args = parser.parse_args()

    if args.week_start:
        monday = datetime.strptime(args.week_start, '%Y-%m-%d').date()
    else:
        today = date.today()
        cur_monday = today - timedelta(days=today.weekday())
        monday = cur_monday + timedelta(weeks=args.week_offset)

    sunday = monday + timedelta(days=6)
    week_num = get_week_number(monday)

    day_data = parse_cron_runs(monday, sunday)
    md = build_weekly_review(monday, sunday, week_num, day_data)

    if args.print_only:
        print(md)
        return

    if args.output:
        out_path = args.output
    else:
        suffix = '' if args.week_offset == 0 else f'-retro-{monday.strftime("%Y%m%d")}'
        out_path = os.path.join(PROGRESS_DIR, f'weekly-review-W{week_num}{suffix}.md')

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        f.write(md)
    print(f'✓ Wrote: {out_path}')


if __name__ == '__main__':
    main()
