from flask import Blueprint

# making the instance of the Blueprint class
app_views = Blueprint('app_views', __name__, url_prefix='/api/vi')
