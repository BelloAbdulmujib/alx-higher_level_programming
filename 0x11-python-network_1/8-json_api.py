#!/usr/python3
"""script that takes in a letter and sends a POST request /
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


def search_user_by_letter(letter):
    base_url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}

    try:
        response = requests.post(base_url, params=params)
        response_json = response.json()

        if response_json:
            user_id = response_json.get("id")
            user_name = response_json.get("name")
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter_arg = sys.argv[1]
    else:
        letter_arg = ""

    search_user_by_letter(letter_arg)
