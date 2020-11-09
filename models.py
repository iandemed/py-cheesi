from app import db
from sqlalchemy.dialects.postgresql import JSON


class CharacteristicMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey(cheese_id), nullable=False)


class Cheese(db.Model):
    __tablename__ = 'cheese'

    id = db.Column(db.Integer, primary_key=True)
    rind = db.Column(db.String(80), nullable=False)
    colour = db.Column(db.String(80), nullable=False)
    vegetarian = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, rind, colour, vegetarian):
        self.rind = rind
        self.colour = colour
        self.vegetarian = vegetarian


class Texture(CharacteristicMixin, db.Model):
    __tablename__ = 'texture'

    texture = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, texture):
        self.cheese_id = cheese_id
        self.texture = texture


class Type(CharacteristicMixin, db.Model):
    __tablename__ = 'type'

    type = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, type):
        self.cheese_id = cheese_id
        self.type = type


class Milk(CharacteristicMixin, db.Model):
    __tablename__ = 'milk'

    milk = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, milk):
        self.cheese_id = cheese_id
        self.milk = milk


class Aroma(CharacteristicMixin, db.Model):
    __tablename__ = 'aroma'

    aroma = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, aroma):
        self.cheese_id = cheese_id
        self.aroma = aroma


class Country(CharacteristicMixin, db.Model):
    __tablename__ = 'country'

    country = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, country):
        self.cheese_id = cheese_id
        self.country = country
