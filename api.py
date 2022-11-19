from flask import Flask, jsonify, request


app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O Senhor dos Aneis',
        'Author': 'J.R.R Tolkien',
    },
    {
        'id': 2,
        'title': 'Harry Potter',
        'Author': 'J.K Howling',
    },
    {
        'id': 3,
        'title': 'James Clear',
        'Author': 'Hábitos Atômicos',
    },
]



@app.route('/livros', methods=['GET'])
def read_all() -> jsonify:
    return jsonify(books)

@app.route('/livros/search/<int:id>', methods=['GET'])
def read_id(id) -> jsonify:
    for items in books:
        if items.get('id') == id:
            return jsonify(items)    
    return jsonify(books)


@app.route('/livros/delete/<int:id>', methods=['POST', 'GET'])
def delete_id(id) -> None:
    for index, item in enumerate(books):
        if item.get('id') == id:
            del books[index]
    return jsonify(books)


@app.route('/livros/edit/<int:id>', methods=['PUT', 'POST', 'GET'])
def update(id) -> jsonify:
    #book_modified = request.get_json()
    new_data = {'id': 3, 'title': 'None', 'Author': 'Hábitos Atômicos'}
    for index, item in enumerate(books):
        if item.get('id') == id:
            item.update(new_data)
    return jsonify(books)



app.run(port=5000, host='localhost', debug=True)
