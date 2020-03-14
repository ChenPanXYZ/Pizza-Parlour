from flask import Flask
from flask import request
import json

from classes.Test import Test
from classes.Menu import Menu
from classes.System import System
from classes.Orders import Orders
app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    print("hello")
    return 'Welcome to Pizza Planet!'

@app.route('/get-full-menu', methods=['GET'])
def get_full_menu():
    # curl localhost:5000/get-full-menu
    return system.menu.get_full_content()

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

@app.route('/new-order', methods=['POST'])
def new_order():
    data = request.get_json()
    pizzas = data['pizzas'] ## This is an array of all pizza.
    drinks = data['drinks'] ## This is an array of all drinks.
    total_price = 0
    for pizza in pizzas:
        this_pizza_price = 0
        this_pizza_size = pizza['size']

        this_pizza_type = pizza['type']
        this_pizza_type_price = get_price(this_pizza_type)

        this_pizza_price += this_pizza_type_price
        # toppings price "toppings": [{"olives": 2}, {"tomatoes": 1}]}]
        this_pizza_topping = pizza['toppings']
        toppings_price = 0
        for topping in this_pizza_topping.keys():
            toppings_price += get_price(topping) * this_pizza_topping[topping]
        this_pizza_price += toppings_price
   
        if(this_pizza_size == "S"):
            this_pizza_price *= 0.8
        elif(this_pizza_size == "L"):
            this_pizza_price *= 1.5
        total_price += this_pizza_price

    for drink in drinks.keys():

        total_price += get_price(drink) * drinks[drink]

    return {"price": total_price}


# curl localhost:5000/new-order -d '{"pizzas": [{"size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}], "drinks": {"Coke": 1, "Diet Coke":2, "Coke Zero":3}}' -H 'Content-Type: application/json'

def get_price(item):
    prices = {}
    with open('price.json', 'r') as f:
        prices = json.load(f)
    return prices[item]

if __name__ == "__main__":
    welcome_pizza()
    system = System()


    # order = Orders()从orders.json中读取数据
    app.run(debug=True, host='0.0.0.0')