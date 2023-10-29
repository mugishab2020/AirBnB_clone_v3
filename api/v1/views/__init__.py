from flask import Blueprint

# making the instance of the Blueprint class
app_views = blueprint('app_views', __name__, url_prefix='/api/vi')
