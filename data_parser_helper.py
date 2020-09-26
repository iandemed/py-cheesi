
from bs4 import BeautifulSoup

# The milk data has two things that we are interested in:
#   1. the pasteurization
#   2. the type of milk
# we need to parse through and extract 2. from a tags and make
# sure 1. is included in the returned data

def is_pasturized(str_item):
    pasteurization = ["pasteurized", "unpasteurized"]
    if (str_item in pasteurization):
        return True
    else:
        return False

# Extract the name of each of the variables that are used to describe a cheese
def strain_data_type(cheese_item):

    cheese_txt = cheese_item.get_text()

    colon_index = cheese_txt.find(":")
    if colon_index != -1:
        
        cheese_type = cheese_txt[:colon_index].lower()

        # As of 09/2020, the variable for country was country of origin, is
        #   a) a bit of misnomer since more than 1 country can be listed
        #   b) two is a bit long for a variable name since one can assume that
        #   any included country would be the country of origin
        if cheese_type.find("country") != -1:
            return "countries"
        else:
            return cheese_type

    # As of 09/2020 the type of milk used to make the cheese was not entered
    # using the same format as the other relevant variables
    elif cheese_txt.find("milk"):
        return "milk"