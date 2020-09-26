import requests
from bs4 import BeautifulSoup
from data_parser_helper import is_pasturized, strain_data_type

def get_cheese_page(cheese):
    url = f'https://www.cheese.com{cheese}'
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def find_cheese_data(soup):
    cheese_soup = soup.find("ul", class_="summary-points")
    return cheese_soup



def create_cheese_dict(cheese_soup):
    cheese_ul_items = cheese_soup.find_all('li')

    for item in cheese_ul_items:
        cheese_item = item.p.extract()
        print(strain_data_type(cheese_item))


soup = get_cheese_page('/abbaye-de-belloc/')
cheese_soup = find_cheese_data(soup)

create_cheese_dict(cheese_soup)