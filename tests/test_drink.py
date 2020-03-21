from classes.Item import Item
from classes.Drink import Drink

def test_new_drink():
    drink = {"item_id": 1, "drink_name": "Coke", "number": 3}
    new_drink = Drink(drink)
    assert new_drink.item_id == 1
    assert new_drink.type == "Coke"
    assert new_drink.number == 3