import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

'''
@app.route('/cheese', methods=['GET', 'POST'])
@app.route('/cheese/<id>', methods=['GET', 'PUT', 'DELETE'])
def cheeses(id=None):
    print(request)
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Cheese.get(Cheese.id == id)))
        else:
            cheese_list = []
            for cheese in Cheese.select():
                cheese_list.append(model_to_dict(cheese))
            return jsonify(cheese_list)

    if request.method == 'POST':
        new_cheese = dict_to_model(Cheese, request.get_json())
        new_cheese.save()
        return jsonify({"success": True})


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
