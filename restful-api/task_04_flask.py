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

    if data_dct is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    if 'username' not in data_dct.keys():
        return jsonify({'error': 'Username is required'}), 400

    if data_dct['username'] in data_dct.keys():
        return jsonify({'error': 'Username already exists'}), 409

    users[data_dct['username']] = {'name': data_dct['name'], 'age': data_dct['age'], 'city': data_dct['city']}
    message = {'message': 'user added', 'user': data_dct}

    return jsonify(message), 201


if __name__ == "__main__":
    app.run(debug=True)
