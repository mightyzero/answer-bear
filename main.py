from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Hi, I'm Answer Bear!"


@app.route("/", methods=['POST'])
def reply():
    comment = request.get_json()['comment']
    resp = "You said: {}. I don't know how to respond to that, I'm just a bear!".format(comment)

    return jsonify(reply=resp), 400


if __name__ == "__main__":
    app.run()
