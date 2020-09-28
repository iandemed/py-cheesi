from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, BooleanField
from cheese import get_cheese_page, find_cheese_data, find_cheese_data, create_cheese_dict

db = PostgresqlDatabase('cheese', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

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
class Flavour(Model):
    cheese_id = ForeignKeyField(Cheese)
    flavour = CharField()
class Texture(Model):
    cheese_id = ForeignKeyField(Cheese)
    texture = CharField()
class Type(Model):
    cheese_id = ForeignKeyField(Cheese)
    cheese_type = CharField()
class Milk(Model):
    cheese_id = ForeignKeyField(Cheese)
    milk = CharField()
class Aroma(Model):
    cheese_id = ForeignKeyField(Cheese)
    aroma = CharField()
class Countries(Model):
    cheese_id = ForeignKeyField(Cheese)
    country = CharField()

soup = get_cheese_page('/abbaye-de-belloc/')
cheese_dict = create_cheese_dict(soup)

print(cheese_dict)