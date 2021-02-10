import flask
from flask import request, jsonify, json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/resources/books', methods=['GET'])
def books():
    bookPath = '/var/www/projects/api/resources/books'
    with open(bookPath, encoding='utf-8') as bookFile:
        books = json.loads(bookFile.read())

    return jsonify(books)

app.run()