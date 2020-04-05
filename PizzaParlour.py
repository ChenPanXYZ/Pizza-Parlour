from flask import Flask, make_response
from flask import jsonify
from flask import request
import json
from classes.System import System
app = Flask("Assignment 2")

system = System()
@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

# Order Part
@app.route('/make-a-new-order', methods = ['POST'])
def make_a_new_order():
    # curl localhost:5000/make-a-new-order -d '{}' -H 'Content-Type: application/json'
    new_order_number = system.make_a_new_order()
    system.update_data()
    return make_response(jsonify(new_order_number), 201)

@app.route('/check-order')
def check_order():
    # curl --request GET localhost:5000/check-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    if "order_number" not in data:
        return make_response('Invalid input', 400)
    order = system.find_order_by_order_number(data['order_number'])
    if order is None:
        return make_response('The Order Number doesn\'t exist.', 404)
    else:
        return make_response(jsonify(order.toJSON()), 200)

@app.route('/cancel-order', methods=['DELETE'])
def cancel_order():
    # curl --request DELETE localhost:5000/cancel-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("order_number" not in data) or (not isinstance(data["order_number"], int)):
        return make_response('Invalid input', 400)
    result = system.cancel_order(data['order_number'])
    system.update_data()

    if result == 404:
        return make_response('The Order Number doesn\'t exist.', 404)
    else:
        return make_response(jsonify(system.OrdersToJSON()), 200)


@app.route('/show-all-orders', methods = ['GET'])
def show_all_orders():
    # Sample cURL: curl localhost:5000/show-all-orders
    return make_response(jsonify(system.show_all_orders()), 200)

@app.route('/order-a-pizza', methods = ['PATCH'])
def order_a_pizza():
    # Route For Ordering a piazza
    # Sample cURL: curl --request PATCH localhost:5000/order-a-pizza -d '{"order_number": 1, "pizza": {"number": 1, "size": "S", "type": "vegetarian", "toppings": {}}}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("order_number" not in data) or (not isinstance(data["order_number"], int)) or ("pizza" not in data) or (not isinstance(data["pizza"], dict)) or ("number" not in data["pizza"]) or (not isinstance(data["pizza"]["number"], int)) or ("size" not in data["pizza"]) or (data["pizza"]["size"] not in system.menu.content["pizza"]["size"]) or ("type" not in data["pizza"]) or(data["pizza"]["type"] not in system.menu.content["pizza"]["type"]) or ("toppings" not in data["pizza"]) or (not isinstance(data["pizza"]["toppings"], dict)):
        return make_response('Invalid input', 400)
    
    for topping in data["pizza"]["toppings"]:
        if (topping not in system.menu.content["pizza"]["topping"]) or (not isinstance(data["pizza"]["toppings"][topping], int)):
            return make_response('Invalid input', 400)       

    order = system.find_order_by_order_number(data['order_number'])
    if order is None:
        return make_response('The Order Number doesn\'t exist.', 404)

    
    for topping in system.types[data['pizza']['type']]:
        if topping in data['pizza']['toppings']:
            data['pizza']['toppings'][topping] += system.types[data['pizza']['type']][topping]
        else:
            data['pizza']['toppings'][topping] = system.types[data['pizza']['type']][topping]

    added_pizza = order.add_pizza(data['pizza'], system.menu)
    system.update_data()
    return make_response(jsonify(added_pizza.toJSON()), 200)


@app.route('/order-a-drink', methods = ['PATCH'])
def order_a_drink():
    # Route For Ordering a drink (any number of it)
    # Sample cURL: curl --request PATCH localhost:5000/order-a-drink -d '{"order_number": 2, "drink": {"drink_name": "Diet Coke", "number": 5}}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("order_number" not in data) or (not isinstance(data["order_number"], int)) or ("drink" not in data) or (not isinstance(data["drink"], dict)) or ("drink_name" not in data["drink"]) or (data["drink"]["drink_name"] not in system.menu.content["drink"]) or ("number" not in data["drink"]) or (not isinstance(data["drink"]["number"], int)):
        return make_response('Invalid input', 400)
    order = system.find_order_by_order_number(data['order_number'])
    if order is None:
        return make_response('The Order Number doesn\'t exist.', 404)
    added_drink = order.add_drink(data["drink"], system.menu)
    system.update_data()
    return make_response(jsonify(added_drink.toJSON()), 200)

