import json
from classes.Order import Order
from classes.Item import Item
from classes.Pizza import Pizza
from classes.Drink import Drink
from classes.Menu import Menu

sample_order = {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

# Assume menu is correct.
data = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

menu = Menu(data)

types = {"pepperoni": {"olives": 2, "mushrooms": 1}, "margherita": {"chicken": 3}, "vegetarian": {"jalapenos": 2, "pepperoni": 1}, "Neapolitan": {"beef": 2}, "New": {"beef": 10, "chicken": 1}}

def test_make_a_new_order():
    new_order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    assert new_order.order_number == 2
    assert new_order.pizzas == []
    assert new_order.drinks == []
    assert new_order.address == ""
    assert new_order.price == 0

def test_toJSON():
    new_order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    assert new_order.toJSON() == {"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": 0}

def test_recover_an_order():
    order = Order(sample_order, menu)
    assert order.toJSON() == {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

def test_set_address():
    order = Order(sample_order, menu)
    order.set_address("300 Street")
    assert order.address == "300 Street"

def test_add_pizza():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    pizza = {"size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    order.add_pizza(pizza, menu)
    assert order.toJSON() == {"order_number": 2, "pizzas": [{"item_id": 1, "size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}], "drinks": [], "address": "", "price": 6}

def test_add_drink():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    drink = {"drink_name": "Coke", "number": 3}
    order.add_drink(drink, menu)
    assert order.toJSON() == {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Coke", "number": 3}], "address": "", "price": 6}

def test_check_pizza_already_exist():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    pizza = {"size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    order.add_pizza(pizza, menu)
    result = order.check_pizza_already_exist(pizza)
    assert result != None
    pizza = {"size": "M", "type": "pepperoni", "toppings": {"olives": 1}, "number": 1}
    result = order.check_pizza_already_exist(pizza)
    assert result == None

def test_check_drink_already_exist():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    drink = {"drink_name": "Coke", "number": 2}
    order.add_drink(drink, menu)
    result = order.check_drink_already_exist(drink)
    assert result != None
    drink = {"drink_name": "Coke", "number": 1}
    result = order.check_drink_already_exist(drink)
    assert result != None
    drink = {"drink_name": "Diet Coke", "number": 1}
    result = order.check_drink_already_exist(drink)
    assert result == None

def test_change_pizza():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    pizza = {"size": "M", "type": "pepperoni", "toppings": {"olives": 2, "mushrooms": 1}, "number": 1}
    order.add_pizza(pizza, menu)
    order.change_pizza({"item_id": 1, "size": "L", "toppings": {"olives": 0}}, menu, types)

    expected = {"order_number": 2, "pizzas": [{"item_id": 1, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "mushrooms": 1}, "number":1 }], "drinks": [], "address": "", "price": 12.0}

    assert order.toJSON() == expected

    order.change_pizza({"item_id": 1, "size": "L", "toppings": {"olives": 3}}, menu, types)

    expected = {"order_number": 2, "pizzas": [{"item_id": 1, "size": "L", "type": "pepperoni", "toppings": {"olives": 3, "mushrooms": 1}, "number":1 }], "drinks": [], "address": "", "price": 16.5}

    assert order.toJSON() == expected

def test_change_drink():
    order = Order({"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": ""})
    drink = {"drink_name": "Coke", "number": 2}
    order.add_drink(drink, menu)
    order.change_drink({"item_id": 1, "number": 10}, menu, types)

    expected = {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Coke", "number": 10}], "address": "", "price": 20}

    order.change_drink({"item_id": 1, "number": 0}, menu, types)

    expected = {"order_number": 2, "pizzas": [], "drinks": [], "address": "", "price": 0}

    assert order.toJSON() == expected



