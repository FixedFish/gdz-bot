import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, link):
        self.url = link
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_items_by_grade(self, grade):
        ul_element = self.soup.select_one(f'.sidebar__main > div:nth-child(1) > ul:nth-child({grade})')
        hrefs = [link.get('href') for link in ul_element.find_all('a')]
        for href in hrefs:
            print(href)


if __name__ == '__main__':
    url = 'https://gdz.ru'
    parser = Parser(url)
    parser.get_items_by_grade(4)
