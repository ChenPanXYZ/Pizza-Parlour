from flask import Flask
from flask import jsonify
from flask import request
import json
from classes.System import System
app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'


# Order Part
@app.route('/show-all-orders', methods = ['GET'])
def show_all_orders():
    # Sample cURL: curl localhost:5000/show-all-orders
    return jsonify(system.show_all_orders())


# Menu Part
@app.route('/get-full-menu')
def get_full_menu():
    # Route For Get the Full Menu
    # Sample cURL: curl localhost:5000/get-full-menu
    # Expected Output: JSON contains infomation of the menu.

    return jsonify(system.menu.get_full_content())


@app.route('/get-price-for-specific-item', methods=['POST'])
def get_price_for_specific_item():
    # Route For Checking the price for a specific item
    # Sample cURL: curl localhost:5000/get-price-for-specific-item -d '{"item": "Coke"}' -H 'Content-Type: application/json'
    # Expected Ourput: The price of that item. Here, $2.
    data = request.get_json()
    return jsonify(system.menu.get_price_for_specific_item(data['item']))


if __name__ == "__main__":
    welcome_pizza()
    system = System()
    app.run(debug=True, host='0.0.0.0')