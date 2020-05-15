from flask import Flask, jsonify
from flask_pymongo import PyMongo
from config.mongoDB import MongoConfig

app = Flask(__name__)
app.config["MONGO_URI"] = MongoConfig.mongoURI()
app.config["MONGO_DBNAME"] = MongoConfig.mongoDataBase()

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Status":"Server Works!"})

@app.route("/insert", methods=["GET"])
def add_star():
  pythonDb = mongo.db.python
  name = "Test"
  distance = "1km"
  star_id = pythonDb.insert({'name': name, 'distance': distance})
  new_star = pythonDb.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

app.run(debug=True)