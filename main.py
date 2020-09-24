import requests
from bs4 import BeautifulSoup

# The base URL page that we will scrape the specific cheese URLs
URL = 'https://www.cheese.com/alphabetical/?i=a'
page = requests.get(URL)

# Get the raw HTML of the web page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all of the "cheese items" on the page, which are cards that contain
# links to a particular type of cheese
cheese_items = soup.find_all('div', class_="cheese-item")

# Loop over all of the cheese items and return the page extensions
for cheese in cheese_items:
    cheese_link = cheese.find('a')['href']
    print(cheese_link)