
from helper import scrape_alphabet_page, find_cheese_links, get_letters

a_soup = scrape_alphabet_page()


print(get_letters(a_soup))
print(find_cheese_links(a_soup))