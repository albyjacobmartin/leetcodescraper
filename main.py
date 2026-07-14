from progress import (
    fetch_all_submissions,
    get_latest_accepted,
    group_by_date,
)

from report import generate_markdown


def main():

    print("Fetching submissions...")

    submissions = fetch_all_submissions()

    print(f"Fetched {len(submissions)} submissions.")

    print("Processing latest accepted submissions...")

    latest = get_latest_accepted(submissions)

    daily = group_by_date(latest)

    print("Generating report...")

    generate_markdown(daily)

    print()

    print(f"✓ Total Problems : {len(latest)}")
    print(f"✓ Active Days    : {len(daily)}")
    print()
    print("Report saved as summary.md")


if __name__ == "__main__":
    main()