
from helper import scrape_alphabet_page, find_cheese_links

a_soup = scrape_alphabet_page("a")

find_cheese_links(a_soup)