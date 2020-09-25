import requests
from bs4 import BeautifulSoup

def get_cheese_page(cheese):
    url = f'https://www.cheese.com{cheese}'
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def find_cheese_data(soup):
    cheese_soup = soup.find("ul", class_="summary-points")
    return cheese_soup

