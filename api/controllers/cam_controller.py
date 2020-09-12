from flask import Flask, jsonify, make_response, request
from api import app, db

@app.route('/api/v1/cam')
@app.route('/monitoramento/api/v1/cam')
def index_cam():
    return jsonify("Hi Cam, Welcome to Monitoramento API in Flask!")