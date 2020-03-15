from flask import Flask
from flask import request
import json
import csv

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


@app.route('/test', methods=['POST'])
def test():
    foodora_deliveries = {}
    with open('foodora.csv', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            delivery_id_info = row[0]
            address_info = row[1]
            pizzas_info = row[2]
            drinks_info = row[3]
            order_address_info = row[4]
            order_price = row[5]

            pizzas_info = pizzas_info.split("|")

            pizzas = []
            for pizza_info in pizzas_info:
                pizza_info = pizza_info.split("-")
                pizza = {}
                pizza['item_id'] = pizza_info[0]
                pizza['size'] = pizza_info[1]
                pizza['type'] = pizza_info[2]
                pizza['toppings'] = {}
                i = 3
                while i < len(pizza_info) - 1:
                    pizza['toppings'][pizza_info[i]] = pizza_info[i+1]
                    i = i + 2

                pizzas.append(pizza)
            drinks = []
            drinks_info = drinks_info.split("|")
            for drink_info in drinks_info:
                drink_info = drink_info.split("-")
                drink = {}
                drink['item_id'] = drink_info[0]
                drink[drink_info[1]] = drink_info[2]
                drinks.append(drink)

            foodora_deliveries[delivery_id_info] = {}
            foodora_deliveries[delivery_id_info]['address'] = address_info
            foodora_deliveries[delivery_id_info]['order_details'] = {}
            foodora_deliveries[delivery_id_info]['order_details']['pizzas'] = pizzas
            foodora_deliveries[delivery_id_info]['order_details']['drinks'] = drinks
            foodora_deliveries[delivery_id_info]['order_details']['drinks'] = drinks
            foodora_deliveries[delivery_id_info]['order_details']['address'] = order_address_info
            foodora_deliveries[delivery_id_info]['order_details']['price'] = order_price
            
    return foodora_deliveries

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
    system.update_data()
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
    order_number = data['order_number']
    order = system.orders.details[order_number]
    order.add_pizza(data['pizza'], system.menu)
    system.update_data()
    return order.toJSON()

@app.route('/order-a-drink', methods = ['POST'])
def order_a_drink():
    # curl localhost:5000/order-a-drink -d '{"order_number": 2, "drink": {"type": "Diet Coke", "number": 2}}' -H 'Content-Type: application/json'
    data = request.get_json()
    order_number = data['order_number']
    order = system.orders.details[order_number]
    order.add_drink(data['drink']['type'], data['drink']['number'], system.menu)
    system.update_data()
    return order.toJSON()


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


    system.update_data()


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
    order = system.orders.details[order_number]
    delivery = data["delivery"]
    if(delivery == "uber"):
        system.add_uber(order)
    elif(delivery == "foodora"):
        return
    system.update_data()
    return 'success'

@app.route('/check-all-uber-delivery', methods = ['POST'])
def check_all_uber_delivery():
    return system.deliveriesTOJSON()














# curl localhost:5000/new-order -d '{"pizzas": [{"size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}], "drinks": {"Coke": 1, "Diet Coke":2, "Coke Zero":3}}' -H 'Content-Type: application/json'

if __name__ == "__main__":
    welcome_pizza()
    system = System()
    app.run(debug=True, host='0.0.0.0')