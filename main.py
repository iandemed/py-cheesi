
from helper import scrape_alphabet_page, find_cheese_links, get_letters

alphabet_soup = scrape_alphabet_page()
letters = get_letters(alphabet_soup)

for letter in letters:
    letter_soup = scrape_alphabet_page(letter)
    cheeses = find_cheese_links(letter_soup)
    print(cheeses)