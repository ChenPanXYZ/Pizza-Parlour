from classes.Item import Item
from classes.Drink import Drink
from classes.Menu import Menu
# Assume menu is correct.
data = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

menu = Menu(data)
def test_new_drink():
    drink = {"item_id": 1, "drink_name": "Coke", "number": 3}
    new_drink = Drink(drink)
    assert new_drink.item_id == 1
    assert new_drink.type == "Coke"
    assert new_drink.number == 3

def test_get_price():
    drink = {"item_id": 1, "drink_name": "Coke", "number": 3}
    new_drink = Drink(drink)
    assert new_drink.get_price(menu) == 6

def test_to_json():
    drink = {"item_id": 1, "drink_name": "Coke", "number": 3}
    new_drink = Drink(drink)
    result = new_drink.toJSON()
    assert result == {'drink_name': 'Coke', 'item_id': 1, 'number': 3}

def test_to_csv():
    drink = {"item_id": 1, "drink_name": "Coke", "number": 3}
    new_drink = Drink(drink)
    result = new_drink.toCSV()
    assert result == '1-Coke-3'
