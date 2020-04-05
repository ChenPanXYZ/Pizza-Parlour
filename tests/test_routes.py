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
    response = app.test_client().get('/check-order', json = data)
    #parsed_response = (json.loads(response.data))
    assert response.data == b'The Order Number doesn\'t exist.'
    data = {"order_number": 1}
    response = app.test_client().get('/check-order', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}

def test_show_all_orders():
    response = app.test_client().get('/show-all-orders')
    parsed_response = (json.loads(response.data))
    assert parsed_response == [{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}, {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}, {"order_number": 4, "pizzas": [], "drinks": [], "address": "", "price": 0}]
    # Note that by previous test a new order is generated.

def test_order_a_pizza():
    data = {"order_number": 2, "pizza": {"number": 1, "size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1}}}
    response = app.test_client().patch('/order-a-pizza', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {"item_id": 1, "number": 1, "size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}}

    data = {"order_number": 200, "pizza": {"number": 1, "size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1}}}
    response = app.test_client().patch('/order-a-pizza', json = data)
    assert response.data == b"The Order Number doesn't exist."

def test_order_a_drink():
    data = {"order_number": 3, "drink": {"drink_name": "Juice", "number": 2}}
    response = app.test_client().patch('/order-a-drink', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {"item_id": 1, "number": 2, "drink_name": "Juice"}

    data = {"order_number": 300, "drink": {"drink_name": "Juice", "number": 2}}
    response = app.test_client().patch('/order-a-drink', json = data)
    assert response.data == b"The Order Number doesn't exist."

def test_change_an_order():
    data = {"order_number": 1, "pizzas": [{"item_id": 1, "size": "L", "toppings": {"olives": 0}}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 10}]}
    response = app.test_client().patch('/change-an-order', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'address': '100 Street', 'drinks': [{'drink_name': 'Pepsi', 'item_id': 1, 'number': 10}], 'order_number': 1, 'pizzas': [{'item_id': 1, 'number': 
1, 'size': 'L', 'toppings': {'mushrooms': 1, 'olives': 2, 'tomatoes': 1}, 'type': 'pepperonis'}], 'price': 33.5}

    data = {"order_number": 4, "pizza": {"number": 1, "size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1}}}
    app.test_client().patch('/order-a-pizza', json = data)

    data = {"order_number": 4, "pizzas": [{"item_id": 1, "size": "S", "type": "vegetarian"}], "drinks": []}
    response = app.test_client().patch('/change-an-order', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'address': '', 'drinks': [], 'order_number': 4, 'pizzas': [{'item_id': 1, 'number': 1, 'size': 'S', 'toppings': {'beef': 2, 'jalapenos': 2, 'pepperoni': 1, 'tomatoes': 1}, 'type': 'vegetarian'}], 'price': 19.6}

    data = {"order_number": 404, "pizzas": [{"item_id": 1, "size": "S", "type": "vegetarian"}], "drinks": []}
    response = app.test_client().patch('/change-an-order', json = data)
    parsed_response = response.data
    assert parsed_response == b"The Order Number doesn't exist."



def test_get_full_menu():
    response = app.test_client().get('/get-full-menu')
    parsed_response = (json.loads(response.data))
    assert parsed_response == {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperonis": 8, "margherita": 6, "vegetarian": 14.5, "Neapolitan": 9}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2, "beef": 4.5, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

def test_get_price_for_specific_item():
    data = {"item": "Coke"}
    response = app.test_client().get('/get-price-for-specific-item', json = data)
    assert float(response.data) == 2
    data = {"item": "margherita"}
    response = app.test_client().get('/get-price-for-specific-item', json = data)
    assert float(response.data) == 6
    data = {"item": "tomatoes"}
    response = app.test_client().get('/get-price-for-specific-item', json = data)
    assert float(response.data) == 1
    data = {"item": "L"}
    response = app.test_client().get('/get-price-for-specific-item', json = data)
    assert float(response.data) == 1.5
    data = {"item": "safasfasfasf"}
    response = app.test_client().get('/get-price-for-specific-item', json = data)
    assert response.data == b"The Item doesn't exist."

def test_add_new_type():
    data = {"name": "New", "method": {"beef": 10, "chicken": 1}}
    response = app.test_client().post('/add-new-type', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'drink': {'Coke': 2, 'Coke Zero': 4, 'Diet Coke': 3, 'Diet Pepsi': 1, 'Dr. Pepper': 3, 'Juice': 2, 'Pepsi': 2, 'Water': 4}, 'pizza': {'size': {'L': 1.5, 'M': 1.0, 'S': 0.8}, 'topping': {'beef': 4.5, 'chicken': 2, 'jalapenos': 6, 'mushrooms': 2, 'olives': 3, 'pepperoni': 2.5, 'tomatoes': 1}, 'type': {'Neapolitan': 9, 'New': 47.0, 'margherita': 6, 'pepperonis': 8, 'vegetarian': 14.5}}}

def test_set_address():
    data = {"order_number": 4, "address": "333 Street"}
    response = app.test_client().patch('/set-address', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'address': '333 Street', 'drinks': [], 'order_number': 4, 'pizzas': [{'item_id': 1, 'number': 1, 'size': 'S', 'toppings': {'beef': 2, 'jalapenos': 2, 'pepperoni': 1, 'tomatoes': 1}, 'type': 'vegetarian'}], 'price': 19.6}

def test_set_delivery():
    data = {"order_number": 4, "delivery": "uber"}
    response = app.test_client().post('/set-delivery', json = data)
    assert response.data == b"Uber-2"
    data = {"order_number": 400, "delivery": "foodora"}
    response = app.test_client().post('/set-delivery', json = data)
    assert response.data == b"The Order Number doesn't exist."

def test_cancel_order():
    data = {"order_number": 4}
    response = app.test_client().delete('/cancel-order', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == [{'order_number': 1, 'address': '100 Street', 'drinks': [{'drink_name': 'Pepsi', 'item_id': 1, 'number': 10}], 'pizzas': [{'item_id': 1, 'number': 1, 'size': 'L', 'toppings': {'mushrooms': 1, 'olives': 2, 'tomatoes': 1}, 'type': 'pepperonis'}], 'price': 33.5}, {'order_number': 2, 'address': '', 'drinks': [{'drink_name': 'Diet Coke', 'item_id': 1, 'number': 5}], 'pizzas': [{'item_id': 1, 'number': 1, 'size': 'L', 'toppings': {'beef': 2, 'chicken': 3, 'tomatoes': 1}, 'type': 'margherita'}], 'price': 39.0}, {'order_number': 3, 'address': '200 Street', 'drinks': [{'drink_name': 'Juice', 'item_id': 1, 'number': 2}], 'pizzas': [{'item_id': 1, 'number': 1, 'size': 'L', 'toppings': {'beef': 2, 'chicken': 3, 'tomatoes': 1}, 'type': 'margherita'}], 'price': 28.0}]

def test_change_price_for_item():
    data = {"item": "olives", "price": 5}
    response = app.test_client().patch('/change-price-for-item', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'drink': {'Coke': 2, 'Coke Zero': 4, 'Diet Coke': 3, 'Diet Pepsi': 1, 'Dr. Pepper': 3, 'Juice': 2, 'Pepsi': 2, 'Water': 4}, 'pizza': {'size': {'L': 1.5, 'M': 1.0, 'S': 0.8}, 'topping': {'beef': 4.5, 'chicken': 2, 'jalapenos': 6, 'mushrooms': 2, 'olives': 5, 'pepperoni': 2.5, 'tomatoes': 1}, 'type': {'Neapolitan': 9, 'New': 47.0, 'margherita': 6, 'pepperonis': 12, 'vegetarian': 14.5}}}

    data = {"item": "Coke", "price": 50}
    response = app.test_client().patch('/change-price-for-item', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'drink': {'Coke': 50, 'Coke Zero': 4, 'Diet Coke': 3, 'Diet Pepsi': 1, 'Dr. Pepper': 3, 'Juice': 2, 'Pepsi': 2, 'Water': 4}, 'pizza': {'size': {'L': 1.5, 'M': 1.0, 'S': 0.8}, 'topping': {'beef': 4.5, 'chicken': 2, 'jalapenos': 6, 'mushrooms': 2, 'olives': 5, 'pepperoni': 2.5, 'tomatoes': 1}, 'type': {'Neapolitan': 9, 'New': 47.0, 'margherita': 6, 'pepperonis': 12, 'vegetarian': 14.5}}}

    data = {"item": "L", "price": 2.0}
    response = app.test_client().patch('/change-price-for-item', json = data)
    parsed_response = (json.loads(response.data))
    assert parsed_response == {'drink': {'Coke': 50, 'Coke Zero': 4, 'Diet Coke': 3, 'Diet Pepsi': 1, 'Dr. Pepper': 3, 'Juice': 2, 'Pepsi': 2, 'Water': 4}, 'pizza': {'size': {'L': 2.0, 'M': 1.0, 'S': 0.8}, 'topping': {'beef': 4.5, 'chicken': 2, 'jalapenos': 6, 'mushrooms': 2, 'olives': 5, 'pepperoni': 2.5, 'tomatoes': 1}, 'type': {'Neapolitan': 9, 'New': 47.0, 'margherita': 6, 'pepperonis': 12, 'vegetarian': 14.5}}}


    data = {"item": "something doesn't exist", "price": 5}
    response = app.test_client().patch('/change-price-for-item', json = data)
    assert response.data == b"The Item doesn't exist."