from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

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
    # comment: str = request.get_json()['comment']
    resp = "I don't know how to respond to that, I'm just a bear!"

    return jsonify(reply=resp)
