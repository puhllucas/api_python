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



@app.route('/livros')
def read_all() -> jsonify:
    return jsonify(books)



app.run(port=5000, host='localhost', debug=True)
