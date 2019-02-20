from flask import Flask, request, jsonify, Response

from answer_bear import app


@app.route("/", methods=['GET'])
def hello():
    return "Hi, I'm Answer Bear!"


@app.route("/", methods=['POST'])
def reply():
    # comment: str = request.get_json()['comment']
    resp = "I don't know how to respond to that, I'm just a bear!"

    return jsonify(reply=resp), 400
