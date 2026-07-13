from api import graphql_request
from collections import defaultdict
from datetime import datetime

# -----------------------------
# Fetch all submissions
# -----------------------------

offset = 0
latest = {}

while True:
    query = f"""
    query {{
      submissionList(offset: {offset}, limit: 20) {{
        submissions {{
          title
          titleSlug
          statusDisplay
          timestamp
        }}
      }}
    }}
    """

    result = graphql_request(query)

    submissions = result["data"]["submissionList"]["submissions"]

    if not submissions:
        break

    for submission in submissions:
        if submission["statusDisplay"] != "Accepted":
            continue

        slug = submission["titleSlug"]
        timestamp = int(submission["timestamp"])

        if slug not in latest or timestamp > latest[slug]:
            latest[slug] = timestamp

    offset += 20

print(f"\nUnique solved problems: {len(latest)}")

# -----------------------------
# Group by date
# -----------------------------

daily = defaultdict(int)

for timestamp in latest.values():
    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    daily[date] += 1

# -----------------------------
# Print cumulative summary
# -----------------------------
import csv

running_total = 0

with open("summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Date", "Completed Today", "Total Completed"])

    for day_number, date in enumerate(sorted(daily.keys()), start=1):
        completed_today = daily[date]
        running_total += completed_today

        print(
            f"Day {day_number} - {date} - +{completed_today} - Total: {running_total}"
        )

        writer.writerow(
            [day_number, date, completed_today, running_total]
        )

print("\nSaved to summary.csv")