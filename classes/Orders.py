import json
from classes.Pizza import Pizza
from classes.Drink import Drink
from classes.Item import Item
from classes.Order import Order
class Orders:
    def __init__(this, menu):
        this.details = {}
        orders = {}
        with open('orders.json', 'r') as f:
            orders = json.load(f)

        for order_num in orders:
            order = orders[order_num]
            this.details[int(order_num)] = Order(int(order_num))
            for pizza in order["pizzas"]:
                this.details[int(order_num)].add_pizza(pizza, menu)

            for drink in order["drinks"]:
                this.details[int(order_num)].add_drink(drink, order["drinks"][drink], menu)

    def add_new_order(this):
        if(not this.details):
            # No Order in Orders.json
            new_order_number = 1
        else:
            new_order_number = max(this.details, key=int) + 1
        this.details[new_order_number] = Order(new_order_number)
    
    def toJSON(this):
        result = {}
        for order_num in this.details:
            result[order_num] = this.details[order_num].toJSON()
        return result