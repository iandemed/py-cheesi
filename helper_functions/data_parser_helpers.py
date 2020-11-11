
from bs4 import BeautifulSoup

# Used to determine if the p-tag passed in corresponds to the type of milk, if we were to
# use unpasteurized it would be too specifc. Only the type of milk should mention
# pazteurization


def is_pasteurized(str_item):
    if (str_item.find("pasteurized") != -1):
        return True
    else:
        return False


def is_unpasteurized(str_item):
    if (str_item.find("unpasteurized") != -1):
        return True
    else:
        return False

# The milk data has two things that we are interested in:
#   1. the pasteurization
#   2. the type of milk
# we need to parse through and extract 2. from anchor tags and make sure 1. is included in the
# returned data


def prepare_milk_data(cheese_item, cheese_string):

    milk_list = []
    milk_types = cheese_item.find_all('a')
    pasteurization = ""
    if is_unpasteurized(cheese_string):
        pasteurization = "unpasteurized "
    elif is_pasteurized(cheese_string):
        pasteurization = "pasteurized "

    for milk_type in milk_types:
        milk_list.append(pasteurization + milk_type.get_text())

    return milk_list

# General purpose function to parse a variety of columns


def prepare_data(cheese_string):

    # Split properties that have a string with a list into arrays
    if ' and ' in cheese_string:
        cheese_data_list = cheese_string.replace(',', '').strip().split(' ')
        cheese_data_list.remove('and')
    else:
        cheese_data_list = cheese_string.strip().split(', ')

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
    # Any cheese may have 0 to n of any combination of the following properties,
    # instead of saving every variable as an array I thought it would make more
    # sense to single out the specific variables that have this kind of variety
    tables_array = ['flavour', 'texture', 'type', 'aroma', 'countries']

    if isinstance(var_data, str) and var_type in tables_array:
        return [var_data]
    else:
        return var_data


def handle_missing_variables(cheese_dict):
    cheese_vars = ['name', 'rind', 'colour', 'vegetarian', 'milk',
                   'flavour', 'texture', 'type', 'aroma', 'countries']

    for cheese_var in cheese_vars:
        if cheese_dict.get(cheese_var) is None:
            cheese_dict[cheese_var] = table_vars_to_array(cheese_var, handle_none(cheese_var))

    return cheese_dict
