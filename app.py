import os
from dotenv import load_dotenv

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from db.models import db, Cheese, Texture, Type, Milk, Aroma, Country
from helper_functions.cheese_dict_helpers import create_cheese_model_dict

from sqlalchemy.exc import ProgrammingError

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.messsage = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    
    def to_dict(self):
        iu_dict = dict(self.payload or ())
        iu_dict['status'] = self.status_code
        iu_dict['message'] = self.messsage

        return iu_dict

# App instances within modules are prone to circular error issues, per
# Flask-SQLAlchemy doucmentation, I implment application contexts
def create_app():
    app = Flask(__name__)
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app()
db.init_app(app)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def hello():
    return "Hello World!"

# ---- Cheese Routes ----

@app.route('/cheese', methods=['GET', 'POST'])
@app.route('/cheese/<id>', methods=['GET', 'PUT', 'DELETE'])
def cheeses(id=None):
    if request.method == 'GET':
        if id:
            try:
                cheese = Cheese.query.filter_by(id=id).first()
                return jsonify(cheese.asdict())
            except:
                raise InvalidUsage('Please enter a valid Cheese ID number', status_code=404)
        else:
            cheese_list = []
            for cheese in Cheese.query.all():
                cheese_list.append(cheese.asdict())
            return jsonify(cheese_list)

    if request.method == 'POST':
        try:
            new_cheese = Cheese(**request.get_json())
            db.session.add(new_cheese)
            db.session.commit()
            return jsonify({"success": True})
        except TypeError as err:
            if "unexpected keyword" in str(err):
                raise InvalidUsage('Please make sure you are only using valid column names: (name, rind, colour, vegetarian)', 400)
            else:
                raise InvalidUsage('Please make sure you are using valid types for all fields', 400)

    if request.method == 'DELETE':
        try:
            cheese = Cheese.query.filter_by(id=id).first()
            db.session.delete(cheese)
            db.session.commit()
            return jsonify(cheese.asdict())
        except:
            raise InvalidUsage('Please enter a valid Cheese ID number', status_code=404)

    if request.method == 'PUT':
        try:
            cheese = Cheese.query.filter_by(id=id).update(request.get_json())
            db.session.commit()
        except TypeError as err:
            if "unexpected keyword" in str(err):
                raise InvalidUsage('Please make sure you are only using valid column names: (name, rind, colour, vegetarian)', 400)
            else:
                raise InvalidUsage('Please make sure you are using valid types for all fields', 400)
        except:
            raise InvalidUsage('Please enter a valid Cheese ID number', status_code=404)
        return jsonify({"success": True})

# ---- Texture Routes ----

@app.route('/texture', methods=['GET', 'POST'])
@app.route('/texture/<id>', methods=['GET', 'PUT', 'DELETE'])
def textures(id=None):
    if request.method == 'GET':
        if id:
            try:
                texture = Texture.query.filter_by(id=id).first()
                return jsonify(texture.asdict())
            except:
                raise InvalidUsage('Please enter a valid Texture ID number', status_code=404)
        else:
            texture_list = []
            for texture in Texture.query.all():
                texture_list.append(texture.asdict())
            return jsonify(texture_list)

    if request.method == 'POST':
        try:
            new_texture = Texture(**request.get_json())
            db.session.add(new_texture)
            db.session.commit()
            return jsonify({"success": True})
        except TypeError as err:
            if "unexpected keyword" in str(err):
                raise InvalidUsage('Please make sure you are only using valid column names: (cheese_id, texture)', 400)
            else:
                raise InvalidUsage('Please make sure you are using valid types for all fields', 400)
        except:
            raise InvalidUsage('Please make sure you are using a valid JSON object', 400)

    if request.method == 'DELETE':
        try:
            texture = Texture.query.filter_by(id=id).first()
            db.session.delete(texture)
            db.session.commit()
            return jsonify(texture.asdict())
        except:
            raise InvalidUsage('Please enter a valid Texture ID number', status_code=404)

    if request.method == 'PUT':
        try:
            texture = Texture.query.filter_by(id=id).update(request.get_json())
            db.session.commit()
        except ProgrammingError as err:
            raise InvalidUsage('ProgrammingError: Please make sure you are using valid coulmn names and a non-empty list for your request', 400)
        except:
            raise InvalidUsage('Please enter a valid Texture ID number', status_code=404)

        return jsonify({"success": True})

# ---- Aroma Routes ----

@app.route('/aroma', methods=['GET', 'POST'])
@app.route('/aroma/<id>', methods=['GET', 'PUT', 'DELETE'])
def aromas(id=None):
    if request.method == 'GET':
        if id:
            try:
                aroma = Aroma.query.filter_by(id=id).first()
                return jsonify(aroma.asdict())
            except:
                raise InvalidUsage('Please enter a valid Aroma ID number', status_code=404)
        else:
            aroma_list = []
            for aroma in Aroma.query.all():
                aroma_list.append(aroma.asdict())
            return jsonify(aroma_list)

    if request.method == 'POST':
        try:
            new_aroma = Aroma(**request.get_json())
            db.session.add(new_aroma)
            db.session.commit()
            return jsonify({"success": True})
        except TypeError as err:
            if "unexpected keyword" in str(err):
                raise InvalidUsage('Please make sure you are only using valid column names: (cheese_id, aroma)', 400)
            else:
                raise InvalidUsage('Please make sure you are using valid types for all fields', 400)
        except:
            raise InvalidUsage('Please make sure you are using a valid JSON object', 400)

    if request.method == 'DELETE':
        try:
            aroma = Aroma.query.filter_by(id=id).first()
            db.session.delete(aroma)
            db.session.commit()
            return jsonify(aroma.asdict())
        except:
            raise InvalidUsage('Please enter a valid Aroma ID number', status_code=404)

    if request.method == 'PUT':
        try:
            aroma = Aroma.query.filter_by(id=id).update(request.get_json())
            db.session.commit()
        except ProgrammingError as err:
            raise InvalidUsage('ProgrammingError: Please make sure you are using valid coulmn names and a non-empty list for your request', 400)
        except:
            raise InvalidUsage('Please enter a valid Aroma ID number', status_code=404)

        return jsonify({"success": True})

if __name__ == '__main__':
    app.run()
