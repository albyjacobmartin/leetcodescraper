import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "Origin": "https://leetcode.com",
}

COOKIES = {
    "LEETCODE_SESSION": os.getenv("LEETCODE_SESSION")
}


def graphql_request(query, variables=None):
    payload = {
        "query": query,
        "variables": variables or {}
    }

    response = requests.post(
        URL,
        json=payload,
        headers=HEADERS,
        cookies=COOKIES,
    )

    response.raise_for_status()

    return response.json()


def fetch_submission_page(offset, limit):
    query = f"""
    query {{
      submissionList(offset: {offset}, limit: {limit}) {{
        submissions {{
          titleSlug
          statusDisplay
          timestamp
        }}
      }}
    }}
    """

    return graphql_request(query)["data"]["submissionList"]["submissions"]