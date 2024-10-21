import requests
from bs4 import BeautifulSoup
from typing import List


class Parser:
    def __init__(self):
        self.base_url = "https://gdz.ru"

    def _get_html(self, url):
        return requests.get(url).content

    def _get_soup(self, html):
        return BeautifulSoup(html, "html.parser")

    def get_subjects_by_grade(self, grade: int) -> List[str]:
        page = self._get_html(self.base_url)
        soup = self._get_soup(page)

        sctr = soup.select_one(f".sidebar__main > div:nth-child(1) > ul:nth-child({grade})")
        return [link.get("href") for link in sctr.find_all("a") if link.get("href") is not None]

    def get_textbook_by_subject(self, url: str) -> List[str]:
        new_url = self.base_url + url
        page = self._get_html(new_url)
        soup = self._get_soup(page)

        sctr = soup.select("ul.book__list > li.book__item > a.book__link")
        return [sr.get("href") for sr in sctr]

    def get_solved_task_img(self, url: str) -> List[str]:
        new_url = self.base_url + url
        page = self._get_html(new_url)
        soup = self._get_soup(page)

        sctr = soup.find_all("img")
        img_path = [sr.get("src") for sr in sctr if sr.get("src") and "/images/task" in sr.get("src")]
        return ["https:" + url for url in img_path]


if __name__ == "__main__":
    fish = Parser()
    available_items = fish.get_subjects_by_grade(9)
    available_books = fish.get_textbook_by_subject(available_items[2])
    img_link = fish.get_solved_task_img(available_books[1] + "15-nom")
    print(available_items[0])
    print(available_books)
    print(img_link)
