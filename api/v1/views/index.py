#!/usr/bin/python3
""" making the json return """

from flask import jsonify
from api.vi.views import app_views


@app_views.route('/status')
def status():
    """ returning the status code in json """
    return jsonify({"status": "OK"})
