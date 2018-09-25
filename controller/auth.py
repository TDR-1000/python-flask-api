import os
from dotenv import load_dotenv, find_dotenv
from random import randint
# import random

load_dotenv(find_dotenv())

# USER_DATA = {
#     "username":"admin",
#     "password":"koyyam"
# }


class Auth(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "Auth(id='%s')" % self.id

    def verify(self, username, password):

        if not (username and password):
            return False
        if (os.getenv('API_USERNAME') == username) & (os.getenv('API_PASSWORD') == password):
            # key=random(5)
            print(randint(100, 999))
            return Auth(id=randint(100, 999))
            # return Auth(id=123)

    def identity(self, payload):
        user_id = payload['identity']
        return {"user_id": user_id}

