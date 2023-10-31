#!/usr/bin/python3
""" making the json return """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ check the status of route """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """ check the status of route """
    return jsonify(
            {
                "amenities": storage.count('Amenity'),
                "cities": storage.count('City'),
                "places": storage.count('Place'),
                "reviews": storage.count('Review'),
                "states": storage.count('State'),
                "users": storage.count('User')
                })
