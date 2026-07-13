from collections import defaultdict
from datetime import datetime

from api import graphql_request

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

        # Keep only the latest Accepted submission
        if slug not in latest or timestamp > latest[slug]:
            latest[slug] = timestamp

    offset += 20

print(f"Total Problems Solved: {len(latest)}")

# -----------------------------
# Group by date
# -----------------------------

daily = defaultdict(int)

for timestamp in latest.values():
    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    daily[date] += 1

# -----------------------------
# Generate Markdown Report
# -----------------------------

running_total = 0

with open("summary.md", "w", encoding="utf-8") as file:

    file.write("# LeetCode Progress Summary\n\n")
    file.write(f"**Total Problems Solved:** {len(latest)}\n\n")
    file.write(f"**Days with Activity:** {len(daily)}\n\n")

    file.write("| Day | Date | Completed Today | Total Completed |\n")
    file.write("|----:|------------|----------------:|----------------:|\n")

    for day_number, date in enumerate(sorted(daily.keys()), start=1):
        completed_today = daily[date]
        running_total += completed_today

        print(
            f"Day {day_number} - {date} - +{completed_today} - Total: {running_total}"
        )

        file.write(
            f"| {day_number} | {date} | {completed_today} | {running_total} |\n"
        )

print("\nMarkdown report saved as summary.md")