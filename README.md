# Book Scraper

A Python project to scrape book titles and prices from an online bookstore.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [License](#license)

## Introduction
The Book Scraper is a Python application designed to extract book titles and prices from the website [Books to Scrape](http://books.toscrape.com/). The project demonstrates web scraping techniques using the `requests` and `BeautifulSoup` libraries.

## Features
- Scrapes book titles and prices from the first page of the bookstore.
- Outputs the scraped data in a readable format.
- Modular and reusable code structure for easy extension and maintenance.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book_scraper.git
    cd book_scraper
    ```

2. Install the required libraries:
    ```bash
    pip install requests
    pip install beautifulsoup4
    ```

## Usage
1. Run the `book_scraper.py` script:
    ```bash
    python book_scraper.py
    ```

2. The script will fetch and display the titles and prices of books from the specified website.

## Code Structure
- `book_scraper.py`: Main script containing the `BookScraper` class and the logic to fetch and parse book data.

### `BookScraper` Class
- `__init__(self, base_url)`: Initializes the scraper with the base URL.
- `fetch_page(self, url)`: Fetches the HTML content of the given URL.
- `parse_books(self, html_content)`: Parses the HTML content to extract book titles and prices.
- `scrape_books(self)`: Orchestrates the fetching and parsing of book data.

### `print_books` Function
- `print_books(books)`: Prints the list of books with their titles and prices.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
