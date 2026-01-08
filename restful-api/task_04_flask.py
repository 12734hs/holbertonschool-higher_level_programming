#!/usr/bin/python3
from flask import Flask, jsonify, request

users = {}
app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def return_info(username):
    if username in users.keys():
        return jsonify(users[username])
    else:
        return jsonify({'error': "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():

    data_dct = request.get_json()

    if not data_dct:
        return jsonify({'error': 'Invalid JSON'}), 400

    username = data_dct.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if username in users:
        return jsonify({'error': 'Username already exists'}), 409

    users[username] = data_dct
    message = {'message': 'user added', 'user': data_dct}

    return jsonify(message), 201


if __name__ == "__main__":
    app.run(debug=True)
