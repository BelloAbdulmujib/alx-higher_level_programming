#!/usr/python3
"""script that takes your GitHub credentials (username and password) /
and uses the GitHub API to display your id
"""
import requests
import sys


def get_github_user_id(username, access_token):
    base_url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Basic {username}:{access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data.get("id")
        return user_id
    except requests.RequestException as e:
        print(f"Error fetching user ID: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python github_user_id.py <username> <access_token>")
        sys.exit(1)

    username, access_token = sys.argv[1], sys.argv[2]
    user_id = get_github_user_id(username, access_token)
    print(f"Your GitHub user ID is: {user_id}")
