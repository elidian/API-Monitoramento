from flask import Flask, jsonify, make_response, request
from api import app, db

@app.route('/')
@app.route('/index')
@app.route('/monitoramento')
def index():
    return jsonify("Welcome to Monitoramento API in Flask!")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)