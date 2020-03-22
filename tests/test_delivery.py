from classes.Delivery import Delivery
from classes.Order import Order

sample_order = {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

def test_new_delivery():
    new_order = Order(sample_order)
    delivery = Delivery(new_order)
    assert delivery.order_details == new_order
    assert delivery.order_number == 1
