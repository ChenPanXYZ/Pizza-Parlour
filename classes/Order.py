import json
from classes.Pizza import Pizza
from classes.Drink import Drink
from classes.Item import Item

class Order:
    def __init__(this, order_number):
        this.pizzas = []
        this.drinks = []
        this.order_number = order_number
        this.price = 0
        this.address = ''

    def add_pizza(this, new_pizza, menu):
        for pizza in this.pizzas:
            if(pizza.type == new_pizza['type'] and pizza.size == new_pizza['size'] and pizza.toppings == new_pizza['toppings']):
                this.price -= pizza.get_price(menu)
                pizza.number += new_pizza["number"]
                this.price += pizza.get_price(menu)
                return

        new_item_id = (len(this.pizzas) + 1)

        new_pizza = Pizza(new_pizza, new_item_id)
        this.price += new_pizza.get_price(menu)
        this.pizzas.append(new_pizza)

    def change_pizza(this, changed_pizza, menu):
        for pizza in this.pizzas:
            if (pizza.item_id == changed_pizza["item_id"]):
                this.price -= pizza.get_price(menu)
                if "size" in changed_pizza:
                    pizza.size = changed_pizza["size"]
                if "type" in changed_pizza:
                    pizza.type = changed_pizza["type"]
                if "toppings" in changed_pizza:
                    for topping in changed_pizza["toppings"]:
                        pizza.toppings[topping] = changed_pizza["toppings"][topping]
                        if pizza.toppings[topping] == 0:
                            pizza.toppings.pop(topping)
                if "number" in changed_pizza:
                    pizza.number = changed_pizza["number"]

                this.price += pizza.get_price(menu)
                if pizza.number == 0:
                    this.pizzas.remove(pizza)
                return
                

    def add_drink(this, type, number, menu):
        for drink in this.drinks:
            if (drink.type == type):
                this.price -= drink.get_price(menu)
                drink.number += number
                this.price += drink.get_price(menu)
                return

        new_item_id = (len(this.drinks) + 1)
        new_drink = Drink(type, number, new_item_id)
        this.price += new_drink.get_price(menu)
        this.drinks.append(new_drink)

    def change_drink(this, changed_drink, menu):
        for drink in this.drinks:
            if (drink.item_id == changed_drink["item_id"]):
                this.price -= drink.get_price(menu)
                drink.number = changed_drink["number"]
                this.price += drink.get_price(menu)
                if drink.number == 0:
                    this.drinks.remove(drink)
                return

    def set_address(this, address):
        this.address = address

    def toJSON(this):
        result = {}
        result['pizzas'] = []
        for pizza in this.pizzas:
            result['pizzas'].append(pizza.toJSON())
        result['drinks'] = {}
        for drink in this.drinks:
            result['drinks'][drink.type] = drink.number
            result['drinks']['item id'] = drink.item_id
        result['address'] = this.address
        result['price'] = this.price
        return result