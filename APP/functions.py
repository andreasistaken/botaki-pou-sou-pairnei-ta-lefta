from typing import Union
import requests as r

def normalizeGithubLink(link: str) -> str:
    if link.startswith("https://"):
        return link
    elif link.startswith("http://"):
        link = link[7:]
        return "https://" + link
    elif not link.startswith("https://") or not link.startswith("http://"):
        return "https://" + link


def repoExists(githubRepo: str) -> Union[bool, str]:

    githubRepo = githubRepo[19:]

    try:
        response = r.get(url=f"https://api.github.com/repos/{githubRepo}")
    except r.exceptions.ConnectionError:
        return "Connection error"

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        return True
    else:
        return False

# repoExists("https://github.com/andreasistaken/test-repo")

# normalLink = normalizeGithubLink("http://github.com/andreasistaken/test-repo")
# print(normalLink)