from classes.Item import Item
from classes.Pizza import Pizza
from classes.Menu import Menu
# Assume menu is correct.
data = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

menu = Menu(data)
def test_new_drink():
    pizza = {"item_id": 1, "size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    new_pizza = Pizza(pizza)
    assert new_pizza.item_id == 1
    assert new_pizza.size == "M"
    assert new_pizza.type == "pepperoni"
    assert new_pizza.toppings == {"olives": 2}
    assert new_pizza.number == 1

def test_get_price():
    pizza = {"item_id": 1, "size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    new_pizza = Pizza(pizza)
    price = new_pizza.get_price(menu)
    assert price == 6.0

def test_to_json():
    pizza = {"item_id": 1, "size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    new_pizza = Pizza(pizza)
    result = new_pizza.toJSON()
    expected = {'item_id': 1, 'number': 1, 'size': 'M', 'toppings': {'olives': 2}, 'type': "pepperoni"}
    assert result == expected

def test_toCSV():
    pizza = {"item_id": 1, "size": "M", "type": "pepperoni", "toppings": {"olives": 2}, "number": 1}
    new_pizza = Pizza(pizza)
    result = new_pizza.toCSV()
    expected = '1-1-M-pepperoni-olives-2'
    assert result == expected