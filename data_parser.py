
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
# we need to parse through and extract 2. from a tags and make sure 1. is included in the 
# returned data

def strain_milk_data(cheese_item, cheese_string):

    milk_list = []
    milk_types = cheese_item.find_all('a')
    pasteurization = "unpasteurized" if is_unpasteurized(cheese_string) else "pasteurized"

    for milk_type in milk_types:
        milk_list.append(pasteurization + " " + milk_type.get_text())

    return milk_list


def strain_data(cheese_string):

    if ' and ' in cheese_string:
        cheese_data_list = cheese_string.replace(',', '').strip().split(' ')
        cheese_data_list.remove('and')
    else:
        cheese_data_list = cheese_string.strip().split(', ')
        if len(cheese_data_list) == 1:
                cheese_data_list = ''.join(cheese_data_list)

    if 'yes' in cheese_data_list:
        return True
    elif 'no' in cheese_data_list:
        return False
    else:
        return cheese_data_list