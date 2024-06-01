# book_scraper.py

import requests
from bs4 import BeautifulSoup

class BookScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None

    def parse_books(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        book_elements = soup.find_all('article', class_='product_pod')
        books = []

        for book in book_elements:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            books.append({'title': title, 'price': price})

        return books

    def scrape_books(self):
        html_content = self.fetch_page(self.base_url)
        if html_content:
            books = self.parse_books(html_content)
            return books
        return []

def print_books(books):
    for book in books:
        print(f"Title: {book['title']}, Price: {book['price']}")

if __name__ == "__main__":
    base_url = "http://books.toscrape.com/"
    scraper = BookScraper(base_url)
    books = scraper.scrape_books()
    print_books(books)
