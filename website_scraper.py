import requests
from bs4 import BeautifulSoup

# Get the HTML for the corresponding letter
def scrape_alphabet_page(letter = None):


    # The base URL page that we will scrape the specific cheese URLs
    url = 'https://www.cheese.com/alphabetical/'
    if isinstance(letter, str):
        url = f'https://www.cheese.com/alphabetical/?i={letter}'
    elif letter is not None:
        print("argument must be None or a letter string")
    page = requests.get(url)

    # Get the raw HTML of the web page
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

# Return a list of letters that a the name of a particular cheese included on 
# cheese.com would include
def get_letters(soup):
    alphabet_box = soup.find(id="alphabetical")

    letter_items = alphabet_box.find_all('input')

    letters = []
    for letter in letter_items:
        letters.append(letter['value'])

    return letters

# Return a list of all of the links for each type of cheese
def find_cheese_links(soup):
    # Find all of the "cheese items" on the page, which are cards that contain
    # links to a particular type of cheese
    cheese_items = soup.find_all('div', class_="cheese-item")

    cheese_links = []
    # Loop over all of the cheese items and return the page extensions
    for cheese in cheese_items:
        cheese_link = cheese.find('a')['href']
        cheese_links.append(cheese_link)

    return cheese_links