import os
from dotenv import load_dotenv

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from db.models import db, Cheese, Texture, Type, Milk, Aroma, Country

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


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/cheese', methods=['GET', 'POST'])
@app.route('/cheese/<id>', methods=['GET', 'PUT', 'DELETE'])
def cheeses(id=None):
    if request.method == 'GET':
        if id:
            cheese = Cheese.query.filter_by(id=id).first()
            print()
            return jsonify(cheese.asdict())
        else:
            cheese_list = []
            for cheese in Cheese.query.all():
                cheese_list.append(cheese.asdict())
            print(cheese_list)
            return jsonify(cheese_list)


'''
    if request.method == 'POST':
        new_cheese = dict_to_model(Cheese, request.get_json())
        new_cheese.save()
        return jsonify({"success": True})
'''

if __name__ == '__main__':
    app.run()

'''
@app.route('/texture', methods=['GET', 'POST'])
@app.route('/texture/<id>', methods=['GET', 'PUT', 'DELETE'])
def textures(id=None):
    print(request)
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Texture.get(Texture.id == id)))
        else:
            texture_list = []
            for texture in Texture.select():
                texture_list.append(model_to_dict(texture))
            return jsonify(texture_list)

    if request.method == 'POST':
        new_texture = dict_to_model(Texture, request.get_json())
        new_texture.save()
        return jsonify({"success": True})
'''
