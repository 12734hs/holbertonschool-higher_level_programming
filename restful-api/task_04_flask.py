#!/usr/bin/python3
from flask import Flask, jsonify, abort, request

users = {'admin': {"name": "admin", "age": "immortal", "city": "earth"}}
not_found_user = {'error': "User not found", "status_code": 404}
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data_return():
    return jsonify(users)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def return_user(username):
    if username in users:
        return users[username]
    else:
        return jsonify(not_found_user)

@app.route('/add_user', methods=["POST", "GET"])
def add_user():
    file = request.get_json()

    if file is None:
        return jsonify({'error': "Invalid JSON"}), 400

    if 'username' not in file:
        return jsonify({'error': "Username is required"}), 400

    if file['username'] in users:
        return jsonify({'error': "Username is already exists"}), 409

    users[file['username']] = {"name": file['name'], "age": file['age'], "city": file['city']}

    return jsonify({'message': 'user added', 'user': {'username': file["username"], 'name': file['name'], "age": file["age"], 'city': file['city']}})

if __name__ == "__main__":
    app.run(debug=True)
