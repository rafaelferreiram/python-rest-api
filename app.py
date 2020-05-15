from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Status":"Server Works!"})

app.run(debug=True)