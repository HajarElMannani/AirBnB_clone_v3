#!/usr/bin/python3
""" place view """
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from flask import abort, request, jsonify
import json


@app_views.route("/cities/<city_id>/places", methods=['GET'], strict_slashes=False)
def place_get(city_id):
    '''get place by city'''
    cities = storage.get(City, city_id)
    if not cities:
        abort(404)
    places = []
    for place in cities.places:
        places.append(place.to_dict())
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    '''get place by its ID'''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    '''delete a place'''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    '''create a place by  city'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places_o = request.get_json(silent=True)
    if not places_o:
        abort(400, "Not a JSON")
    if "user_id" not in places_o:
        abort(400, "Missing user_id")
    user = storage.get(User, places_o["user_id"])
    if not user:
        abort(404)
    if "name" not in places_o:
        abort(400, "Missing name")
    new_place = Place(**places_o)
    new_place.city_id = city_id
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    '''update a place'''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    place_obj = request.get_json(silent=True)
    if not place_obj:
        abort(400, "Not a JSON")
    for key, value in place_obj.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
