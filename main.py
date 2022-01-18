from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data" : data,
        "message" : "Success!"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data" : star_data,
        "message" : "Success!"
    }), 200
# Link for specific star data:
# http://127.0.0.1:5000/star?name=Capella
if __name__ == "__main__":
    app.run(debug = True)