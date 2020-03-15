from flask import Flask
from flask import request
import json

from classes.Test import Test
from classes.Menu import Menu
from classes.System import System
from classes.Orders import Orders
from classes.Order import Order
app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    print("hello")
    return 'Welcome to Pizza Planet!'

@app.route('/get-full-menu', methods=['GET'])
def get_full_menu():
    # curl localhost:5000/get-full-menu
    return system.menu.get_full_content()

@app.route('/check-order', methods=['POST'])
def check_order():
    # curl localhost:5000/check-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data['order_number']
    return system.orders.details[order_number].toJSON()

@app.route('/cancel-order', methods=['POST'])
def cancel_order():
    # curl localhost:5000/cancel-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data['order_number']
    system.orders.details.pop(order_number)
    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)
    return 'success'

@app.route('/get-price-for-specific-item', methods=['POST'])
def get_price_for_specific_item():
    data = request.get_json()
    item = data["item"]
    if item in system.menu.content['pizza']['size']:
        return {"price": system.menu.content['pizza']['size'][item]}
    elif item in system.menu.content['pizza']['type']:
        return {"price": system.menu.content['pizza']['type'][item]}
    elif item in system.menu.content['pizza']['topping']:
        return {"price": system.menu.content['pizza']['topping'][item]}
    elif item in system.menu.content['pizza']['drink']:
        return {"price": system.menu.content['pizza']['drink'][item]}
    else:
        return {"price": -1} # tell the fron-end that this item doesn't exist

@app.route('/show-orders', methods = ['GET'])
def show_orders():
    return {"orders":Orders().get_all_orders()}

@app.route('/make-new-order', methods = ['POST'])
def make_new_order():
# curl localhost:5000/make-new-order -d '{}'
    system.orders.add_new_order()
    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)
    return 'success'

@app.route('/order-a-pizza', methods = ['POST'])
def order_a_pizza():
    # curl localhost:5000/order-a-pizza -d '{"order_number": 1, "pizza": {"number": 2, "size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}}' -H 'Content-Type: application/json'
    data = request.get_json()
    order = system.orders.details[data["order_number"]]
    order.add_pizza(data['pizza'], system.menu)
    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)
    return 'success'

@app.route('/order-a-drink', methods = ['POST'])
def order_a_drink():
    # curl localhost:5000/order-a-drink -d '{"order_number": 1, "drink": {"type": "Diet Coke", "number": 2}}' -H 'Content-Type: application/json'
    data = request.get_json()
    order = system.orders.details[data["order_number"]]
    order.add_drink(data['drink']['type'], data['drink']['number'], system.menu)
    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)
    return 'success'


@app.route('/add-new-type', methods = ['POST'])
def add_new_type():
    # curl localhost:5000/add-new-type -d '{"typename": "Yuwan", "price": 2}' -H 'Content-Type: application/json'
    data = request.get_json()
    typename = data["typename"]
    price = data["price"]
    system.menu.content['pizza']['type'][typename] = price
    with open('menu.json', 'w') as f:
        json.dump(system.menu.toJSON(), f)
    return 'success'

@app.route('/change-an-order', methods = ['POST'])
def change_an_order():
    # curl localhost:5000/change-an-order -d '{"order_number": 1, "pizzas": [{"item_id": 1, "size": "L", "toppings": {"olives" : 0}}]}' -H 'Content-Type: application/json'

    data = request.get_json()
    order_number = data["order_number"]
    order = system.orders.details[order_number]
    changed_drinks = []
    changed_pizzas = []
    if "drinks" in data:
        changed_drinks = data["drinks"]
    if "pizzas" in data:
        changed_pizzas = data["pizzas"]


    for drink in changed_drinks:
        order.change_drink(drink, system.menu)
    
    for pizza in changed_pizzas:
        order.change_pizza(pizza, system.menu)


    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)


    return 'success'

@app.route('/set-address', methods = ['POST'])
def set_address():
    # curl localhost:5000/set-address -d '{"order_number": 1, "address": "855 dgsdg"}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data["order_number"]
    address = data["address"]
    system.orders.details[order_number].set_address(address)
    with open('orders.json', 'w') as f:
        json.dump(system.orders.toJSON(), f)
    return 'success'

@app.route('/set-delivery', methods = ['POST'])
def set_delivery():
    # curl localhost:5000/set-delivery -d '{"order_number": 1, "delivery": "uber"}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data["order_number"]
    delivery = data["delivery"]
    if(delivery == "uber"):
        return
    elif(delivery == "foodora"):
        return













# curl localhost:5000/new-order -d '{"pizzas": [{"size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}], "drinks": {"Coke": 1, "Diet Coke":2, "Coke Zero":3}}' -H 'Content-Type: application/json'

if __name__ == "__main__":
    welcome_pizza()
    system = System()
    app.run(debug=True, host='0.0.0.0')