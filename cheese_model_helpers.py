import requests
from bs4 import BeautifulSoup
from data_parser_helpers import is_pasteurized, prepare_milk_data, prepare_data, handle_none, table_vars_to_array, handle_missing_variables


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
            cheese_dict["milk"] = prepare_milk_data(cheese_item, cheese_string)
        else:
            cheese_list = cheese_string.split(": ")
            var_type = cheese_list[0].lower() if cheese_list[0].find(
                "Country") == -1 else "countries"

            cheese_dict[var_type] = table_vars_to_array(
                var_type, prepare_data(cheese_list[1]))

    return handle_missing_variables(cheese_dict)


# Create the cheese model from cheese dictionary
def create_cheese_model(cheese_dict):
    keys = ['name', 'rind', 'colour', 'vegetarian']
    cheese_model_dict = {x: cheese_dict[x] for x in keys}

    return cheese_model_dict


def create_milk_models(cheese_dict, cheese_id):
    milk = cheese_dict['milk']

    milk_dicts = []
    for cheese_milk in milk:
        milk_dicts.append({"cheese_id": cheese_id, "milk": cheese_milk})

    return milk_dicts


def create_texture_models(cheese_dict, cheese_id):
    textures = cheese_dict['texture']

    texture_dicts = []
    for cheese_texture in textures:
        texture_dicts.append(
            {"cheese_id": cheese_id, "texture": cheese_texture})

    return texture_dicts