@app.route('/change-an-order', methods = ['PATCH'])
def change_an_order():
    # Route When the User wants to change the order.
    # Sample cURL: curl --request PATCH localhost:5000/change-an-order -d '{"order_number": 2, "pizzas": [{"item_id": 1, "size": "S", "type": "vegetarian"}], "drinks": []}' -H 'Content-Type: application/json'
    # User need to provide the order_number they want to change, the item_id for pizzas or drinks they are going to modify.
    # Note that since each pizza has a type, that has a specific preparation method. Hence, if the user is going to decreasing the toppings, we will check if it still meets the minimum requirement for that type of pizza. If not, we will send back a response that saying the update doesn't finish because the preparation method can not be done with those toppings.
    data = request.get_json()
    if ("order_number" not in data) or (not(isinstance(data["order_number"], int))) or ("pizzas" not in data) or (not(isinstance(data["pizzas"], list))) or ("drinks" not in data) or (not(isinstance(data["drinks"], list))):
         return make_response('Invalid input', 400)
    modified_order = system.change_an_order(data["order_number"], data['pizzas'], data['drinks'])
    if modified_order == None:
        return make_response('The Order Number doesn\'t exist.', 404)
    system.update_data()
    return make_response(modified_order.toJSON(), 200)


@app.route('/set-address', methods = ['PATCH'])
def set_address():
    # Route When the User set an address for his / her order.
    # Sample cURL: curl --request PATCH localhost:5000/set-address -d '{"order_number": 400, "address": "222 Street"}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("order_number" not in data) or ("address" not in data):
        return make_response('Invalid input', 400)
    order_number = data["order_number"]
    address = data["address"]
    order = system.find_order_by_order_number(data['order_number'])
    if order is None:
        return make_response('The Order Number doesn\'t exist.', 404)
    order.set_address(address)
    system.update_data()
    return make_response(order.toJSON(), 200)

@app.route('/set-delivery', methods = ['POST'])
def set_delivery():
    # curl localhost:5000/set-delivery -d '{"order_number": 1, "delivery": "uber"}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("order_number" not in data) or ("delivery" not in data) or not(data["delivery"] == "uber" or data["delivery"] == "foodora"):
        return make_response('Invalid input', 400)
    order_number = data["order_number"]
    order = system.find_order_by_order_number(order_number)
    if order is None:
        return make_response('The Order Number doesn\'t exist.', 404)
    delivery = data["delivery"]
    new_delivery_id = ""
    if(delivery == "uber"):
        new_delivery_id = system.add_uber(order)
    elif(delivery == "foodora"):
        new_delivery_id = system.add_foodora(order)
    system.update_data()
    return make_response(new_delivery_id, 200)

# Menu Part
@app.route('/get-full-menu')
def get_full_menu():
    # Route For Get the Full Menu
    # Sample cURL: curl localhost:5000/get-full-menu
    # Expected Output: JSON contains infomation of the menu.

    return make_response(jsonify(system.menu.get_full_content()), 200)

@app.route('/get-price-for-specific-item')
def get_price_for_specific_item():
    # Route For Checking the price for a specific item
    # Sample cURL: curl --request GET localhost:5000/get-price-for-specific-item -d '{"item2": []}' -H 'Content-Type: application/json'
    # Expected Ourput: The price of that item. Here, $2.
    data = request.get_json()
    if ("item" not in data) or (not isinstance(data["item"], str)):
        return make_response('Invalid input', 400)
    result = system.menu.get_price_for_specific_item(data['item'])
    if result == -1:
        return make_response("The Item doesn\'t exist.", 404)
    else:
        return make_response(jsonify(system.menu.get_price_for_specific_item(data['item'])), 200)

@app.route('/add-new-type', methods = ['POST'])
def add_new_type():
    # Route for adding a new type.
    # curl localhost:5000/add-new-type -d '{"name": "New", "method": {"beef": 9, "chicken": 1}}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("name" not in data) or (not isinstance(data["name"], str)) or ("method" not in data) or (not isinstance(data["method"], dict)):
        return make_response('Invalid input', 400)
    for topping in data["method"]:
        if (topping not in system.menu.content["pizza"]["topping"]) or (not isinstance(data["method"][topping], int)):
            return make_response('Invalid input', 400)
    result = system.add_new_type(data)
    return make_response(jsonify(result), 201)

@app.route('/change-price-for-item', methods = ['PATCH'])
def change_price_for_item():
    # curl --request PATCH localhost:5000/change-price-for-item -d '{"item": "olives", "price": 5}' -H 'Content-Type: application/json'
    data = request.get_json()
    if ("item" not in data) or (not isinstance(data["item"], str)) or ("price" not in data) or (not isinstance(data["price"], (int, float))):
        return make_response('Invalid input', 400)
    result = system.menu.change_price_for_item(data["item"], data["price"], system.types)
    if result == 404:
        return make_response("The Item doesn\'t exist.", 404)
    else:
        system.update_data()
        system.file_dealer.write_to_menu(system.menu.content)
        return make_response(jsonify(system.menu.content), 200)


if __name__ == "__main__":
    welcome_pizza()
    system.update_data()
    app.run(debug=True, host='0.0.0.0')