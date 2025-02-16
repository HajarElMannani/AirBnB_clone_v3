#!/usr/bin/python3
'''fileStorage class'''
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_ap(exception):
    '''Method that calls storage.close()'''
    storage.close()


if __name__ == "__main__":
    if getenv('HBNB_API_HOST'):
        h_host = getenv('HBNB_API_HOST')
    else:
        h_host = '0.0.0.0'
    if getenv('HBNB_API_PORT'):
        h_port = getenv('HBNB_API_PORT')
    else:
        h_port = 5000
    app.run(host=h_host, port=h_port, threaded=True)
