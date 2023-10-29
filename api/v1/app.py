#!/usr/bin/python3
""" importing the needed moules """
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


# declaring the teardow handler
@app.teardown_appcontext
def teardown(exception):
    """closes the SQLAchemy session"""
    storage.close()


if __name__ = "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
