#!flask/bin/python
from flask import Flask, request, jsonify, abort
from utils import return_news, get_articles

app = Flask(__name__)



@app.route('/api/news', methods=['POST'])
def index():
    if not request.json or not 'keywords' in request.json:
        return jsonify({'error': 'keywords is requirewd'}), 400
    keywords = request.json['keywords']

    response = get_articles(keywords)
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
