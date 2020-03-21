from classes.FileDealer import FileDealer
file_dealer = FileDealer()

def test_filerdealer_load_menu():
    after = file_dealer.load_menu()
    expected = {
    "pizza": {
        "size": {
            "S": 0.8, 
            "M": 1.0, 
            "L": 1.5
            }, 
            "type": {
                "pepperoni": 8, "margherita": 6, "vegetarian": 14.5, "Neapolitan": 9
                }, 
                "topping": 
                {
                    "olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2, "beef": 4.5, "pepperoni": 2.5
                }
        }, "drink": 
        {
            "Coke": 2, 
            "Diet Coke": 3, 
            "Coke Zero": 4, 
            "Pepsi": 2, 
            "Diet Pepsi": 1, 
            "Dr. Pepper": 3, 
            "Water": 4, 
            "Juice": 2}
    }

    assert after == expected

def test_filerdealer_load_orders():
    after = file_dealer.load_orders()
    expected = [{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}, {"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}]
    assert after == expected


def test_filerdealer_load_uber_json():
    expected = {"Uber-1": {"order_details": {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}}}
    after = file_dealer.load_uber_json()
    assert after == expected

def test_filerdealer_load_foodora_csv():
    after = file_dealer.load_foodora_csv()
    expected = {
        'Foodora-1': {
            'order_details': {
               'pizzas': [
                    {
                        'item_id': 1, 
                        'toppings': {
                            'olives': 4, 
                            'tomatoes': 1,
                            'mushrooms': 1
                        }, 
                        'type': 'pepperoni', 
                        'number': 1, 
                        'size': 'L'
                    }
                ],  
                'drinks': [
                    {
                        'item_id': 1, 
                        'number': 2, 
                        'drink_name': 'Pepsi'
                    }
                    ],
                    'price': 26.5,
                    'address': '100 Street'
                }, 
                'order_number': 1
                }
    }
    assert after == expected

def test_filerdealer_load_types():
    expected = {"pepperoni": {"olives": 2, "mushrooms": 1}, "margherita": {"chicken": 3}, "vegetarian": {"jalapenos": 2, "pepperoni": 1}, "Neapolitan": {"beef": 2}, "New": {"beef": 10, "chicken": 1}}
    after = file_dealer.load_types()
    assert after == expected

