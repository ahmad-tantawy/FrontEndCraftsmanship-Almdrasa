# Link for Planing :  https://miro.com/app/board/uXjVNPgia48=/?moveToWidget=3458764569687762051&cot=14
# project_02 Website Scrapper

# Initialize the program

import requests
from bs4 import BeautifulSoup

# Target website for data extraction
url = "https://books.toscrape.com/"

try:
    # Send a request to the target website
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

    # Specify the data to retrieve
    soup = BeautifulSoup(response.content, "html.parser")

    # Select HTML elements containing the desired information
    books = soup.find_all("article")

    # Extract and display relevant information for each book
    for book in books:
        title = book.h3.a["title"]
        rating = book.select_one("p[class*='star-rating']")["class"][1]
        print(f"Book titled '{title}' has a rating of: {rating} stars")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    # Handle the error gracefully, log it, or take appropriate action

# Conclude the program
