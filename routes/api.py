import json

from flask import Blueprint
from flask import jsonify


bp = Blueprint(__name__, "api")


@bp.route("/", methods=["GET"])
def index():
    response = {
        "error": 0,
        "message": 'success',
        "data": {
            "message": 'hello World'
        }
    }
    return jsonify(response)
@bp.route("/api", methods=["GET"])
def apiURI():
    response = {
        "error": 0,
        "message": 'success',
        "data": {
            "message": 'AI API ENDPOINTS'
        }
    }
    return jsonify(response)

@bp.route("/api/v1", methods=["GET"])
def get_ApiVersion():
    response = {
        "error": 0,
        "message": 'success',
        "data": {
            "message": 'AI Api version : 1.0'
        }
    }
    return jsonify(response)


