#!flask/bin/python
from flask import Flask, request, jsonify, abort
from utils import return_news

app = Flask(__name__)



@app.route('/api/news', methods=['POST'])
def index():
    if not request.json or not 'keywords' in request.json:
        return jsonify({'error': 'keywords is requirewd'}), 400
    keywords = request.json['keywords']

    return_news(keywords)
    task = {
        'keywords': request.json['keywords'],
        'done': False
    }
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
