# book_scraper.py

import requests
from bs4 import BeautifulSoup

class BookScraper:
    """
    A class to scrape book information from an online bookstore.
    """
    def __init__(self, base_url):
        """
        Initializes the BookScraper with the base URL of the bookstore.
        
        :param base_url: str: The base URL of the bookstore.
        """
        self.base_url = base_url

    def fetch_page(self, url):
        """
        Fetches the HTML content of the given URL.
        
        :param url: str: The URL of the page to fetch.
        :return: str: The HTML content of the page, or None if an error occurs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None

    def parse_books(self, html_content):
        """
        Parses the HTML content to extract book titles and prices.
        
        :param html_content: str: The HTML content of the page.
        :return: list: A list of dictionaries containing book titles and prices.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        book_elements = soup.find_all('article', class_='product_pod')
        books = []

        # Iterate through each book element to extract title and price
        for book in book_elements:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            books.append({'title': title, 'price': price})

        return books

    def scrape_books(self):
        """
        Orchestrates the fetching and parsing of book data.
        
        :return: list: A list of dictionaries containing book titles and prices.
        """
        html_content = self.fetch_page(self.base_url)
        if html_content:
            books = self.parse_books(html_content)
            return books
        return []

def print_books(books):
    """
    Prints the list of books with their titles and prices.
    
    :param books: list: A list of dictionaries containing book titles and prices.
    """
    for book in books:
        print(f"Title: {book['title']}, Price: {book['price']}")

if __name__ == "__main__":
    # Define the base URL of the bookstore
    base_url = "http://books.toscrape.com/"
    
    # Create an instance of BookScraper
    scraper = BookScraper(base_url)
    
    # Scrape the books and print their details
    books = scraper.scrape_books()
    print_books(books)
