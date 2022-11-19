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



app.run(port=5000, host='localhost', debug=True)
