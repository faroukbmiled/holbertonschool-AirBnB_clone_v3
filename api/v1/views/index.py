#!/usr/bin/python3
"""task nm 3"""
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status')
def status():
    """status response"""
    return jsonify({"status": "OK"}), 200
