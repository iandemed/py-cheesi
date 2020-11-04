import requests
from bs4 import BeautifulSoup
from data_parser_helpers import is_pasteurized, strain_milk_data, strain_data


# Get the HTML from each individuals webpage
def get_cheese_page(cheese):
    url = f'https://www.cheese.com{cheese}'
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


# Functions to parse data on the cheese specific webpage
def find_cheese_data(soup):
    cheese_soup = soup.find("ul", class_="summary-points")
    return cheese_soup

def find_cheese_name(soup):
    cheese_header = soup.find('div', class_="unit")
    return cheese_header.h1.get_text().lower()


def create_cheese_dict(soup):
    
    cheese_soup = find_cheese_data(soup)
    cheese_ul_items = cheese_soup.find_all('li')

    cheese_dict = {}
    cheese_dict["name"] = find_cheese_name(soup)

    for item in cheese_ul_items:
        cheese_item = item.p.extract()
        cheese_string = cheese_item.get_text()

        # Initialize var_type and var_data variables
        var_type = ""
        var_data = None

        # As of 09/2020 the type of milk used to make the cheese was not entered
        # using the same format as the other relevant variables
        if is_pasteurized(cheese_string) or "milk" in cheese_string:
            var_type = "milk"
            var_data = strain_milk_data(cheese_item, cheese_string)
        else:
            cheese_list = cheese_string.split(": ")
            var_type = cheese_list[0].lower() if cheese_list[0].find("Country") == -1 else "countries"

            var_data = strain_data(cheese_list[1])
        
        cheese_dict[var_type] = var_data
    
    # Control structure to deal with "missing" data
    if cheese_dict.get('rind') is None:
        cheese_dict['rind'] = "none"
    if cheese_dict.get('colour') is None:
        cheese_dict['colour'] = "none"
    if cheese_dict.get('vegetarian') is None:
        cheese_dict['vegetarian'] = False
    if cheese_dict.get('milk') is None:
        cheese_dict['milk'] = "none"   

    return cheese_dict


# Create the cheese model from cheese dictionary
def create_cheese_model(cheese_dict):
    keys = ['name', 'rind', 'colour', 'vegetarian']
    cheese_model_dict = {x:cheese_dict[x] for x in keys}

    return cheese_model_dict

# Create milk model from cheese id and cheese dictionaries
def create_milk_models(cheese_dict, cheese_id):
    milk = cheese_dict['milk']

    milk_dicts = []
    for cheese_milk in milk:
        milk_dicts.append({"cheese_id": cheese_id, "milk": cheese_milk})

    return milk_dicts