#!/usr/bin/python3
'''start flask app'''
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/status')
def status_get():
    '''method that returns jsonified status'''
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/stats')
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
