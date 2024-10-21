import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.base_url = "https://gdz.ru"

    def _get_html(self, url):
        return requests.get(url).content

    def _get_soup(self, html):
        return BeautifulSoup(html, "html.parser")

    def get_items_by_grade(self, grade):
        page = self._get_html(self.base_url)
        soup = self._get_soup(page)
        sr = soup.select_one(f".sidebar__main > div:nth-child(1) > ul:nth-child({grade})")
        return [link.get("href") for link in sr.find_all("a") if link.get("href") is not None]


if __name__ == "__main__":
    fish = Parser()
    available_items = fish.get_items_by_grade(9)
    print(available_items[0])
