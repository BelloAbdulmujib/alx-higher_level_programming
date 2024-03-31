#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys


def get_commits(repository_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/\
            {repository_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print(f"Error fetching commits. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repository_name, owner_name)
