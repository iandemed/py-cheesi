from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cheese(db.Model):
    __tablename__ = 'cheese'

    id = db.Column(db.Integer, primary_key=True)
    rind = db.Column(db.String(80), nullable=False)
    colour = db.Column(db.String(80), nullable=False)
    vegetarian = db.Column(db.Boolean, default=False, nullable=False)
    textures = db.relationship('Texture')
    types = db.relationship('Type')
    milk = db.relationship('Milk')
    aromas = db.relationship('Aroma')
    countries = db.relationship('Country')

    def __init__(self, rind, colour, vegetarian):
        self.rind = rind
        self.colour = colour
        self.vegetarian = vegetarian

    def asdict(self):
        return {'id': self.id, 'rind': self.rind, 'colour': self.colour, 'vegetarian': self.vegetarian}


class Texture(db.Model):
    __tablename__ = 'texture'

    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey('cheese.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    texture = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, texture):
        self.cheese_id = cheese_id
        self.texture = texture

    def asdict(self):
        return {'id': self.id, 'cheese_id': self.cheese_id, 'texture': self.texture}


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey('cheese.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    type = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, type):
        self.cheese_id = cheese_id
        self.type = type

    def asdict(self):
        return {'id': self.id, 'cheese_id': self.cheese_id, 'type': self.type}


class Milk(db.Model):
    __tablename__ = 'milk'

    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey('cheese.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    milk = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, milk):
        self.cheese_id = cheese_id
        self.milk = milk

    def asdict(self):
        return {'id': self.id, 'cheese_id': self.cheese_id, 'milk': self.milk}


class Aroma(db.Model):
    __tablename__ = 'aroma'

    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey('cheese.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    aroma = db.Column(db.String(80), nullable=False)

    def __init__(self, cheese_id, aroma):
        self.cheese_id = cheese_id
        self.aroma = aroma

    def asdict(self):
        return {'id': self.id, 'cheese_id': self.cheese_id, 'aroma': self.aroma}


class Country(db.Model):
    __tablename__ = 'country'

    country = db.Column(db.String(80), nullable=False)

    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column('cheese_id', db.Integer,
                          db.ForeignKey('cheese.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, cheese_id, country):
        self.cheese_id = cheese_id
        self.country = country

    def asdict(self):
        return {'id': self.id, 'cheese_id': self.cheese_id, 'country': self.country}
