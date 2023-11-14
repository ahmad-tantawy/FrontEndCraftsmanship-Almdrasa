import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract book titles and prices
        books = soup.find_all('h3')  # Assuming book titles are wrapped in <h3> tags
        prices = soup.find_all(class_='price_color')  # Assuming prices have the class 'price_color'

        # Print the scraped data
        for book, price in zip(books, prices):
            print(f"Book Title: {book.a.attrs['title']}")
            print(f"Price: {price.text}")
            print("-" * 40)

    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")

# URL of the website to scrape
url_to_scrape = "https://books.toscrape.com/"

# Call the function to scrape the books
scrape_books(url_to_scrape)
