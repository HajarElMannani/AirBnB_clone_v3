#!usr/bin/python3
'''view for link between Place objects and Amenity'''
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request
from os import getenv
from models import storage_t


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def amenities_get(place_id):
    '''get emenities by place'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if storage_t == 'db':
        amenities = [amenity.to_dict() for amenity in place.emenities]
    else:
        amenities = [storage.get(Amenity, amenity_id).to_dict()
                     for amenity_id in place.amenity_ids]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def amenity_delete(place_id, amenity_id):
    '''delete an amenity'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if storage_t == 'db':
        if amenity not in place.amenities:
            abort(404)
        place.amenities.delete(amenity)
    else:
        if amenity not in place.amenity_ids:
            abort(404)
        place.amenity_ids.delete(amenity)
    storage.save()
    return jsonify({}), 200


'''
@app_views.route('/places/<place_id>/amenities/<amenity_id>',
 methods=['POST'], strict_slashes=False)
'''
