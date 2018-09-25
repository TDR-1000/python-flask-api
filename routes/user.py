import json

from flask import Blueprint
from flask import jsonify
from flask import request
from flask_restful import Resource, Api
from flask_jwt import jwt_required,current_identity

from controller import UserController
from exceptions import BadRequest

userController = UserController()

bp = Blueprint(__name__, "user")


@bp.route("/api/v1/user/", methods=["GET"])
@jwt_required()
def get():
    response = {"error": 0, "message": "success", "data": dict(current_identity)}

    return jsonify(response)



@bp.route("/api/v1/users", methods=["GET"])
@jwt_required()
def get_user():
    result = userController.get_user()

    response = {"error": 0, "message": "success", "data": result}

    return jsonify(response)

@bp.route("/api/v1/auth", methods=["POST"])
def auth_user():
    result = userController.verify('koyyam','snowowl')

    response = {"error": 0, "message": "success", "data": result}

    return jsonify(response)


@bp.route("/api/v1/user", methods=["POST"])
def create_user():

    user_object = request.data

    try:
        user_object_json = json.loads(user_object)
    except:
        raise BadRequest("user_object is missing or error format", 200, 1)

    try:
        email = user_object_json['email']
        username = user_object_json['username']
        password = user_object_json['password']
        first_name = user_object_json['first_name']
        last_name = user_object_json['last_name']
    except:
        raise BadRequest("email, username, password, first_name or last_name is missing",
                         200, 1)

    params = {
        "email": email,
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
    }

    result = userController.create_user(**params)

    response = {"message": "success", "error": 0, "data": result}

    return jsonify(response)
