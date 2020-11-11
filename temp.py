from flask import Flask, jsonify, request
from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, BooleanField
from playhouse.shortcuts import dict_to_model, model_to_dict

# Import functions necessary to parse through cheese.com's website and parse
# through all of the data gathered
# from website_scraper import scrape_alphabet_page, find_cheese_links, get_letters
#from cheese_model_helpers import get_cheese_page, find_cheese_data, create_cheese_dict, create_cheese_model, create_milk_models, create_texture_models

import os
from dotenv import load_dotenv

load_dotenv()
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD')

db = PostgresqlDatabase('cheese', user='postgres', password=PSQL_PASSWORD,
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

# Singular characteristics for each unique cheese


class Cheese(BaseModel):
    name = CharField()
    rind = CharField()
    colour = CharField()
    vegetarian = BooleanField()


# These are characteristics of the cheeses that would normally be stored in a
# list. A cheese can have more than one of each of these properties
class Flavour(BaseModel):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    flavour = CharField()


class Texture(BaseModel):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    texture = CharField()


class Type(BaseModel):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    cheese_type = CharField()


class Milk(BaseModel):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    milk = CharField()


class Aroma(BaseModel):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    aroma = CharField()


class Countries(Model):
    cheese_id = ForeignKeyField(Cheese, on_delete='CASCADE')
    country = CharField()

'''
db.connect()
db.drop_tables([Cheese, Milk, Texture])
db.create_tables([Cheese, Milk, Texture])


# Get a list of all of the alphabetic letters included in the cheese database
alphabet_soup = scrape_alphabet_page()
# letters = get_letters(alphabet_soup)

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

    cheese_model_dict = create_cheese_model(cheese_dict)
    new_cheese = dict_to_model(Cheese, cheese_model_dict)
    new_cheese.save()

    milk_dicts = create_milk_models(cheese_dict, cheese_id)
    for milk_dict in milk_dicts:
        new_milk = dict_to_model(Milk, milk_dict)
        new_milk.save()

    texture_dicts = create_texture_models(cheese_dict, cheese_id)
    for texture_dict in texture_dicts:
        new_texture = dict_to_model(Texture, texture_dict)
        new_texture.save()

    cheese_id += 1
'''