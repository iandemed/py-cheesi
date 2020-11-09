from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


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


app.run(debug=True, port=9000)
