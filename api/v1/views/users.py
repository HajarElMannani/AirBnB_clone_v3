#!/usr/bin/python3
'''view for Users'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users_get():
    '''Get all users'''
    users_all = storage.all(User).values()
    users = [user.to_dict() for user in users_all]
    return jsonify(users)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def users_id(user_id):
    '''retrieve user by id'''
    users = storage.get(User, user_id)
    if not users:
        abort(404)
    return jsonify(users.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'])
def user_delete(user_id=None):
    '''delete a user by id'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def user_post():
    '''Create an user'''
    user = request.get_json(silent=True)
    if user is None:
        abort(400, "Not a JSON")
    if "name" not in user.keys():
        abort(400, "Missing name")
    new_item = User(**user)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def user_update(user_id):
    '''update user'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
