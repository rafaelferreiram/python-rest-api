from flask import Flask, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:pwdadmin@dynamic-dug18.mongodb.net/py-db?retryWrites=true&w=majority"
app.config["MONGO_DBNAME"] = "python"
mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Status":"Server Works!"})

@app.route("/insert", methods=["GET"])
def add_star():
  pythonDb = mongo.db.python
  name = "Rafael"
  distance = "1km"
  star_id = pythonDb.insert({'name': name, 'distance': distance})
  new_star = pythonDb.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

app.run(debug=True)