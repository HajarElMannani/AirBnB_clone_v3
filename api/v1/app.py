#!/usr/bin/python3
'''fileStorage class'''
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    '''handler for 404 errors that returns JSON response for 404 errors'''
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown_ap(exception):
    '''Method that calls storage.close()'''
    storage.close()


if __name__ == "__main__":
    '''main app'''
    if getenv('HBNB_API_HOST'):
        h_host = getenv('HBNB_API_HOST')
    else:
        h_host = '0.0.0.0'
    if getenv('HBNB_API_PORT'):
        h_port = getenv('HBNB_API_PORT')
    else:
        h_port = 5000
    app.run(host=h_host, port=h_port, threaded=True)
