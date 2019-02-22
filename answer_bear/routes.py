import os

from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin

FAREWELLS = ['bye', 'good bye', 'goodbye', 'byebye', 'bye bye', 'seeya', 'cya', 'farewell', 'fare thee well']
GREETINGS = ['hi', 'hello', 'what\'s up', 'wassup', 'hiz', 'hizz', 'hizzz']

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET'])
@cross_origin()
def hello():
    return "Hi, I'm Answer Bear!"


@app.route("/", methods=['POST'])
@cross_origin()
def reply():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

    comment: str = request.get_json()['comment']

    resp = "I don't know how to respond to that, I'm just a bear!"
    if comment.lower().strip() in GREETINGS:
        resp = 'Hi! I\'m Bear. How can this bear be of service to you? Ask me something.'
    elif comment.lower().strip() in FAREWELLS:
        resp = 'Bye bye! Come to this bear for answers again! I give free bear hugs!'
    elif 'hoax' in comment and 'environment' in comment:
        resp = """Global warming is happening and human is contributing to it.
        
        Link 1: https://climate.nasa.gov/evidence
        Link 2: https://www.livescience.com/topics/global-warming
        Link 3: https://www.nationalgeographic.com/environment/global-warming/global-warming-effects
        """
    elif os.path.isfile('d2v_model.model'):
        resp = "Let me look in my magical pouch!"

    return jsonify(reply=resp)
