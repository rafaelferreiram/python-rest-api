from flask import Flask, jsonify , json , request
from flask_pymongo import PyMongo
from config.mongoDB import MongoConfig
from models.UserModel import UserModel
from dto.response.UserResponseDTO import UserResponseDTO
from service.UserService import UserService

app = Flask(__name__)
app.config["MONGO_URI"] = MongoConfig.mongoURI()
app.config["MONGO_DBNAME"] = MongoConfig.mongoDataBase()

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Status":"Server Works!"})

@app.route("/api/v1/user/cad", methods=["POST"])
def insert_user_post():
  returnMsg = ""
  try:
    userModel = UserModel(request.json.get("firstName"),request.json.get("lastName"),request.json.get("age"),request.json.get("email"))
    userId = UserService.create_user(userModel,mongo)
    returnMsg = "User created successfully. userId: "+userId
  except:
    returnMsg = "Error creating user"
  return returnMsg

@app.route("/api/v1/user/name/<string:name>", methods=["GET"])
def get_user_by_name(name):
  returnMsg = ""
  try:
    pythonDb = mongo.db.python
    userResponse = pythonDb.find_one({'firstName': name})
    userResponseDTO = UserResponseDTO.formatDTO(userResponse)
    returnMsg = userResponseDTO
  except:
    returnMsg = "Error getting User"
  return returnMsg

def get_user_by_id(id):
  #userResponse = pythonDb.find_one({'_id': userId })
  #userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return "TODO GetById"

@app.route("/api/v1/user/name/<string:name>", methods=["DELETE"])
def delete_user(name):
  return "TODO Delete"

def update_user(user):
  return "TODO Update"

app.run(debug=True)