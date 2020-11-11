

# Set file path to the parent directory
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from helper_functions.cheese_dict_helpers import create_cheese_dict, create_cheese_model_dict
from helper_functions.website_scraper import scrape_alphabet_page, get_letters, find_cheese_links, get_cheese_page
from app import create_app
from models import db, Cheese, Texture
from flask import jsonify, request





app = create_app()
app.app_context().push()

db.init_app(app)

# Clear ALL of the data currently in the database
Cheese.query.delete()

# Get a list of all of the alphabetic letters included in the cheese database
alphabet_soup = scrape_alphabet_page()

letters = ['a']

# Creat a list containing every cheese in the cheese.com database
cheese_links = []
for letter in letters:
    letter_soup = scrape_alphabet_page(letter)
    cheeses = find_cheese_links(letter_soup)
    cheese_links.extend(cheeses)

# Intialize the ID variable
cheese_id = 1

for cheese in cheese_links:
    soup = get_cheese_page(cheese)
    
    cheese_dict = create_cheese_dict(soup)
    cheese_model_dict = create_cheese_model_dict(cheese_dict)
    
    print(cheese_model_dict)
    new_cheese = Cheese(**cheese_model_dict)
    db.session.add(new_cheese)
    db.session.commit()

    cheese_id += 1
