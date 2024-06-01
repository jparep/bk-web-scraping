# web_scraping_example.py

import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    # Send a request to the website
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    # Parse the HTML content
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract book titles and prices
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        print(f'Title: {title}, Price: {price}')

if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    scrape_books(url)
