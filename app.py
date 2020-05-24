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
    UserService.create_user(userModel,mongo)
    returnMsg = "User created successfully"
  except:
    returnMsg = "Error creating user"
  #userResponse = pythonDb.find_one({'_id': userId })
  #userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return returnMsg

@app.route("/api/v1/user/name/<string:name>", methods=["GET"])
def get_user_by_name(name):
  pythonDb = mongo.db.python
  userResponse = pythonDb.find_one({'firstName': name})
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

@app.route("/api/v1/user/name/<string:name>", methods=["DELETE"])
def delete_user(name):
  return "TODO Delete"

def update_user(user):
  return "TODO Update"

app.run(debug=True)