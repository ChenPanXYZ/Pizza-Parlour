#from PizzaParlour import app
import requests, unittest, json


#helper function
def get_json(address):
    with open(address, 'r') as f:
        json_got = json.load(f)
    return json_got

class TestPizzaParlour(unittest.TestCase):
    
    def test_pizza(self):
        response = app.test_client().get('/pizza')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome to Pizza Planet!')
  
    def test_empty_json(self):
       empty_dic = {}
       with open('../orders.json', 'w') as f:
           json.dump(empty_dic, f)
       self.assertEqual(get_json('../orders.json'), empty_dic)

    def test_make_new_order(self):

        before = get_json("../orders.json")
        expected = before
        if not expected:
            order_num = 1
        else:
            order_num = max(int(i) for i in before) + 1
        expected[str(order_num)] = {"pizzas": [], "drinks": [], "address": "", "price": 0}
        data = '{}'
        response = requests.post('http://localhost:5000/make-new-order', data=data)
        after = get_json("../orders.json")
        self.assertEqual(expected, after)
    
    def test_order_a_drink(self):

        before = get_json("../orders.json")
        expected = before
        in_item = False
        max_item_id = 0
        drinks = expected["1"]["drinks"]
        for item in drinks:
            if "item_id" in item:
                if item["item_id"] > max_item_id:
                    max_item_id = item["item_id"] 
            if "Diet Coke" in item:
                item["Diet Coke"] += 2
                in_item = True
                break
          
        if not in_item:
            drinks.append({"Diet Coke" : 2, "item_id": max_item_id + 1})

        expected["1"]["price"] += 2 * 3 # Price of Diet Coke

        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 1, "drink": {"type": "Diet Coke", "number": 2}}'
        response = requests.post('http://localhost:5000/order-a-drink', headers=headers, data=data)
        
        after = get_json("../orders.json")
        self.assertEqual(expected, after)
    
    def test_order_a_pizza(self):
        before = get_json("../orders.json")

        expected = before
        expected["1"]["pizzas"].append({"number": 2, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}})
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 1, "pizza": {"number": 2, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}}'
        response = requests.post('http://localhost:5000/order-a-pizza', headers=headers, data=data) 
        after = get_json("../orders.json")
        self.assertCountEqual(expected, after) #Since order of items of a dictionary can be random, use assertCountEqual here
    
    def test_change_an_order_1(self):
        before = get_json("../orders.json")
        expected = before
        for item in expected["1"]["drinks"]:
            if item["item_id"] == 2:

                for key in item:
                    if key != "item_id":
                        item_ordered = key
                        number_before = item[key]
                        item[key] = 3

        if 3 > number_before:
            expected["1"]["price"] += 2 * (3-number_before)
        else:
            expected["1"]["price"] -= 2 * (number_before-3)
        
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 1, "drinks": [{"item_id": 2, "number": 3}]}'
        response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

        after = get_json("../orders.json")
        self.assertEqual(expected, after)

    def test_change_an_order_2(self):
        before = get_json("../orders.json")
        expected = before
        for item in expected["1"]["pizzas"]:
            if (item["item_id"] == 1) :
                item["size"] = "M"
        headers = {'Content-Type': 'application/json',}
        data = '{"order_number": 1, "pizzas": [{"pizza_id": 1, "size": "M", "item_id": 1}]}'
        response = requests.post('http://localhost:5000/change-an-order', headers=headers, data=data)

        after = get_json("../orders.json")
        self.assertEqual(expected, after)  

    def test_get_full_menu(self):

        response = requests.get('http://localhost:5000/get-full-menu')
        dic_text = ""
        #Remove "\n"
        for s in response.text:
            if s != "\n":
                dic_text = dic_text + s
        dict_got = json.loads(dic_text)
        return dict_got
        self.assertEqual(dict_got,get_json("../menu.json"))
#def test_pizza():
#    response = app.test_client().get('/pizza')

#    assert response.status_code == 200
#    assert response.data == b'Welcome to Pizza Planet!'

if __name__ == '__main__':
    unittest.main()
