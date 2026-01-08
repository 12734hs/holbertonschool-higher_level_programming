#!/usr/bin/python3
from flask import Flask, jsonify, request

users = {}
not_found_user = {'error': "User not found", "status_code": 404}
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
    json_file = request.get_json()
    username = json_file.get('username')

    if json_file is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    if not username:
        return jsonify({'error': "Username is required"}), 400

    if json_file['username'] in users:
        return jsonify({'error': "Username already exists"}), 409

    users[username] = json_file

    return jsonify({"message": "user added", 'user': json_file})


if __name__ == "__main__":
    app.run(debug=True)
