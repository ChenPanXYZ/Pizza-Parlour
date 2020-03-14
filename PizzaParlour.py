from flask import Flask
from flask import request
import json

app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    print("hello")
    return 'Welcome to Pizza Planet!'

@app.route('/test', methods=['GET', 'POST'])
def test():
    return request.get_json()

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
    app.run()