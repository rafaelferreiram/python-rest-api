from flask import Flask, jsonify , json , request
from flask_pymongo import PyMongo
from config.mongoDB import MongoConfig
from models.UserModel import UserModel
from dto.response.UserResponseDTO import UserResponseDTO

app = Flask(__name__)
app.config["MONGO_URI"] = MongoConfig.mongoURI()
app.config["MONGO_DBNAME"] = MongoConfig.mongoDataBase()

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Status":"Server Works!"})

@app.route("/api/v1/user/cad", methods=["GET"])
def insert_user():
  userModel = UserModel("Teste","123","22","rafael@ferreira.dev")
  pythonDb = mongo.db.python
  valuestr = json.dumps(userModel, default=lambda x: x.__dict__)
  value = json.loads(valuestr)
  userId = pythonDb.insert(value)
  userResponse = pythonDb.find_one({'_id': userId })
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

@app.route("/api/v1/user/cad", methods=["POST"])
def insert_user_post():
  userModel = UserModel(request.json.get("firstName"),request.json.get("lastName"),request.json.get("age"),request.json.get("email"))
  pythonDb = mongo.db.python
  valuestr = json.dumps(userModel, default=lambda x: x.__dict__)
  value = json.loads(valuestr)
  userId = pythonDb.insert(value)
  userResponse = pythonDb.find_one({'_id': userId })
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

@app.route("/api/v1/user/name/<string:name>", methods=["GET"])
def get_user_by_name(name):
  pythonDb = mongo.db.python
  userResponse = pythonDb.find_one({'firstName': name})
  print(userResponse)
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

app.run(debug=True)