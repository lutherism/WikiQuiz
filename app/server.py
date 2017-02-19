import requests, json
import os
from flask import Flask, request, Response, send_from_directory
from Article import Article

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('..', 'index.html')

@app.route('/js/<path>', methods=['GET'])
def serve_js(path):
    return send_from_directory('../js', path)

@app.route('/css/<path>', methods=['GET'])
def serve_css(path):
    return send_from_directory('../css', path)

@app.route('/quiz/<article_name>/', methods = ['GET'])
def get_quiz(article_name):

    _resp = []

    try:
        a = Article(article_name)

        for question in a.quiz.get_ten_random():
            _resp.append((question.text, question.missing, question.label))

        data_send = json.dumps({
            'questions': _resp,
            'locations': a.quiz.get_random_locations(),
            'propers': a.quiz.get_random_propers(),
            'numbers': a.quiz.get_random_numbers()
        })
        resp = Response(data_send, status=200, mimetype='application/json')
    except:
        resp = Response("ERROR", status=500, mimetype='application/json')

    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp

def web_run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))

if __name__ == '__main__':
    app.debug = True
    app.run()
