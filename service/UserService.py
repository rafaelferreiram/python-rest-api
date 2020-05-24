from flask import json

class UserService():

    def create_user(user, mongo):
        pythonDb = mongo.db.python
        valuestr = json.dumps(user, default=lambda x: x.__dict__)
        value = json.loads(valuestr)
        userId = pythonDb.insert(value)
        return userId