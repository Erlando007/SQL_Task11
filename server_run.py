from flask import Flask, jsonify, request
from main import *
from flask import Flask, jsonify, request
from main import *

app = Flask(__name__)

@app.route("/get_book/", methods=['GET'])
def get_items():
    items = get_book()
    return jsonify({'data':items})

@app.route('/create_book/', methods=['POST'])
def create_item():
    data = request.get_json()
    item = ItemPydantic(
        title = data.get('title', 'no title'),
        author = data.get('author', 'do author'),
        genre = data.get('genre', 'no genre'),
        created_at = data.get('created_at', 'no data')
    )
    create_book(item)
    return jsonify({'message':'created successfully'})

@app.route('/retrieve_item/<int:item_id>/', methods=['GET'])
def get_one_item(item_id):
    item = retrieve(item_id)
    if not item:
        return jsonify({'message':'not found'})
    
    return jsonify({'data':item})

@app.route('/update_book/<int:item_id>/', methods=['PUT'])
def update_item(item_id):
    try:
        data = request.get_json()
        update_book(item_id, data)
        return f'sucessfully'
    except:
        return f'failed'

@app.route('/delete_book/<int:item_id>/', methods=['DELETE'])
def delete_books(item_id):
    try:
        delete_book(item_id)
        return f'sucessfuly'
    except:
        return f'failed'


@app.route("/", methods=['GET'])
def hello():
    return '<h1>Hello World</h1>'

app.run(host='localhost', port=8000)