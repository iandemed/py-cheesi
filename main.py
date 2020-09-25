
from dotcom_helper import scrape_alphabet_page, find_cheese_links, get_letters

# Get a list of all of the alphabetic letters included in the cheese database
alphabet_soup = scrape_alphabet_page()
letters = get_letters(alphabet_soup)

# Creat a list containing every cheese in the cheese.com database
cheese_links = []
for letter in letters:
    letter_soup = scrape_alphabet_page(letter)
    cheeses = find_cheese_links(letter_soup)
    cheese_links.extend(cheeses)