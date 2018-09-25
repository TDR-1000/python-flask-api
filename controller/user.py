
from model import db
from datetime import datetime
from bson.objectid import ObjectId
from passlib.hash import md5_crypt as pwd_context
from flask import current_app
from exceptions import BadRequest



class UserController(object):

    def get_user(self):
        try:
            result = list(db.db.user.find({}))
        except:
            result = []
        
        for each_result in result:
            each_result['_id'] = str(each_result['_id'])

        return result

    def create_user(self, **kwargs):
        email = kwargs.get("email")
        username = kwargs.get("username")
        password = kwargs.get("password")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")

        current_date = str(datetime.now())

        result_object = {
            "email": email,
            "username": username,
            "password": pwd_context.encrypt(password),
            "first_name": first_name,
            "last_name": last_name,
            "timezone": 'Asia/Jakarta',
            "join_date": str(current_date),
            "expired_date": str(current_date),
            # "confirmation_code": self.id_generator(),  # generate random code
            "is_active": True,
            "is_deleted": False,
            "is_admin": False,
            "user_type": "register",
            "picture": "-"
        }

        result = db.db.user.insert_one(result_object)

        result_object.update({"_id": str(result.inserted_id)})

        return result_object
