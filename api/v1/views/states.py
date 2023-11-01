#!/usr/bin/python3
"""An end point for usr"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_user(id=None):
    """a function to retrieve user from the database"""
    if id is None:
        states = storage.all(State)
        state_list = [state.to_dict() for state in states.values()]
        return jsonify(state_list)
    return jsonify(storage.all("State", id))


@app_views.route('states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(id=None):
    """a function that delete the object db"""
    state = storage.get("State", id)
    if state is not None:
        storage.delete(state)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_user():
    """a function to create state"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
