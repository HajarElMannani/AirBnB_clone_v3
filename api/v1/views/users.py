#!/usr/bin/python3
'''
view for Users
'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users_get():
    '''Get all users'''
    users_all = storage.all('User').values()
    print(users_all)
    users = [user.to_dict() for user in users_all]
    return jsonify(users)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def users_id(user_id):
    '''get users by id'''
    users = storage.get(User, user_id)
    if not users:
        abort(404)
    return jsonify(users.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def user_delete(user_id=None):
    '''delete users'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def user_post():
    '''create new users'''
    user = request.get_json(silent=True)
    if user is None:
        abort(400, "Not a JSON")
    if "email" not in user.keys():
        abort(400, "Missing email")
    if "password" not in user.keys():
        abort(400, "Missing password")
    new_item = User(**user)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def user_update(user_id):
    '''update users'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
