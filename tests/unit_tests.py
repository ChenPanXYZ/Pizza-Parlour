#from PizzaParlour import app
import requests, unittest, json

#helper function
def get_json(address):
    with open(address, 'r') as f:
        json_got = json.load(f)
    return json_got

class TestPizzaParlour(unittest.TestCase):
    
    #def test_pizza(self):
    #    response = app.test_client().get('/pizza')
    #    self.assertEqual(response.status_code, 200)
    #    self.assertEqual(response.data, b'Welcome to Pizza Planet!')
  
    #def test_empty_json(self):
    #    empty_dic = {}
    #    with open('../orders.json', 'w') as f:
    #        json.dump(empty_dic, f)
    #    self.assertEqual(get_json('../orders.json'), empty_dic) 

    def test_make_new_order(self):
        before = get_json("../orders.json")
        expected = before
        if not expected:
            order_num = 1
        else:
            order_num = max(int(i) for i in before) + 1
        expected[str(order_num)] = {"pizzas": [], "drinks": {}, "address": "", "price": 0}
        data = '{}'
        response = requests.post('http://localhost:5000/make-new-order', data=data)
        after = get_json("../orders.json")
        self.assertEqual(expected, after)
    
    def test_order_a_drink(self):
        before = get_json("../orders.json")

        expected = before
        if "Diet Coke" in expected["2"]["drinks"]:
            expected["2"]["drinks"]["Diet Coke"] += 2
        else: 
            expected["2"]["drinks"]["Diet Coke"] = 2
            expected["2"]["drinks"]["item id"] = 1
        expected["2"]["price"] += 2 * 3 # Price of Diet Coke

        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 2, "drink": {"type": "Diet Coke", "number": 2}}'
        response = requests.post('http://localhost:5000/order-a-drink', headers=headers, data=data)
        
        after = get_json("../orders.json")
        self.assertEqual(expected, after)
    
    def test_order_a_pizza(self):
        before = get_json("../orders.json")

        expected = before
        expected["2"]["pizzas"].append({"number": 2, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}})
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 2, "pizza": {"number": 2, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}}'
        response = requests.post('http://localhost:5000/order-a-pizza', headers=headers, data=data) 
        after = get_json("../orders.json")
        self.assertCountEqual(expected, after) #Since order of items of a dictionary can be random, use assertCountEqual here
    
    def test_change_an_order_1(self):
        before = get_json("../orders.json")
        expected = before
        for item in expected["2"]["drinks"]:
            if item["item id"] == 2:
               item["number"] = 3
        
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 2, "drinks": [{"item_id": 2, "number": 3}]}'
        response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

        after = get_json("../orders.json")
        self.assertEqual(expected, after)

    def test_change_an_order_2(self):
        before = get_json("../orders.json")
        expected = before
        for item in expected["2"]["pizzas"]:
            if (item["item_id"] == 1) :
                item["size"] = "M"
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 2, "pizzas": [{"pizza_id": 1, "size": "M", "item_id": 1}]}'
        response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

        after = get_json("../orders.json")
        self.assertEqual(expected, after)  
     

#def test_pizza():
#    response = app.test_client().get('/pizza')

#    assert response.status_code == 200
#    assert response.data == b'Welcome to Pizza Planet!'

if __name__ == '__main__':
    unittest.main()
