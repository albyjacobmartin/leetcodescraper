from collections import defaultdict
from datetime import datetime

from api import fetch_submission_page
from config import PAGE_SIZE


def fetch_all_submissions():

    submissions = []
    offset = 0

    while True:

        page = fetch_submission_page(offset, PAGE_SIZE)

        if not page:
            break

        submissions.extend(page)
        offset += PAGE_SIZE

    return submissions


def get_latest_accepted(submissions):

    latest = {}

    for submission in submissions:

        if submission["statusDisplay"] != "Accepted":
            continue

        slug = submission["titleSlug"]
        timestamp = int(submission["timestamp"])

        if slug not in latest:
            latest[slug] = timestamp
        else:
            latest[slug] = max(latest[slug], timestamp)

    return latest


def group_by_date(latest):

    daily = defaultdict(int)

    for timestamp in latest.values():

        date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        daily[date] += 1

    return dict(sorted(daily.items()))