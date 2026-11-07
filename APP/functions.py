from typing import Union
import requests as r

def repoExists(githubRepo: str) -> Union[bool, str]:
    if githubRepo.startswith("https://"):
        githubRepo = githubRepo[19:]
    else:
        githubRepo = githubRepo[11:]

    try:
        response = r.get(url=f"https://api.github.com/repos/{githubRepo}")
    except r.exceptions.ConnectionError:
        return "Connection error"

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        return True
    else:
        return False

repoExists("https://github.com/andreasistaken/test-repo")