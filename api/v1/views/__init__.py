#!/usr/bin/python3
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import * #c
from api.v1.views.states import * #c
from api.v1.views.cities import * #c
from api.v1.views.amenities import * #c
from api.v1.views.users import * #c
from api.v1.views.places import * #c
