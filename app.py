from flask import Flask, jsonify , json
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
  userModel = UserModel("Rafael","Ferreira","22","rafael@ferreira.dev")
  pythonDb = mongo.db.python
  valuestr = json.dumps(userModel, default=lambda x: x.__dict__)
  value = json.loads(valuestr)
  userId = pythonDb.insert(value)
  userResponse = pythonDb.find_one({'_id': userId })
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

@app.route("/api/v1/user/name", methods=["GET"])
def get_user_by_name(name):
  pythonDb = mongo.db.python
  userResponse = pythonDb.find_one({'firstName': name})
  userResponseDTO = UserResponseDTO.formatDTO(userResponse)
  return userResponseDTO

app.run(debug=True)