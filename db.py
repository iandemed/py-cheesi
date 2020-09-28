from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, BooleanField
from cheese import get_cheese_page, find_cheese_data, find_cheese_name, create_cheese_dict, create_cheese_model, create_milk_models
from playhouse.shortcuts import dict_to_model

db = PostgresqlDatabase('cheese', user='postgres', password='',
                        host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database=db

class Cheese(BaseModel):
    name = CharField()
    rind = CharField()
    colour = CharField()
    vegetarian = BooleanField()


# These are characteristics of the cheeses that would
# normally be stored in a list. A cheese can have more
# than one of each of these properties
class Flavour(BaseModel):
    cheese_id = ForeignKeyField(Cheese)
    flavour = CharField()
class Texture(BaseModel):
    cheese_id = ForeignKeyField(Cheese)
    texture = CharField()
class Type(BaseModel):
    cheese_id = ForeignKeyField(Cheese)
    cheese_type = CharField()
class Milk(BaseModel):
    cheese_id = ForeignKeyField(Cheese)
    milk = CharField()
class Aroma(BaseModel):
    cheese_id = ForeignKeyField(Cheese)
    aroma = CharField()
class Countries(Model):
    cheese_id = ForeignKeyField(Cheese)
    country = CharField()

db.connect()
db.drop_tables([Cheese, Milk])
db.create_tables([Cheese, Milk])


cheeses = ['/abbaye-de-belloc/', '/abbaye-de-belval/']
cheese_id = 1

for cheese in cheeses:
    soup = get_cheese_page(cheese)
    cheese_dict = create_cheese_dict(soup)

    cheese_model_dict = create_cheese_model(cheese_dict)
    print(cheese_model_dict)
    new_cheese = dict_to_model(Cheese, cheese_model_dict)
    new_cheese.save()

    milk_dicts = create_milk_models(cheese_dict, cheese_id)
    for milk_dict in milk_dicts:
        new_milk = dict_to_model(Milk, milk_dict)
        new_milk.save()
    
    cheese_id += 1