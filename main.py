from requests.exceptions import RequestException

from progress import (
    fetch_all_submissions,
    get_latest_accepted,
    group_by_date,
)

from report import generate_markdown


def main():

    try:

        submissions = fetch_all_submissions()

        latest = get_latest_accepted(submissions)

        daily = group_by_date(latest)

        generate_markdown(daily)

        print("✓ summary.md generated successfully.")

    except RequestException:
        print("\nError: Unable to connect to LeetCode.")
        print("Please check your internet connection and try again.")

    except RuntimeError as e:
        print(f"\nError: {e}")

        if "session" in str(e).lower():
            print("Your LEETCODE_SESSION may have expired.")

    except KeyError:
        print("\nError: LeetCode API response has changed.")
        print("The script needs to be updated.")

    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()