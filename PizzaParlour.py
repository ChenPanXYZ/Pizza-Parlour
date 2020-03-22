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
@app.route('/make-a-new-order', methods = ['POST'])
def make_a_new_order():
    # curl localhost:5000/make-a-new-order -d '{}' -H 'Content-Type: application/json'
    new_order_number = system.make_a_new_order()
    system.update_data()
    return jsonify(new_order_number)

@app.route('/check-order', methods=['POST'])
def check_order():
    # curl localhost:5000/check-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    order = system.find_order_by_order_number(data['order_number'])
    return order.toJSON()

@app.route('/cancel-order', methods=['POST'])
def cancel_order():
    # curl localhost:5000/cancel-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    system.cancel_order(data['order_number'])
    system.update_data()
    return 'Cancelled'


@app.route('/show-all-orders', methods = ['GET'])
def show_all_orders():
    # Sample cURL: curl localhost:5000/show-all-orders
    return jsonify(system.show_all_orders())

@app.route('/order-a-pizza', methods = ['POST'])
def order_a_pizza():
    # Route For Ordering a piazza
    # Sample cURL: curl localhost:5000/order-a-pizza -d '{"order_number": 3, "pizza": {"number": 1, "size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1}}}' -H 'Content-Type: application/json'
    data = request.get_json()
    order = system.find_order_by_order_number(data['order_number'])

    
    for topping in system.types[data['pizza']['type']]:
        if topping in data['pizza']['toppings']:
            data['pizza']['toppings'][topping] += system.types[data['pizza']['type']][topping]
        else:
            data['pizza']['toppings'][topping] = system.types[data['pizza']['type']][topping]

    order.add_pizza(data['pizza'], system.menu)
    system.update_data()
    return jsonify(data['order_number'])


@app.route('/order-a-drink', methods = ['POST'])
def order_a_drink():
    # Route For Ordering a drink (any number of it)
    # Sample cURL: curl localhost:5000/order-a-drink -d '{"order_number": 2, "drink": {"drink_name": "Diet Coke", "number": 5}}' -H 'Content-Type: application/json'
    data = request.get_json()
    order = {}
    for old_order in system.orders:
        if old_order.order_number == data["order_number"]:
            order = old_order
    order.add_drink(data["drink"], system.menu)
    system.update_data()
    return jsonify(data["order_number"])


@app.route('/change-an-order', methods = ['POST'])
def change_an_order():
    # Route When the User wants to change the order.
    # Sample cURL: curl localhost:5000/change-an-order -d '{"order_number": 1, "pizzas": [{"item_id": 1, "size": "L", "toppings": {"olives": 0}}], "drinks": []}' -H 'Content-Type: application/json'
    # User need to provide the order_number they want to change, the item_id for pizzas or drinks they are going to modify.
    # Note that since each pizza has a type, that has a specific preparation method. Hence, if the user is going to decreasing the toppings, we will check if it still meets the minimum requirement for that type of pizza. If not, we will send back a response that saying the update doesn't finish because the preparation method can not be done with those toppings.
    data = request.get_json()
    modified_order = system.change_an_order(data["order_number"], data['pizzas'], data['drinks'])
    system.update_data()
    return modified_order.toJSON()


@app.route('/set-address', methods = ['POST'])
def set_address():
    # Route When the User set an address for his / her order.
    # Sample cURL: curl localhost:5000/set-address -d '{"order_number": 1, "address": "222 Street"}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data["order_number"]
    address = data["address"]
    order = {}
    for old_order in system.orders:
        if old_order.order_number == data["order_number"]:
            order = old_order
    order.set_address(address)
    system.update_data()
    return 'success'

@app.route('/set-delivery', methods = ['POST'])
def set_delivery():
    # curl localhost:5000/set-delivery -d '{"order_number": 3, "delivery": "uber"}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data["order_number"]
    order = system.find_order_by_order_number(order_number)
    delivery = data["delivery"]
    if(delivery == "uber"):
        system.add_uber(order)
    elif(delivery == "foodora"):
        system.add_foodora(order)
    system.update_data()
    return 'success'


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


@app.route('/add-new-type', methods = ['POST'])
def add_new_type():
    # Route for adding a new type.
    # curl localhost:5000/add-new-type -d '{"name": "New", "method": {"beef": 10, "chicken": 1}}' -H 'Content-Type: application/json'
    data = request.get_json()
    system.add_new_type(data)
    return jsonify(data)

@app.route('/change-price-for-item', methods = ['POST'])
def change_price_for_item():
    # curl localhost:5000/change-price-for-item -d '{"item": "olives", "price": 5}' -H 'Content-Type: application/json'
    data = request.get_json()
    system.menu.change_price_for_item(data["item"], data["price"], system.types)
    system.update_data()
    system.file_dealer.write_to_menu(system.menu.toJSON())
    return "success"


if __name__ == "__main__":
    welcome_pizza()
    system = System()
    system.update_data()
    app.run(debug=True, host='0.0.0.0')