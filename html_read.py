import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
content = response.text
#print(content)


soup = BeautifulSoup(content, "html.parser")
anchors = soup.find_all("a")
scores = [int(score.get_text().split(" ")[0]) for score in soup.find_all("span", class_="score")]
print(scores)
"""
n = 1
for anchor in anchors:
    print(f"{n}. {anchor.get_text()} - {anchor.get('href')}")
    n += 1
"""
