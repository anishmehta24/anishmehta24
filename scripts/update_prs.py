"""Refresh the 'latest pull requests' block in README.md from the GitHub search API."""
import json
import os
import re
import urllib.request

USER = "anishmehta24"
START, END = "<!-- PRS:START -->", "<!-- PRS:END -->"

req = urllib.request.Request(
    f"https://api.github.com/search/issues?q=is:pr+author:{USER}+-user:{USER}&sort=created&order=desc&per_page=6",
    headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"},
)
items = json.load(urllib.request.urlopen(req))["items"]

lines = []
for it in items:
    repo = it["repository_url"].split("/repos/")[1]
    if it.get("pull_request", {}).get("merged_at"):
        state = "merged"
    elif it["state"] == "closed":
        state = "closed"
    else:
        state = "open"
    title = it["title"].replace("|", "\|")
    lines.append(f"| [{repo}](https://github.com/{repo}) | [{title}]({it['html_url']}) | `{state}` |")

block = "\n".join(["| Repository | Pull request | Status |", "|---|---|---|", *lines])
readme = open("README.md", encoding="utf-8").read()
new = re.sub(f"{re.escape(START)}.*?{re.escape(END)}", f"{START}\n{block}\n{END}", readme, flags=re.S)
if new != readme:
    open("README.md", "w", encoding="utf-8", newline="\n").write(new)
    print("README updated")
else:
    print("no change")
