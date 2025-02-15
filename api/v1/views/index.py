#!/usr/bin/python3
'''start flask app'''
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', methods=['GET'])
def status_get():
    '''method that returns jsonified status'''
    status = {"status": "OK"}
    return jsonify(status)
