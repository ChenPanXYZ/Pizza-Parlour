from classes.System import System
from classes.Menu import Menu
from classes.FileDealer import FileDealer

def test_new_system():
    system = System()
    assert isinstance(system.menu, Menu)
    assert isinstance(system.file_dealer, FileDealer)
    assert len(system.orders) == 3
    assert system.types == {"pepperonis": {"olives": 2, "mushrooms": 1}, "margherita": {"chicken": 3}, "vegetarian": {"jalapenos": 2, "pepperoni": 1}, "Neapolitan": {"beef": 2}}
    assert len(system.deliveries["uber"]) == 1
    assert len(system.deliveries["foodora"]) == 1

def test_add_new_type():
    system = System()
    system.add_new_type({"name": "New Type", "method": {"beef": 3}})
    assert system.types == {"pepperonis": {"olives": 2, "mushrooms": 1}, "margherita": {"chicken": 3}, "vegetarian": {"jalapenos": 2, "pepperoni": 1}, "Neapolitan": {"beef": 2}, "New Type": {"beef": 3}}

def test_make_a_new_order():
    system = System()
    system.make_a_new_order()
    assert len(system.orders) == 4

def test_OrdersToJSON():
    system = System()
    assert system.OrdersToJSON() == [{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}, {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}]

def test_find_order_by_order_number():
    system = System()
    order = system.find_order_by_order_number(1)
    assert order.toJSON() == {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

def test_change_an_order():
    system = System()
    system.change_an_order(1, [], [{"item_id": 1, "drink_name": "Pepsi", "number": 0}])
    assert system.OrdersToJSON() == [{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [], "address": "100 Street", "price": 22.5}, {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}]

def test_cancel_order():
    system = System()
    system.cancel_order(1)
    assert system.OrdersToJSON() == [{"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}]

def test_uber_deliveries_toJSON():
    system = System()
    assert system.uber_deliveries_toJSON() == {"Uber-1": {"order_details": {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}}}

def test_add_uber():
    system = System()
    order = system.find_order_by_order_number(2)
    system.add_uber(order)
    assert system.uber_deliveries_toJSON() == {'Uber-1': {'order_details': {'price': 24.0, 'pizzas': [{'item_id': 1, 'toppings': {'chicken': 3, 'beef': 2, 'tomatoes': 1}, 'type': 'margherita', 'number': 1, 'size': 'L'}], 'order_number': 3, 'address': '200 Street', 'drinks': []}}, 'Uber-2': {'order_details': {'price': 15, 'pizzas': [], 'order_number': 2, 'address': '', 'drinks': [{'item_id': 1, 'number': 5, 'drink_name': 'Diet Coke'}]}}}

# def test_foodora_deliveries_toCSV():
#     system = System()
#     assert system.foodora_deliveries_toCSV() == ['Foodora-1,1-1-L-pepperoni-mushrooms-1-olives-4-tomatoes-1,1-Pepsi-2,100 Street,26.5,1']

# def test_add_foodora():
#     system = System()
#     order = system.find_order_by_order_number(2)
#     system.add_foodora(order)
#     assert system.foodora_deliveries_toCSV() == ['Foodora-2,,1-Diet Coke-5,,15,2', 'Foodora-1,1-1-L-pepperoni-mushrooms-1-olives-4-tomatoes-1,1-Pepsi-2,100 Street,26.5,1']