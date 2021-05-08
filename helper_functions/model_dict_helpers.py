import requests
from bs4 import BeautifulSoup
from helper_functions.data_parser_helpers import is_pasteurized, prepare_milk_data, prepare_data, handle_none, table_vars_to_array, handle_missing_variables
from helper_functions.website_scraper import find_cheese_data, find_cheese_name

def create_cheese_dict(soup):
    '''
    Creates a dictionary corresponding to a cheese from a cheese.com 
    webpage

        Parameters:
            soup (object): A data object representing a webpage that 
            was parsed with the BeautifulSoup module

        Return:
            cheese_dict (dict): A dictionary containing information 
            on a particularcheese
    '''

    cheese_soup = find_cheese_data(soup)
    cheese_ul_items = cheese_soup.find_all('li')

    cheese_dict = {}
    cheese_dict["name"] = find_cheese_name(soup)


    # Loop over all of the cheese characteristics (or items) that are contained 
    # in the list item tags
    for item in cheese_ul_items:
        cheese_item = item.p.extract()
        item_string = cheese_item.get_text()

        var_type = ""
        var_data = None

        # As of 09/2020 the type of milk used to make the cheese was not entered
        # using the same format as the other relevant variables
        if "Made from" in item_string:
            cheese_dict["milk"] = prepare_milk_data(cheese_item)
        else:
            item_list = item_string.split(": ")
            var_type = item_list[0].lower() if item_list[0].find(
                "Country") == -1 else "countries"

            cheese_dict[var_type] = table_vars_to_array(
                var_type, prepare_data(item_list[1]))

    return handle_missing_variables(cheese_dict)


# Create the cheese model from cheese dictionary
def create_cheese_model_dict(cheese_dict):
    '''
    Converts the cheese_dict dictionary into a dictionary that 
    can be used to create the Cheese model specified in our Flask 
    PostgreSQL database
    '''

    keys = ['name', 'rind', 'colour', 'vegetarian']
    cheese_model_dict = {x: cheese_dict[x] for x in keys}

    return cheese_model_dict


def create_milk_model_dicts(cheese_dict, cheese_id):
    '''
    Converts the cheese_dict dictionary into a dictionary that 
    can be used to create the Milk model specified in our Flask 
    PostgreSQL database
    '''

    milk = cheese_dict['milk']

    milk_dicts = []
    for cheese_milk in milk:
        if 'none' in cheese_milk:
            break
        else:
            milk_dicts.append({"cheese_id": cheese_id, "milk": cheese_milk})

    return milk_dicts


def create_texture_model_dicts(cheese_dict, cheese_id):
    '''
    Converts the cheese_dict dictionary into a dictionary that 
    can be used to create the Texture model specified in our Flask 
    PostgreSQL database
    '''

    textures = cheese_dict['texture']

    texture_dicts = []
    for cheese_texture in textures:
        texture_dicts.append(
            {"cheese_id": cheese_id, "texture": cheese_texture})

    return texture_dicts
