#!/usr/bin/python3
'''view for Amenity objects'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities_get():
    '''Get all amenities'''
    amenities_all = storage.all(Amenity).values()
    amenities = [amenity.to_dict() for amenity in amenities_all]
    return jsonify(amenities)


@app_views.route('amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def amenity_id(amenity_id):
    '''get amenities by id'''
    amenities = storage.get(Amenity, amenity_id)
    if not amenities:
        abort(404)
    return jsonify(amenities.to_dict())


@app_views.route('amenities/<string:amenity_id>', methods=['DELETE'])
def amenity_delete(amenity_id=None):
    '''delete amenities by given id'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def amenity_post():
    '''create an amenity'''
    amenity = request.get_json(silent=True)
    if amenity is None:
        abort(400, "Not a JSON")
    if "name" not in amenity.keys():
        abort(400, "Missing name")
    new_item = Amenity(**amenity)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def amenity_update(amenity_id):
    '''update an amenity'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
