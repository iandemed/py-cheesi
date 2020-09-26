import requests
from bs4 import BeautifulSoup
from data_parser_helper import is_pasteurized, strain_milk_data

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
        cheese_string = cheese_item.get_text()

        var_type = ""
        # As of 09/2020 the type of milk used to make the cheese was not entered
        # using the same format as the other relevant variables
        if is_pasteurized(cheese_string):
            var_type = "milk"
            strain_milk_data(cheese_item, cheese_string)
        else:
            cheese_list = cheese_string.split(": ")
            var_type = cheese_list[0].lower() if cheese_list[0].find("Country") == -1 else "countries"
        
        print(var_type)


soup = get_cheese_page('/abbaye-de-belloc/')
cheese_soup = find_cheese_data(soup)

create_cheese_dict(cheese_soup)