import requests
from bs4 import BeautifulSoup
import csv

def fetch_news():
    url = "https://news.ycombinator.com/"  # сайт для примера (Hacker News)
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select(".titleline a")

    with open("news.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Link"])
        for title in titles[:20]:   # первые 20 заголовков
            writer.writerow([title.get_text(), title.get("href")])

    print("✅ Новости сохранены в news.csv")

if __name__ == "__main__":
    fetch_news()
