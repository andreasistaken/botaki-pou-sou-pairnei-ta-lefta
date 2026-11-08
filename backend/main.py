import requests as req

ENDPOINT = "make-project"

data = {
    "name": "Project",
    "deadline": "27-11-2026",
    "description": "this is a very long and descriptive description of my project",
    "repo": "github.com/andreasistaken/test-repo",
    "amount": 20
}

try:
    res = req.post(url=f"http://localhost:3000/{ENDPOINT}", json=data)
    print(res.text)
except ConnectionError:
    print("Connection Error")