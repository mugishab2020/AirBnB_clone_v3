#!/usr/bin/python3
"""init program"""
from flask import Blueprint


# making the instance of the Blueprint class
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
