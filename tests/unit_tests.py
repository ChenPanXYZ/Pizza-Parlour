from PizzaParlour import app

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'


# #from PizzaParlour import app
# import requests, unittest, json
# from flask import Flask
# app = Flask("Assignment 2 Unit Test")


# #helper function
# def get_json(address):
#     with open(address, 'r') as f:
#         json_got = json.load(f)
#     return json_got

# def empty_data():
#     init_order = {}
#     init_uber = {}
#     init_menu = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}
#     init_foodora = ""
#     with open('../orders.json', 'w') as f:
#         json.dump(init_order, f)
#     with open('../uber.json', 'w') as f:
#         json.dump(init_uber, f)
#     with open('../menu.json', 'w') as f:
#         json.dump(init_menu, f)
#     with open('../foodora.csv', 'w') as f:
#         f.write(init_foodora)

# class TestPizzaParlour(unittest.TestCase):
    
#     # def test_pizza(self):
#     #     response = app.test_client().get('/pizza')
#     #     #self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(response.data, 'Welcome to Pizza Planet!')
  
#     # def test_empty_json(self):
#     #    empty_dic = {}
#     #    with open('../orders.json', 'w') as f:
#     #        json.dump(empty_dic, f)
#     #    self.assertEqual(get_json('../orders.json'), empty_dic)

#     def test_make_new_order(self):
#         expected = {"1": {"pizzas": [], "drinks": [], "address": "", "price": 0}}
#         data = '{}'
#         response = requests.post('http://localhost:5000/make-new-order', data=data)
#         after = get_json("../orders.json")
#         self.assertEqual(expected, after)

    
#     # def test_order_a_drink_case1(self):
#     #     # Test For Order a Drink feature, case 1: Diet Coke doesn't exist at first.
#     #     expected = {"1": {"pizzas": [], "drinks": [{"Diet Coke": 1, "item_id": 1}], "address": "", "price": 3}}

#     #     headers = {'Content-Type': 'application/json',}
#     #     data = '{"order_number": 1, "drink": {"type": "Diet Coke", "number": 1}}'
#     #     response = requests.post('http://localhost:5000/order-a-drink', headers=headers, data=data)
        
#     #     after = get_json("../orders.json")
#     #     self.assertEqual(expected, after)
    
#     # def test_order_a_drink_case2(self):
#     #     # Test For Order a Drink feature, case 2: Diet Coke already exists.

#     #     expected = {"1": {"pizzas": [], "drinks": [{"Diet Coke": 2, "item_id": 1}], "address": "", "price": 6}}

#     #     headers = {'Content-Type': 'application/json',}
#     #     data = '{"order_number": 1, "drink": {"type": "Diet Coke", "number": 1}}'
#     #     response = requests.post('http://localhost:5000/order-a-drink', headers=headers, data=data)
        
#     #     after = get_json("../orders.json")
#     #     self.assertEqual(expected, after)
    
#     # def test_order_a_piazza(self):
#     #     expected = {"1": {"pizzas": [{"size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}, "number": 2, "item_id": 1}], "drinks": [{"Diet Coke": 2, "item_id": 1}], "address": "", "price": 24.0}}
        
#     #     headers = {'Content-Type': 'application/json',}
#     #     data = '{"order_number": 1, "pizza": {"number": 2, "size": "M", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}}'
#     #     response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

#     #     after = get_json("../orders.json")
#     #     self.assertEqual(expected, after)

#     # def test_change_an_order(self):
#     #     # Test For Change an Order, a topping should be removed because the number is decreased to 0.
#     #     expected = {"1": {"pizzas": [{"size": "L", "type": "pepperoni", "toppings": {"tomatoes": 1}, "number": 2, "item_id": 1}], "drinks": [{"Diet Coke": 2, "item_id": 1}], "address": "", "price": 15.0}}
#     #     headers = {'Content-Type': 'application/json',}
#     #     data = '{"order_number": 1, "pizzas": [{"item_id": 1, "size": "L", "toppings": {"olives" : 0}}]}'
#     #     response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

#     #     after = get_json("../orders.json")
#     #     self.assertEqual(expected, after)

#     def test_get_full_menu(self):

#         response = requests.get('http://localhost:5000/get-full-menu')
#         dic_text = ""
#         #Remove "\n"
#         for s in response.text:
#             if s != "\n":
#                 dic_text = dic_text + s
#         dict_got = json.loads(dic_text)
#         return dict_got
#         self.assertEqual(dict_got,get_json("../menu.json"))
# #def test_pizza():
# #    response = app.test_client().get('/pizza')

# #    assert response.status_code == 200
# #    assert response.data == b'Welcome to Pizza Planet!'

# if __name__ == '__main__':
#     #empty_data()
#     unittest.main()
#     #empty_data()
