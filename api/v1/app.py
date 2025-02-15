#!/usr/bin/python3
'''fileStorage class'''
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv, environ
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "0.0.0.0"}})
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exeption):
    '''Method that calls storage.close()'''
    storage.close()


if __name__ == "__main__":
    h_host = '0.0.0.0'
    h_port = 5000
    if environ.get('HBNB_API_HOST'):
        h_host = getenv('HBNB_API_HOST')
    if environ.get('HBNB_API_PORT'):
        h_port = getenv('HBNB_API_PORT')
        
    app.run(host=h_host, port=h_port, threaded=True)
