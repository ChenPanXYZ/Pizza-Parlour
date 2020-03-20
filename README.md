# a2-starter

Run the main Flask module by running `python3 PizzaParlour.py`

Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`

# We stored the information of all orders in orders.json. Although it is not required as per to the handout, we think it makes more sense to store this kind of data.


curl localhost:5000/make-new-order -d '{}'
curl localhost:5000/order-a-drink -d '{"order_number": 1, "drink": {"type": "Diet Coke", "number": 2}}' -H 'Content-Type: application/json'

curl localhost:5000/order-a-pizza -d '{"order_number": 1, "pizza": {"number": 2, "size": "L", "type": "pepperoni", "toppings": {"olives": 2, "tomatoes": 1}}}' -H 'Content-Type: application/json'


curl localhost:5000/change-an-order -d '{"order_number": 1, "drinks": [{"item_id": 1, "number": 3}]}' -H 'Content-Type: application/json'


curl localhost:5000/change-an-order -d '{"order_number": 1, "pizzas": [{"pizza_id": 1, "size": "M", "item_id": 1}]}' -H 'Content-Type: application/json'
