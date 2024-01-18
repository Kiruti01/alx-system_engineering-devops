#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        headers = {
                "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                }
        params = {
                "limit": 10
                }

        try:
            response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check for HTTP errors
         response.raise_for_status()

         # Check if "data" field is present
         if results and "children" in results:
             [print(c.get("data").get("title")) for c in results["children"]]
         else:
             print("No data found in the response.")
         else:
             print("Empty response.")
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print(f"Subreddit '{subreddit}' not found.")
            else:
                print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
