#!/usr/bin/python3
'''view for State objects'''
import models
import json
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_get():
    '''Get all states'''
    states_all = storage.all(State).values()
    states = [state.to_dict() for state in states_all]
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def state_id(state_id):
    '''retrieve State by id'''
    states = storage.get(State, state_id)
    if not states:
        abort(404)
    return jsonify(states.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def state_delete(state_id=None):
    '''delete a state by id'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def states_post():
    '''Create a state'''
    state = request.get_json(silent=True)
    if state is None:
        abort(400, "Not a JSON")
    if "name" not in state.keys():
        abort(400, "Missing name")
    new_item = State(**state)
    storage.new(new_item)
    storage.save()
    return jsonify(new_item.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    '''update state'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    inp = request.get_json(silent=True)
    if inp is None:
        abort(400, "Not a JSON")
    for key, value in inp.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
