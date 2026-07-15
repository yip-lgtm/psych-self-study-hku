#!/usr/bin/env bash
# auto-weekly-review.sh
# Wrapper: generates last week's review (since cron fires Sunday evening
# at 20:00 HKT = 12:00 UTC, we generate the week just-ended).

set -e

REPO_DIR="/app/psych-self-study-hku"
SCRIPT="${REPO_DIR}/scripts/auto-weekly-review.py"
WEEKLY_REVIEW_FILE="${REPO_DIR}/progress/weekly-review-latest.md"

echo "=== Auto-weekly-review: $(date -u '+%Y-%m-%d %H:%M:%S') UTC ==="

# Generate for the week just ended (offset -1 from current Sunday)
WEEK_NUM=$(python3 -c "
from datetime import date, timedelta
today = date.today()
# Cron fires Sunday; the week that just ended is last week
last_sunday = today - timedelta(days=today.weekday() + 1)
monday_of_last_week = last_sunday - timedelta(days=6)
print(monday_of_last_week.isocalendar()[1])
")
echo "Week number: ${WEEK_NUM}"

# Run the generator with offset -1 (previous week)
python3 "${SCRIPT}" --week-offset -1

# Also copy to a stable "latest" path
LATEST_FILE="${REPO_DIR}/progress/weekly-review-W${WEEK_NUM}-retro-$(date -u '+%Y%m%d').md"
if [ -f "${REPO_DIR}/progress/weekly-review-W${WEEK_NUM}-retro-$(python3 -c "
from datetime import date, timedelta
today = date.today()
last_sunday = today - timedelta(days=today.weekday() + 1)
monday_of_last_week = last_sunday - timedelta(days=6)
print(monday_of_last_week.strftime('%Y%m%d'))
").md" ]; then
  cp "${REPO_DIR}/progress/weekly-review-W${WEEK_NUM}-retro-$(python3 -c "
from datetime import date, timedelta
today = date.today()
last_sunday = today - timedelta(days=today.weekday() + 1)
monday_of_last_week = last_sunday - timedelta(days=6)
print(monday_of_last_week.strftime('%Y%m%d'))
").md" "${WEEKLY_REVIEW_FILE}"
fi

echo "Latest review: ${WEEKLY_REVIEW_FILE}"
echo "=== Done ==="
