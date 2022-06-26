# Import flask module
# flask is a module which allows you to write a python service which can serve HTTP request made from UI
# jsonify is a function in Flask's flask. json module
# jsonify serializes data to JSON format, wraps it in a Response object with the application/json mimetype.

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/get_locations_names", methods = ["GET"])
def get_locations_names():
    response = jsonify({
        "locations" : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/predict_home_price", methods = ["GET","POST"])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
