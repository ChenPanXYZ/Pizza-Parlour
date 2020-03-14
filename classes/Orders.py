import json
from classes.Pizza import Pizza
from classes.Drink import Drink
from classes.Item import Item
class Orders:
    def __init__(this):
        this.orders = {}
        order_json = {}
        with open('orders.json', 'r') as f:
            order_json = json.load(f)
        for num in order_json:
            this.orders[num] = {}
            this_order = this.orders[num]
            pizzas = order_json[num]["pizzas"]
            this_order["pizzas"] = []
            for pizza in pizzas:
                this_pizza = Pizza(pizza)
                this_order["pizzas"].append(this_pizza)
            drinks = order_json[num]["drinks"]
            this_order["drinks"] = []
            for drink in drinks:
                this_drink = Drink(drink)
                this_order["drinks"].append(this_drink)
    def get_all_orders(this):
        return this.orders



          
            

        
#   this.content ==所有order
    
#    读orders.js，
#    for loop

#    this.content["order number": ====== new Order(order)]