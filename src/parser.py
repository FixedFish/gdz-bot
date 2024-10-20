import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, link):
        self.url = link
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_items_by_grade(self, grade):
        selector = self.soup.select_one(f'.sidebar__main > div:nth-child(1) > ul:nth-child({grade})')
        hrefs = [link.get('href') for link in selector.find_all('a')]
        for href in hrefs:
            print(href)

    def get_books_by_grade(self, grade, item):
        href = []
        page = requests.get(f'https://gdz.ru/class-{grade}/geometria').content
        soup = BeautifulSoup(page, 'html.parser')
        books = soup.select('li.book__item > a:nth-child(1)')
        for book in books:
            href.append(book)
        for h in href:
            print(h['href'])



if __name__ == '__main__':
    url = 'https://gdz.ru'
    parser = Parser(url)
    parser.get_items_by_grade(9)
    parser.get_books_by_grade(9, 0)
