#!/usr/bin/python3
'''view for City objects'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.state import City
from models.city import City
from models.place import Place
from models.review import Review
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def review_get(place_id):
    '''Get rviews of a place'''
    places = storage.get(Place, place_id)
    if not places:
        abort(404)
    reviews_list = [review.to_dict() for review in places.reviews]
    return jsonify(reviews_list)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def reviews_id(review_id):
    '''Retrieve a review by id'''
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def review_delete(review_id=None):
    '''delete a review'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def reviews_post(place_id):
    '''review a city'''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    review_o = request.get_json(silent=True)
    if review_o is None:
        abort(400, "Not a JSON")
    if "user_id" not in review_o:
        abort(400, "Missing user_id")
    user = storage.get(User, review_o["user_id"])
    if not user:
        abort(404)
    if "text" not in review_o:
        abort(400, "Missing text")
    new_item = Review(place_id=place_id, **review_o)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def review_update(review_id):
    '''update review'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "user_id", "created_at", "updated_at"]:
            setattr(Review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
