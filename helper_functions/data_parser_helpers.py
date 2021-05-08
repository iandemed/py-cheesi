
from bs4 import BeautifulSoup

# ---- Milk specific functions for data parsing ----

# The milk data has two things that we are interested in:
#   1. the pasteurization
#   2. the type of milk
# we need to parse through and extract 2. from anchor tags and make sure 1. is 
# included in the returned data.
#
# Used to determine if the p-tag passed in corresponds to the type of milk, if 
# we were to use unpasteurized it would be too specifc. Only the type of milk 
# should mention pazteurization

def is_pasteurized(str_item):
    '''
    Takes in a string and returns a boolean for whether it contains pasteurized
    '''
    if (str_item.find("pasteurized") != -1):
        return True
    else:
        return False


def is_unpasteurized(str_item):
    '''
    Takes in a string and returns a boolean for whether it contains unpasteurized
    '''
    if (str_item.find("unpasteurized") != -1):
        return True
    else:
        return False


def prepare_milk_data(cheese_item):
    '''
    The type of milk used to make a cheese is not entered in the same 
    format as the other relevant variables inlcluded on the webpage, 
    requiring a seperate function to process the milk data speficially

    Parameters:
        cheese_item (object): A BeautfiulSoup list item tag
        item_string (str): A string representation of the 
            BeautfiulSoup list item tag

    Return:
        milk_list (list): A list of strings corresponding to each
            milk that could be used to create the cheese
    '''

    milk_list = []
    milk_types = cheese_item.find_all('a')

    for milk_type in milk_types:
        milk_list.append(milk_type.get_text())

    return milk_list

#---- General purpose functions ----

def prepare_data(item_string):
    '''
    Converts string associated with a specific cheese charateristic 
    and returns a list of string values associated with each
    charateristic (ex. ['mild', 'milky', 'salty'] for flavours)
    '''

    # Split properties that have a string with a list into arrays
    if ' and ' in item_string:
        cheese_data_list = item_string.replace(',', '').strip().split(' ')
        cheese_data_list.remove('and')
    else:
        cheese_data_list = item_string.strip().split(', ')

        if len(cheese_data_list) == 1:
            cheese_data_list = ''.join(cheese_data_list)
        elif cheese_data_list is None:
            cheese_data_list = handle_none(cheese_data_list)

    if 'yes' in cheese_data_list:
        return True
    elif 'no' in cheese_data_list:
        return False
    else:
        return cheese_data_list


def handle_none(var_type):
    if var_type == "vegetarian":
        return False
    else:
        return "none"


def table_vars_to_array(var_type, var_data):
    '''
    Returns a list or str of data depending on whether it belongs to a select 
    few categories (i.e. flavour, texture, type, aroma, countries)

        Parameters:
            var_type (str): A string indicating which variable the respective 
                data belongs too
            var_data (str): The data belonging to the corresponding column

        Returns:
            var_data (list): A list of data


    Any cheese may have a 0 to n combinations of the above properties. 
    Instead of saving every variable as a list, I thought it would make more 
    sense to single out the specific variables that have this kind of variety
    and add them to seperate table
    '''

    tables_array = ['flavour', 'texture', 'type', 'aroma', 'countries']

    if isinstance(var_data, str) and var_type in tables_array:
        return [var_data]
    else:
        return var_data


def handle_missing_variables(cheese_dict):
    '''
    Returns a revised cheese dictionary that contains necessary columns with 
    "none" replacing missing data

        Parameters:
            cheese_dict (dict): A dictionary containing scraped cheese.com data

        Returns:
            cheese_dict (dict): A revised dictionary that contains necessary 
            columns to post to PostgreSQL
    '''

    cheese_vars = ['name', 'rind', 'colour', 'vegetarian', 'milk', 'flavour', 'texture', 'type', 'aroma', 'countries']

    for cheese_var in cheese_vars:
        if cheese_dict.get(cheese_var) is None:
            cheese_dict[cheese_var] = table_vars_to_array(cheese_var, handle_none(cheese_var))

    return cheese_dict
