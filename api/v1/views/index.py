#!/usr/bin/python3
'''start flask app'''
from api.v1.views import app_views
from flask import Flask, jsonify, request


@app_views.route('/status', methods=['GET'])
def status_get():
    '''method that returns jsonified status'''
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
    '''endpoint that retrieves the number of each objects by type'''
    counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(counts)
