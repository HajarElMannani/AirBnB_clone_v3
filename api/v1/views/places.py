#!/usr/bin/python3
'''view for place objects'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.state import City
from models.city import City
from models.place import Place
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def places_get(city_id):
    '''Get all places objects of a state'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places_list = [place.to_dict() for place in city.places]
    return jsonify(places_list)

'''
@app_views.route('cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
def city_id(city_id):
   
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('cities/<string:city_id>', methods=['DELETE'])
def city_delete(city_id=None):
   
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('states/<string:state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def cities_post(state_id):
   
    states = storage.get(State, state_id)
    if not states:
        abort(404)
    city = request.get_json(silent=True)
    if city is None:
        abort(400, "Not a JSON")
    if "name" not in city:
        abort(400, "Missing name")
    new_item = City(state_id=state_id, **city)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('cities/<city_id>', methods=['PUT'], strict_slashes=False)
def cities_update(city_id):
   
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
'''
