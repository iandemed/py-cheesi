import requests
from bs4 import BeautifulSoup

def scrape_alphabet_page(letter = None, page_num = 1):
    '''
    Returns a soup object containing the HTML from the first 
    alphabetical list page coresponding to a specific letter 
    passed into the function
    '''

    # The base URL page that we will scrape the specific cheese URLs
    url = 'https://www.cheese.com/alphabetical/'
    if isinstance(letter, str):
        url = f'https://www.cheese.com/alphabetical/?per_page=20&i={letter}&page={page_num}'
    elif letter is not None:
        print("argument must be None or a letter string")
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def get_cheese_page(cheese):
    '''
    Returns soup object containing HTML from a specific cheese's
    webpage
    '''
    url = f'https://www.cheese.com{cheese}'
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def get_letters(soup):
    '''
    Return a list of letters that contain a cheese from cheese.com
    '''
    alphabet_box = soup.find(id="alphabetical")

    letter_items = alphabet_box.find_all('input')

    letters = []
    for letter in letter_items:
        letters.append(letter['value'])

    return letters

def get_numbers(soup):
    '''
    Return the highest number page in order to loop over the entirety of the page
    ''' 
    page_list = soup.find(id="id_page")
    return int(page_list.find_all('input')[-1]['value'])

def find_cheese_links(soup):
    '''
    Return a list of cheese urls given a soup object that
    contains a list of cheeses
    '''
    # Find all of the "cheese items" on the page, which are cards that contain
    # links to a particular type of cheese
    cheese_items = soup.find_all('div', class_="cheese-item")

    cheese_links = []
    # Loop over all of the cheese items and return the page extensions
    for cheese in cheese_items:
        cheese_link = cheese.find('a')['href']
        cheese_links.append(cheese_link)

    return cheese_links

#---- Functions to parse data on specific cheese webpage ----

def find_cheese_data(soup):
    '''
    Takes a soup object corresponding to the full cheese web-page 
    and returns a soup object containing only the characteristics of
    the cheese
    '''
    cheese_soup = soup.find("ul", class_="summary-points")
    return cheese_soup


def find_cheese_name(soup):
    '''
    Takes a soup object and returns a string corresponding to
    the name of the cheese
    '''
    cheese_header = soup.find('div', class_="unit")
    return cheese_header.h1.get_text().lower()