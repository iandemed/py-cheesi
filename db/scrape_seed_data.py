

# Set file path to the parent directory
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from helper_functions.model_dict_helpers import create_cheese_dict, create_cheese_model_dict, create_milk_model_dicts, create_texture_model_dicts
from helper_functions.website_scraper import scrape_alphabet_page, get_letters, find_cheese_links, get_cheese_page, get_numbers
from app import create_app
from db.models import db, Cheese, Texture, Milk
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
    max_page = get_numbers(scrape_alphabet_page(letter))
    for page_num in range(1, 2):
        letter_soup = scrape_alphabet_page(letter, page_num)
        cheeses = find_cheese_links(letter_soup)
        cheese_links.extend(cheeses)

# Intialize the ID variable
cheese_id = 1

for cheese in cheese_links:
    soup = get_cheese_page(cheese)
    
    cheese_dict = create_cheese_dict(soup)
    print(cheese_dict)

    #---- Add new Cheese to the database ----
    cheese_model_dict = create_cheese_model_dict(cheese_dict)
    new_cheese = Cheese(**cheese_model_dict)
    db.session.add(new_cheese)
    db.session.commit()
    print("Cheese model added")
    
    # #---- Add new Milk to the database ----
    # milk_model_dicts = create_milk_model_dicts(cheese_dict, cheese_id)
    # for milk_model_dict in milk_model_dicts:
    #     new_milk = Milk(**milk_model_dict)
    #     db.session.add(new_milk)
    #     db.session.commit()
    
    
    
    # #---- Add new Cheese to the database ----
    # texture_model_dicts = create_texture_model_dicts(cheese_dict, cheese_id)(cheese_dict, cheese_id)
    # for texture_model_dict in texture_model_dicts:
    #     new_texture = Texture(**texture_model_dict)
    #     db.session.add(new_texture)
    #     db.session.commit()



    cheese_id += 1
