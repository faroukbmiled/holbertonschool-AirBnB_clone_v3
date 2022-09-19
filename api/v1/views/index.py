#!/usr/bin/python3
"""test"""
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def stat():
    """status"""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats')
def status():
    """counts obj"""
    count = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(count)
