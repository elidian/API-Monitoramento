from flask import Flask, jsonify, make_response, request, abort
from api import app, db
from api.models.user import User

@app.route('/api/v1/user')
def index_user():
    return jsonify("Hi User, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    if users is None:
        abort(404)
    return make_response(jsonify(users), 200)

@app.route('/api/v1/user/new', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    senha = request.json['senha']
    user = User(username, email, senha)

    db.session.add(user)
    db.session.commit()

    return jsonify(user)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

