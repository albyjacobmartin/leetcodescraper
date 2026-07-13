import os
import requests
from dotenv import load_dotenv

load_dotenv()

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")

URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "Origin": "https://leetcode.com",
}

COOKIES = {
    "LEETCODE_SESSION": LEETCODE_SESSION
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

    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        print(response.text)
        raise