import json
from classes.Item import Item
from classes.Pizza import Pizza
from classes.Drink import Drink
class Order:
    def __init__(this, order, menu=None):
        if menu is None:
            # Make a new Order
            this.order_number = order["order_number"]
            this.price = 0
            this.address = ""
            this.pizzas = []
            this.drinks = []
        else:
            # Recover order from database
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
                new_pizza["item_id"] = this.unique_key_maker(this.pizzas)
            pizza = Pizza(new_pizza)
            this.price += pizza.get_price(menu)
            this.pizzas.append(pizza)

    def check_pizza_already_exist(this, new_pizza):
        for pizza in this.pizzas:
            if pizza.type == new_pizza['type'] and pizza.size == new_pizza['size'] and pizza.toppings == new_pizza['toppings']:
                return pizza
        return None

    def change_pizza(this, change_pizza, menu, method):
        for pizza in this.pizzas:
            if pizza.item_id == change_pizza['item_id']:
                this.price -= pizza.get_price(menu)
                if "size" in change_pizza:
                    pizza.size = change_pizza["size"]
                if "type" in change_pizza:
                    # Since type is changed, need to change 
                    for topping in pizza.toppings:
                        if topping in method[pizza.type]:
                            pizza.toppings[topping] -= method[pizza.type][topping]
                            if pizza.toppings[topping] == 0:
                                pizza.toppings.remove(topping)
                    for topping in method[pizza.type]:
                        if topping not in pizza.toppings:
                            pizza.toppings[topping] = method[pizza.type][topping]
                        else:
                            pizza.toppings[topping] += method[pizza.type][topping]
                if "toppings" in change_pizza:
                    # Extra toppings
                    for topping in change_pizza["toppings"]:
                        if topping not in pizza.toppings:
                            pizza.toppings[topping] = change_pizza["toppings"][topping]
                        else:
                            pizza.toppings[topping] = change_pizza["toppings"][topping]
                            if pizza.toppings[topping] == 0 and topping not in method[pizza.type]:
                                del pizza.toppings[topping]
                            elif pizza.toppings[topping] == 0 and topping in method[pizza.type]:
                                pizza.toppings[topping] = method[pizza.type][topping]
                if "number" in change_pizza:
                    pizza.number = change_pizza["number"]
                    if pizza.number == 0:
                        this.pizzas.remove(pizza)
                        return
                this.price += pizza.get_price(menu)
                return

        

    # Drink Part
    def add_drink(this, new_drink, menu):
        drink = this.check_drink_already_exist(new_drink)
        if drink != None:
            this.price -= drink.get_price(menu)
            drink.number += new_drink["number"]
            this.price += drink.get_price(menu)
            return "Added Successfully."
        else:
            if("item_id" not in new_drink):
                new_drink["item_id"] = this.unique_key_maker(this.drinks)
            drink = Drink(new_drink)
            this.price += drink.get_price(menu)
            this.drinks.append(drink)

    def check_drink_already_exist(this, new_drink):
        for drink in this.drinks:
            if(drink.type == new_drink["drink_name"]):
                return drink
        return None

    def change_drink(this, change_drink, menu, type):
        for drink in this.drinks:
            if drink.item_id == change_drink['item_id']:
                this.price -= drink.get_price(menu)
                drink.number = change_drink['number']
                this.price += drink.get_price(menu)
                if drink.number == 0:
                    this.drinks.remove(drink)
                return

    
    def unique_key_maker(this, dict_list):
        # The list consists of dicts.
        if(not dict_list):
            return 1
        else:
            return max(dict_list, key=lambda item: item.item_id).item_id + 1

    # Set Adress
    def set_address(this, address):
        this.address = address

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

    def toCSV(this):
        result = ''
        i = 0
        for pizza in this.pizzas:
            result += pizza.toCSV()
            if(i != len(this.pizzas) - 1):
                result += '|'
            
            i = i + 1


        result = result + ','
        i = 0
        for drink in this.drinks:
            result+= drink.toCSV()
            if(i != len(this.drinks) - 1):
                result += '|'
            
            i = i + 1

        result = result + ','

        result = result + this.address + "," + str(this.price) + "," + str(this.order_number)
        return result



    