import flask
from flask import request, jsonify, json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

bookPath = '/var/www/projects/api/resources/books'
with open(bookPath, encoding='utf-8') as bookFile:
    allBooks = json.loads(bookFile.read())

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/resources/books', methods=['GET'])
def getBooks():
    
    return jsonify(allBooks)

@app.route('/resources/book', methods=['GET'])
def getBook():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    result = []
    for book in allBooks:
        if book['id'] == id:
            result.append(book)
    
    return jsonify(result)

app.run()