import json
from classes.Item import Item
from classes.Pizza import Pizza
from classes.Drink import Drink
class Order:
    def __init__(this, order, menu):
        this.order_number = order["order_number"]
        this.price = 0
        this.address = order["address"]
        this.pizzas = []
        this.drinks = []
        for pizza in order["pizzas"]:
            this.add_pizza(pizza, menu)
        for drink in order["drinks"]:
            this.add_drink(drink, menu)

    
    # Pizza Part
    def add_pizza(this, new_pizza, menu):
        pizza = this.check_pizza_already_exist(new_pizza)
        if pizza != None:
            this.price -= pizza.get_price(menu)
            pizza.number += new_pizza["number"]
            this.price += pizza.get_price(menu)
            return "Added Successfully."
        else:
            # Register a new pizza
            if("item_id" not in new_pizza):
                new_pizza["item_id"] = unique_key_maker(this.pizzas)
            pizza = Pizza(new_pizza)
            this.price += pizza.get_price(menu)
            this.pizzas.append(pizza)

    def check_pizza_already_exist(this, new_pizza):
        for pizza in this.pizzas:
            if pizza.type == new_pizza['type'] and pizza.size == new_pizza['size'] and pizza.toppings == new_pizza['toppings']:
                return pizza
        return None
        

    # Drink Part
    def add_drink(this, new_drink, menu):
        drink = this.check_drink_already_exist(new_drink)
        if drink != None:
            this.price -= drink.get_price(menu)
            drink.number += drink["number"]
            this.price += drink.get_price(menu)
            return "Added Successfully."
        else:
            if("item_id" not in new_drink):
                new_drink["item_id"] = unique_key_maker(this.drinks)
            drink = Drink(new_drink)
            this.price += drink.get_price(menu)
            this.drinks.append(drink)

    def check_drink_already_exist(this, new_drink):
        for drink in this.drinks:
            if(drink.type == new_drink["drink_name"]):
                return drink
        return None

    
    def unique_key_maker(dict_list):
        # The list consists of dicts.
        seq = [x["item_id"] for x in dict_list]
        return max(seq) + 1

    def toJSON(this):
        result = {}
        result["order_number"] = this.order_number
        result['pizzas'] = []
        for pizza in this.pizzas:
            result['pizzas'].append(pizza.toJSON())
        result['drinks'] = []
        for drink in this.drinks:
            result['drinks'].append(drink.toJSON())
        result['address'] = this.address
        result['price'] = this.price
        return result



    