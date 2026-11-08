from typing import Union
import requests as r

from datetime import datetime

def normalizeGithubLink(link: str) -> str: 
    if "github.com" in link:
        if link.startswith("https://"):
            return link
        elif link.startswith("http://"):
            link = link[7:]
            return "https://" + link
        else:
            return "https://" + link
    else:
        return "Invalid link"


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

def TimeFormatGood(time):
        format = "%d-%m-%Y %H:%M:%S"

        try:
            datetime.strptime(time, format)
            print("True")
            return True
        except ValueError:
            print("False")
            return False



def time(date):
    class TimeLeft:
        def __init__(self, difference, days, hours, minutes, seconds):
            self.difference = difference
            self.days = days
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    date = datetime.strptime(date, "%d-%m-%Y %H:%M:%S")

    now = datetime.now()

    difference = date - now

    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60

    timer = TimeLeft(difference, days, hours, minutes, seconds)

    return timer


# checkTimeFormat("30-11-2026 22:23:24")

# repoExists("https://github.com/andreasistaken/test-repo")

# normalLink = normalizeGithubLink("http://github.com/andreasistaken/test-repo")
# print(normalLink)