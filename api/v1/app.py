#!/usr/bin/python3
'''fileStorage class'''
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exeption):
    '''Method that calls storage.close()'''
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
