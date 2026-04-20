import requests
import json

KEYWORDS = ["tesla", "nvidia", "ai", "xrp", "stock", "earnings"]

url = "https://www.reddit.com/r/stocks/new.json?limit=20"

headers = {"User-agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers).json()

posts = res["data"]["children"]

signals = []

for p in posts:
    title = p["data"]["title"].lower()
    link = "https://reddit.com" + p["data"]["permalink"]

    score = sum(1 for k in KEYWORDS if k in title)

    if score >= 2:
        signals.append({
            "title": p["data"]["title"],
            "score": score,
            "url": link
        })

with open("data.json", "w") as f:
    json.dump(signals, f, indent=2)

print("Signals:", len(signals))
