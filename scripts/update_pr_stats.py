#!/usr/bin/env python3
"""Regenerate the merged-pull-request counts in README.md from the GitHub API.

Counts only pull requests merged into repositories someone else owns, since a
merge into your own repository is not external review and should not inflate
the number a recruiter reads.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"
USER = os.environ.get("PR_STATS_USER", "aryanputta")
QUERY = f"is:pr author:{USER} is:merged archived:false"
START = "<!-- pr-stats:start -->"
END = "<!-- pr-stats:end -->"

# Display grouping. Several orgs are better known by their project name, and a
# few belong under one parent. Anything absent falls back to the org name with
# a neutral logo, so a merge into a new org still renders without a code change.
GROUPS = {
    "NVIDIA": ("NVIDIA", "nvidia"),
    "ai-dynamo": ("Dynamo", "nvidia"),
    "IBM": ("IBM", "ibm"),
    "microsoft": ("Microsoft", "microsoft"),
    "deepspeedai": ("Microsoft", "microsoft"),
    "huggingface": ("HuggingFace", "huggingface"),
    "Dao-AILab": ("FlashAttention", "pytorch"),
    "linkedin": ("Liger_Kernel", "linkedin"),
    "pulumi": ("Pulumi", "pulumi"),
    "kubernetes": ("Kubernetes", "kubernetes"),
    "kubernetes-sigs": ("Kubernetes", "kubernetes"),
    "kornia": ("kornia", "python"),
    "simdutf": ("simdutf", "cplusplus"),
    "awslabs": ("AWS", "amazonaws"),
}
FALLBACK_LOGO = "github"


def api(url: str) -> dict:
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-pr-stats",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
           if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def external_repos() -> list[str]:
    """Every repo path holding a merged PR, excluding repos the user owns."""
    repos: list[str] = []
    page = 1
    while True:
        url = ("https://api.github.com/search/issues?"
               + urllib.parse.urlencode({"q": QUERY, "per_page": 100, "page": page}))
        payload = api(url)
        items = payload.get("items", [])
        for item in items:
            path = item["repository_url"].split("/repos/", 1)[1]
            if path.split("/", 1)[0].lower() != USER.lower():
                repos.append(path)
        # The search API caps out at 1000 results; stop on a short page.
        if len(items) < 100 or len(repos) >= payload.get("total_count", 0):
            return repos
        page += 1


def render(repos: list[str]) -> str:
    counts = Counter()
    for path in repos:
        org = path.split("/", 1)[0]
        label, logo = GROUPS.get(org, (org, FALLBACK_LOGO))
        counts[(label, logo)] += 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0][0].lower()))

    names = " · ".join(dict.fromkeys(label.replace("_", " ") for (label, _), _ in ranked))
    badges = "\n".join(
        f'<img src="https://img.shields.io/badge/{label}-{n}_merged-111111'
        f'?style=flat-square&logo={logo}&logoColor=C9AA71" />'
        for (label, logo), n in ranked
    )
    return (
        f"{START}\n"
        f'<div align="center">\n'
        f"<sub><b>{len(repos)} merged pull requests</b> across {names}"
        f" — inference, CUDA, CI, and ML-systems internals</sub>\n"
        f"</div>\n\n<br/>\n\n"
        f'<div align="center">\n{badges}\n</div>\n'
        f"{END}"
    )


def main() -> int:
    try:
        repos = external_repos()
    except (urllib.error.URLError, urllib.error.HTTPError) as error:
        print(f"GitHub API unreachable, leaving README unchanged: {error}", file=sys.stderr)
        return 1
    if not repos:
        print("Query returned no external merged PRs; refusing to overwrite "
              "the README with a zero count.", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print(f"Markers {START} / {END} missing from README.md", file=sys.stderr)
        return 1

    block = render(repos)
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if updated == text:
        print(f"No change. {len(repos)} merged pull requests.")
        return 0
    README.write_text(updated, encoding="utf-8")
    print(f"Updated to {len(repos)} merged pull requests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
