from PizzaParlour import app
import json
def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

def test_new_order():
    data = {}
    response = app.test_client().post('/make-a-new-order', json = data)
    assert int(response.data) == 4

def test_check_order():
    data = {"order_number": 100}
    response = app.test_client().post('/check-order', json = data)
    #parsed_response = (json.loads(response.data))
    assert response.data == b'The Order Number doesn\'t exist.'
    data = {"order_number": 1}
    response = app.test_client().post('/check-order', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

def test_show_all_orders():
    response = app.test_client().get('/show-all-orders')
    parsed_response = (json.loads(response.data))
    print(parsed_response)
    assert parsed_response == [{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}, {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}, {"order_number": 4, "pizzas": [], "drinks": [], "address": "", "price": 0}]
    # Note that by previous test a new order is generated.


