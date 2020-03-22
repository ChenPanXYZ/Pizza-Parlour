from classes.Delivery import Delivery
from classes.Order import Order
from classes.Foodora import Foodora
from classes.Menu import Menu

sample_order = {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

# Assume menu is correct.
data = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

menu = Menu(data)

def test_new_foodora():
    new_order = Order(sample_order)
    foodora = Foodora(new_order)
    assert foodora.order_details == new_order 

# def test_toCSV():
#     new_order = Order(sample_order, menu)
#     foodora = Foodora(new_order)
#     result = foodora.toCSV()
#     expected = '1-1-L-pepperoni-mushrooms-1-olives-4-tomatoes-1,1-Pepsi-2,100 Street,26.5,1'
#     print(result)
#     assert result == expected

