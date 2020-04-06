
# Assignment 2: Pair Programming

## Table of Contents
1. [Instruction](#introductions)
2. [Demo Video](#demo)
2. [Data](#data)
3. [Program Design](#program-design)
4. [Functionality](#functionality)
5. [API Docs](#api-docs)
5. [Pair Programming](#pair-programming)
6. [Code Craftsmanship](#code-craftsmanship)
7. [Other Stories](#other-stories)

## Instructions<a name="introductions"></a>
### Running our program
```
$ git clone https://github.com/csc301-winter-2020/assignment-2-chenpan_gujingji.git
$ cd assignment-2-chenpan_gujingji
$ python3 PizzaParlour.py
```
### Running the tests
You can choose to type the command line to do the test mannually, but we wrote two shell scripts which will make it much easier for you to check the test results.
```
$ ./class_test.sh
$ ./route_test.sh
```
To manually input the test command:
```
$ cp sample-data/Menu.json sample-data/Orders.json sample-data/Types.json sample-data/Uber.json sample-data/Foodora.csv data
$ python3 -m pytest --cov-config=.coverageforclasstest --cov-report term --cov=. tests/class_tests
$cp sample-data/Menu.json sample-data/Orders.json sample-data/Types.json sample-data/Uber.json sample-data/Foodora.csv data
$python3 PizzaParlour.py
```
Open another bash shell:
```
$ python3 -m pytest --cov-config=.coveragerc --cov-report term --cov=. tests/test_routes.py
```
The test results should look like this:
#### Result For Class test
![enter image description here](https://blog.chenpan.xyz/wp-content/uploads/2020/04/class_test.png)
This doesn't cover 90% lines of the codes, but we will cover 90% lines of the codes with Route Test.
#### Result For Route test
![enter image description here](https://blog.chenpan.xyz/wp-content/uploads/2020/04/route_test.png)

## Data Video<a name="demo"></a>
[![IMAGE ALT TEXT](https://blog.chenpan.xyz/wp-content/uploads/2020/04/demo-video-screenshot.png)](https://www.youtube.com/watch?v=LMSJN-cWAc8&feature=youtu.be "Demo Video")
Click to see the demo video on Youtube.
## Data<a name="data"></a>
We use file-based database. We have five files that store the data. All the data files are in the **data** folder.

 - Orders.json: it stores all the orders' details.
 - Menu.json: it stores the information of the menu. For example, the price of Coke.
 - Types.json: it stores the names of pizzas' types and its corresponding method of preparation.
- Uber.json: it stores the information of Uber deliveries.
- Foodora.csv: it stores the information of Foodora deliveries.

For test purpose, we predefined sample data. The sample data is stored in the **sample-data** folder.

Sample data looks like:
### Orders.json
```
[
{"order_number": 1, "pizzas": [{"size": "L", "type": "pepperonis", "toppings": {"olives": 4, "tomatoes": 1, "mushrooms": 1}, "number": 1, "item_id": 1}], "drinks": [{"item_id": 1, "drink_name": "Pepsi", "number": 2}], "address": "100 Street", "price": 26.5}, 
{"order_number": 2, "pizzas": [], "drinks": [{"item_id": 1, "drink_name": "Diet Coke", "number": 5}], "address": "", "price": 15}, 
{"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}
]
```
### Menu.json
```
{

	"pizza": {

		"size": {

			"S": 0.8,

			"M": 1.0,

			"L": 1.5

		},

		"type": {

		"pepperonis": 8, 
		"margherita": 6, 
		"vegetarian": 14.5, 
		"Neapolitan": 9
		},

		"topping":

		{
			"olives": 3, 
			"tomatoes": 1, 
			"mushrooms": 2, 
			"jalapenos": 6, 
			"chicken": 2, 
			"beef": 4.5, 
			"pepperoni": 2.5
		}

	}, 
	"drink":
	{
		"Coke": 2,
		"Diet Coke": 3,
		"Coke Zero": 4,
		"Pepsi": 2,
		"Diet Pepsi": 1,
		"Dr. Pepper": 3,
		"Water": 4,
		"Juice": 2
	}
}
```
### Types.json
```
{
"pepperonis": {"olives": 2, "mushrooms": 1}, 
"margherita": {"chicken": 3}, 
"vegetarian": {"jalapenos": 2, "pepperoni": 1}, 
"Neapolitan": {"beef": 2}, 
"New": {"beef": 10, "chicken": 1}}
```
### Uber.json
```
{"Uber-1": {"order_details": {"order_number": 3, "pizzas": [{"size": "L", "type": "margherita", "toppings": {"beef": 2, "tomatoes": 1, "chicken": 3}, "number": 1, "item_id": 1}], "drinks": [], "address": "200 Street", "price": 24.0}}}
```
### Foodora.csv
```
Foodora-1,1-1-L-pepperonis-olives-4-tomatoes-1-mushrooms-1,1-Pepsi-2,100 Street,26.5,1
```
To help you understand how the information is  stored in Foodora.csv:

 - Each row stands for one Foodora Delivery.
 - The format is: FoodoraID, ItemID-Number-Size-Type-Topping1-Number-Topping2-Number-Topping3-Number, itemID-Drink1-Number, itemID-Drink2-Number, Price, Address, Price, OrderNumber

## Program design<a name="introductions"></a>
### Stucture of  our program
![enter image description here](https://www.chensnotes.com/wp-content/uploads/2020/03/structure.png)
### Relationships between objects
Our Draft for Design (UML graph)
![enter image description here](https://www.chensnotes.com/wp-content/uploads/2020/03/75B0B055-8329-48B8-8439-AF404653CFA5-scaled.jpeg)

### Function design
When dicussing about the function design, we turned to the real world. We believed each class in our program should "make sense" as a real world Object and do its job accordingly. 
We imagine the flask routes as the "conversasions" between the Customers and the Waiters. The System is like the Machine that the waiters operate with when he / she hears something from the customer, and the File Dealer is like pencil so that the waiter can write down details. And the Order is like the real order, having order_number (id), pizzas, drinks, address and price. And Pizza has size, type, and toppings, drink has its name, just like the real world.
So, for instance, here was how a function (add a pizza) was designed:
 - **We started image what is it like in the real world**
 - Customer: Hi (new conversation, Pizza Parlour is involved), **Waiter** (System is involved), I am ready (Make a new order).
 - Waiter: OK (write down the **order number**), what do you want?
 - Customer: I'd like one pizza (**Pizza** is involved), large size, vegetarian, with two extra tomatoes.
 - Waiter: writing down the details. (**File Dealer** is involved).
 - Customer: And I'd like to use Uber (**Uber** is involved), my address is ABC.
 - Waiter: writing down the details. (**File Dealer** is involved).
 - Waiter: Is that all for today?
 - Customer: Yes, that's all.
 - Waiter: OK, thank you! Your order is on the way. (System is involved, update the status.) 
That's basically how we design the functions, we connect our functions with the real world, find out which parts are involved, what kind of data is needed.

The details of each function is in the **Functionality**. And how they work with each other is in the UML graph.

### Design patterns
1. We applied the **Singleton** design pattern. System class has only one instance called system, and the reason why we want to use this design pattern is to restrict the access to the shared resource. That is, we only allow the system instance to have access to Uber.json, Foodora.csv, Orders.json, and Menu.json.
Also, the Singleton design pattern makes it possible that some objects can be accessed from anywhere in the program, for example, the menu instance can be accessed when calculating the total price for pizzas and drinks, but unlike using a global variable, it is much harder to overwrite it.
2. We also applied the **Adapter** design pattern. We have a JSONWriter and a CSVWriter class, but none of the data can be understood by these two writers. So, before send dating to these two writers, we adapt the Object to JSON or CSV format.
3. We also applied the **Observer** design pattern. That is, when a pizza or a drink or the address of an order is changed, the system will notify and update Uber and Foodora and update the data stored. Similarly, when adding a new type, the system will notify and update the menu and type.
4. We also applied the **Dependency Injection** design pattern. When a class has the instance of another class, we don't let the class to instantiate the instance. Instead, we have those objects initialized by other class and just pass it in. For instance, every Delievery has Order as this.order_details, instead of making Delievery to generate the instance, we let the system do the job and pass Order to Uber or Foodora.
5. we also used **Factory Design** Pattern. To describe the order clearly, we create a ‘Pizza’ class and a ‘Drink’ class. Since they share the same attribute ‘Type’, we identify them as sub classes of an ‘Item’ class. ‘Type’ is the mere attribute of ‘Item’ class and is initialized at the time constructor of ‘Item’ is created, where ‘Pizza’ and ‘Drink’ have some other unique attributes and methods. ‘Order’ class is the factory where ‘Pizza’ and ‘Drink’ instances are created. It decides when to create either of them based on the different prompts that the consumer delivers, such as “Change_pizza” or “Add_drink”.

## Functionality<a name="functionality"></a>
### Required and Extra features
#### Required features
##### Make a new order
We have an route that generates an empty order and stores in the json-based databse.
##### Order a pizza
By giving the order number and the pizza details, we have a route order-a-pizza that updates the order by adding the pizza.
Note that, since each pizza has a method of preparation, so we will make it in the following way:
 - The pizza details contains Size, Type, Extra Toppings. When adding a new pizza, we will first add the toppings that are required by Type and then add the Extra Toppings the user requires.
 - If we find that the Pizza has already existed in the order, we will simply increment the number of the Pizza recorded in the order. (Just like item number in the real receipt.)
##### Order a drink
By giving the order number and the drink details, we have a route order-a-drink that updates the order by adding the drink.
 - If we find that the Drink has already existed in the order, we will simply increment the number of the Drink recorded in the order. 
##### Update an existing order
By giving the order number and the details on how to change the order, the route change-an-order can update the order.
Please note that:
 - When the Type of a Pizza is changed, our system will make sure that the new Pizza has the required toppings for the new type.
 - If the number of a pizza and a drink becomes 0, we will remove it from the order.
 - If the order number doesn't exist, the route will give a response that tells the front-end.
##### Cancel order
By giving the order number, the route cancel-order can remove the order.
##### Ask for pickup or delivery
We have Uber.json and Foodora, with each containing the Delivery's order number, the adddress, and the order details. There is a function in System that loads the Uber and Foodora data into our program.
For inhouse delivery, we do not have a separate file to store. All inhouse delivery will be stored in Orders.json.
For pickup, it is the order without an address, it is also stored in Orders.json.
##### Ask for the menu
We have two routes. get-full-menu will simply return the full menu. get-price-for-specific-item will return the price by the item name.
##### Change the price for an item
With the item name and the new price, the Route change-price-for-item can handle the price changes. 
##### Add new type
By giving the new type and its method of preparation, Route add-new-type can add the new type into Type.json and change Menu.json as well.

#### Extra features
##### Send Requests to Uber and Foodora
We have route set-delivery. By giving the order number and the method of delivery (Uber or Foodora), we send a request to Uber and Foodora (For now, we just mock that we have such APIs), and then we get the delivery id back, and we store the information into Uber.json or Foodora.
##### The data never loses.
Although not required by the handout, we think it makes more sense to store the information of orders somewhere, not just Uber and Foodora. So, we managed to store the informations of all orders into Orders.json. Thanks to this, everytime when the system restarts, the data will still be there.

#### Future Features
##### Stauts for the order
Because we used Observer design pattern, now if we update an order or change the price of an item, it will notify Order, Uber, and Foodora to update their data as well. We want, in the future, we will added another attritute to each order, called "status". So, if the status of an order is "delivering" or "completed", we won't update their data.

#### cURL examples
##### Make a new order
```
$ curl --request POST localhost:5000/make-a-new-order -d '{}' -H 'Content-Type: application/json'
```
##### Check an order (by order number)
```
$ curl --request GET localhost:5000/check-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
```
##### Cancel an order (by order number)
```
$ curl --request DELETE localhost:5000/cancel-order -d '{"order_number": 1}' -H 'Content-Type: application/json'
```
##### Show all orders
```
$ curl --request GET localhost:5000/show-all-orders
```
##### Order a pizza
```
$ curl --request PATCH localhost:5000/order-a-pizza -d '{"order_number": 1, "pizza": {"number": 1, "size": "S", "type": "vegetarian", "toppings": {"beef": 2, "tomatoes": 1, "pepperoni": 1, "jalapenos": 2}}}' -H 'Content-Type: application/json'
```
##### Order a drink
```
$ curl --request PATCH localhost:5000/order-a-drink -d '{"order_number": 2, "drink": {"drink_name": "Diet Coke", "number": 5}}' -H 'Content-Type: application/json'
```
##### Change an order
```
$ curl --request PATCH localhost:5000/change-an-order -d '{"order_number": 4, "pizzas": [{"item_id": 1, "size": "S", "type": "vegetarian"}], "drinks": []}' -H 'Content-Type: application/json'
```
##### Set address
```
$ curl --request PATCH localhost:5000/set-address -d '{"order_number": 1, "address": "222 Street"}' -H 'Content-Type: application/json'
```
##### Set delivery
```
$ curl localhost:5000/set-delivery -d '{"order_number": 1, "delivery": "uber"}' -H 'Content-Type: application/json'
```
##### Get the full menu
```
$ curl localhost:5000/get-full-menu
```
##### Get price for specific item
```
$ curl --request GET localhost:5000/get-price-for-specific-item -d '{"item": "Coke"}' -H 'Content-Type: application/json'
```
##### Add new type
```
$ curl localhost:5000/add-new-type -d '{"name": "New", "method": {"beef": 10, "chicken": 1}}' -H 'Content-Type: application/json'
```
##### Change price for item
```
$ curl --request PATCH localhost:5000/change-price-for-item -d '{"item": "olives", "price": 5}' -H 'Content-Type: application/json'
```

## API Docs<a name="api-docs"></a>
### ```POST```: Route to add a new order.

**Route: /make-a-new-order

**Request:** does not have a body

**Response:**

```
New_Order_ID
```

### ```GET```: Route to check an existing order.

**Route: /check-order

**Request:** 

```json
{
	"order_number": INT
}
```

**Response:**

```json
{
	"order_number": ORDER_NUMBER,
	"pizzas": [
		{"item_id": ITEM_ID, "number": NUMBER, "size": SIZE, 
		 "type": TYPE, "toppings": [{TOPPING_NAME: NUMBER}, ...]
		}, ...
	],
	"drinks": [
		{"item_id": ITEM_ID, "number": NUMBER, "drink_name": DRINK_NAME,
		}, ...
	]
	"address": ADDRESS,
	"price": PRICE
}
```

### ```DELETE```:  Route to Cancel an order

**Route: /cancel-order

**Request:** 

```json
{
	"order_number": INT
}
```

**Response:**

```json
{
	"order_number": ORDER_NUMBER,
	"pizzas": [
		{"item_id": ITEM_ID, "number": NUMBER, "size": SIZE, 
		 "type": TYPE, "toppings": [{TOPPING_NAME: NUMBER}, ...]
		}, ...
	],
	"drinks": [
		{"item_id": ITEM_ID, "number": NUMBER, "drink_name": DRINK_NAME,
		}, ...
	]
	"address": ADDRESS,
	"price": PRICE
}
```

### ```GET```:  Route to Get All Orders

**Route: /show-all-orders

**Request:**  No Request Body Needed

**Response:**

```json
[
	{
		"order_number": ORDER_NUMBER,
		"pizzas": [
			{"item_id": ITEM_ID, "number": NUMBER, "size": SIZE, 
			 "type": TYPE, "toppings": [{TOPPING_NAME: NUMBER}, ...]
			}, ...
		],
		"drinks": [
			{"item_id": ITEM_ID, 
			"number": NUMBER, "drink_name": DRINK_NAME,
			}, ...
		]
		"address": ADDRESS,
		"price": PRICE
	}, ...
]
```

### ```PATCH```:  Route to Order a Pizza

**Route: /order-a-pizza

**Request:** 

```json
{
	"order_number": INT,  
	"pizza":{
		"number":INT,  
		"size": STR,  
		"type": STR,  
		"toppings":[{"EXTRA-TOPPING": NUMBER}, ...] 
	}
}
```

**Response:**

```json
{
	"item_id": ITEM_ID,
	"number": NUMBER,
	"size": SIZE,
	"toppings": {
	"TOPPING": NUMBER,
	...
	},
	"type": TYPE
}
```
### ```PATCH```:  Route to Order a drink

**Route: /order-a-drink

**Request:** 

```json
{
	"order_number": 2, 
	"drink": {
		"drink_name": STR, 
		"number": INT
	}
}
```

**Response:**

```json
{
	"item_id": ITEM_ID,
	"drink_name": DRINK_NAME,
	"number": NUMBER
}
```

### ```PATCH```:  Route to Change an Existing Order

**Route: /change-an-order

**Request:** 

```json
{
	"order_number": INT, 
	"pizzas": [
		{"item_id": INT, ("size": STR), ("type": STR), 
		("toppings": [{EXTRA-TOPPING_NAME: NUMBER}, ...])}
		,...
	],
	"drinks": [{DRINK_NAME: NUMBER}], ...}
```

**Response:**

```json
{
	"order_number": ORDER_NUMBER,
	"pizzas": [
		{"item_id": ITEM_ID, "number": NUMBER, "size": SIZE, 
		 "type": TYPE, "toppings": [{TOPPING_NAME: NUMBER}, ...]
		}, ...
	],
	"drinks": [
		{"item_id": ITEM_ID, "number": NUMBER, "drink_name": DRINK_NAME,
		}, ...
	]
	"address": ADDRESS,
	"price": PRICE
}
```

### ```PATCH```:  Route to Set up an Address for an existing order

**Route: /set-address

**Request:** 

```json
{
	"order_number": 1, 
	"address": "222 Street"
}
```

**Response:**

```json
{
	"order_number": ORDER_NUMBER,
	"pizzas": [
		{"item_id": ITEM_ID, "number": NUMBER, "size": SIZE, 
		 "type": TYPE, "toppings": [{TOPPING_NAME: NUMBER}, ...]
		}, ...
	],
	"drinks": [
		{"item_id": ITEM_ID, "number": NUMBER, "drink_name": DRINK_NAME,
		}, ...
	]
	"address": ADDRESS,
	"price": PRICE
}
```

### ```POST```:  Route to Set delivery For an existing order (Uber / Foodora)

**Route: /set-delivery

**Request:** 

```json
{
	"order_number": INT, 
	"delivery": "uber" / "foodora"
}
```

**Response:**

```
DELIVERY_ID
```

### ```GET```:  Route to Get Full Menu

**Route: /get-full-menu

**Request:**  No Request Body Needed

**Response:**

```json

{
	"pizza": {
		"size": {
			"S": 0.8,
			"M": 1.0,
			"L": 1.5
		},
	"type": {
		"pepperonis": 8,
		"margherita": 6,
		"vegetarian": 14.5,
		"Neapolitan": 9,
		...
	},
	"topping": {
		"olives": 3,
		"tomatoes": 1,
		"mushrooms": 2,
		"jalapenos": 6,
		"chicken": 2,
		"beef": 4.5,
		"pepperoni": 2.5
	}
}, 
"drink": {
	"Coke": 2,
	"Diet Coke": 3,
	"Coke Zero": 4,
	"Pepsi": 2,
	"Diet Pepsi": 1,
	"Dr. Pepper": 3,
	"Water": 4,
	"Juice": 2
	}
}
```

### ```GET```:  Route to Get price for specific item

**Route: /get-price-for-specific-item

**Request:**  
```json
{
	"ITEM": STR
}
```

**Response:**

```
ITEM_PRICE
```

### ```POST```:  Route to Add new type

**Route: /add-new-type

**Request:**  
```json
{
	"name": NAME, 
	"method": {TOPPING: NUMBER, ...}
}
```

**Response:**
```json
{
	"pizza": {
		"size": {
			"S": 0.8,
			"M": 1.0,
			"L": 1.5
		},
	"type": {
		"pepperonis": 8,
		"margherita": 6,
		"vegetarian": 14.5,
		"Neapolitan": 9,
		"NEW_TYPE": NEW_TYPE_PRICE
		...
	},
	"topping": {
		"olives": 3,
		"tomatoes": 1,
		"mushrooms": 2,
		"jalapenos": 6,
		"chicken": 2,
		"beef": 4.5,
		"pepperoni": 2.5
	}
}, 
"drink": {
	"Coke": 2,
	"Diet Coke": 3,
	"Coke Zero": 4,
	"Pepsi": 2,
	"Diet Pepsi": 1,
	"Dr. Pepper": 3,
	"Water": 4,
	"Juice": 2
	}
}
```


### ```PATCH```:  Route to Change price for item

**Route: /change-price-for-item

**Request:**  
```json
{
	"item": STR, 
	"price": INT
}
```

**Response:**
```json
{
	"pizza": {
		"size": {
			"S": 0.8,
			"M": 1.0,
			"L": 1.5
		},
	"type": {
		"pepperonis": 8,
		"margherita": 6,
		"vegetarian": 14.5,
		"Neapolitan": 9,
	...
	},
		"topping": {
		"olives": 3,
		"tomatoes": 1,
		"mushrooms": 2,
		"jalapenos": 6,
		"chicken": 2,
		"beef": 4.5,
		"pepperoni": 2.5
	}
}, 
"drink": {
	"Coke": 2,
	"Diet Coke": 3,
	"Coke Zero": 4,
	"Pepsi": 2,
	"Diet Pepsi": 1,
	"Dr. Pepper": 3,
	"Water": 4,
	"Juice": 2
	}
}
```

## Pair Programming<a name="pair-progarmming"></a>
### Pair-programmed features
We did pair programming for every part of the assignment, except the readme, test shell scripts.

### Driver and Navigator for the pair-programmed features
We applied pair programming on each module of the PizzaParlour application.
In general, **Pan Chen** managed to implement the controller classes of the applications, such as “System”, “Orders” and “Menu” class module, along with classes for three ways to send deliveries, which involves JSON and CSV input and output, i.e “Uber”,“Foodora” and “Delivery” classes. 
Meanwhile, **Jingjing Gu** is assigned to finish the fundamental, factual classes such as “Drink”,“Pizza” and “Item”. 
As for tests, they were done in two parts, tests for classes and tests for routes. Either of us created tests for the part he programs for. All the coding were done through pair programming.
Based on the jobs allocation mentioned before, the one who was programming is the driver, and the other is the navigator. We used screen share feature on Skype to make drivers’ programming process available to the navigator, and the navigator could comment by voice in real time and provided support by pointing out errors or offering suggestions.
### Reflections on Pair Programming
#### Positive Reflection:
 - Higher efficiency: pair programming might be not that helpful at the beginning since we were just writing some isolated parts, like Drink, Pizza. But it became very powerful, because by writing codes, as well as watching the other's writing codes, every one had a better understanding on the codes, so it became easier to write codes for the more complicated parts, like Order, System, and so on. And if the Driver got lost, the navigator could always give his hands.
 - Encouraging each other and not to be frustrated: we will feel very frustrated if we are writing code alone, it is even worse if we debug alone. But pair programming means that we always work with someone else. So, we can encourage each other when we face difficulties.
 - Learn from each other: we are both undergraduate students, we are not perfect for programming, so everyone has their own expertise. Through pair programming, we can more directly discover and learn the advantages of each other.
 - Supervise each other to improve efficiency: in pair programming, we are not fighting alone, but it also means that there is one more pair of eyes looking at us. We used Skype's "Share Screen" to realize Pair Programming among the coronavirus crisis, since the Navigator is looking at the Driver's computer screen, no one had ever watched Youtube while programming.
#### Nagative Reflection:
 - Low efficiency : As for the PizzaParlour web app we build, it is easy
   to divide the whole project into several small tasks. With jobs
   allocated clearly, we would have been able to code alone. However,
   since we need to swap between driver and navigator, only one person
   can code at a time. Pair programming slows down our progress on the
   project to some extent.
 - Stressful coding atmosphere: For a person who is used to code alone,
   coding as a driver is stressful, since in pair programming, there is
   always an audience, the navigator, watching you coding. Normally, one
   could debug a lot when coding alone, since he can be accustomed to
   the “trial and error” style of coding. However, with an audience
   aside, spending much time debugging is easy to be considered as
   inexperienced, and could waste other’s time indirectly.
 - Imbalanced workload: Though we are formed as a team, we can still
   have coding skill differences towards a specific language, and we may
   not code as fast as each other. However, generally, in pair
   programming, we intend to average out the total coding time among
   each other, to ensure that each of us acts as driver or navigator for
   a similar amount of time. Given that much time, one of us can finish
   more coding jobs than the other, which means that he is doing more
   jobs. The workload difference can be significant, depending on the
   skill gap between the pair.
## Code Craftsmanship<a name="code-craftsmanship"></a>
We used VS Code extension Code Spell Checker to check spelling errors, and Linters for code craftsmanship.

Also we deleted all the commentted codes. We were really suprised that the instructor said we shouldn't comment codes to make backup. But it is very useful as we got used to it.
## Other stories<a name="other-stories"></a>
 - When we did the route test, we found that if we changed the Pizza
   type to "vegetarian", the new price was different. We started to
   doubt that there was some issues regarding calculation. We spent like
   three hours, only to find out it was because there one Pizza type and
   one Pizza topping shared the same name: "pepperoni". So, "vegetarian"
   has "pepperoni", which should be $2.5, but since there was also a
   type "pepperoni", which was $8, everytime when calculating price for
   topping  "pepperoni", $8 was applied. So, we found a workaround that
   rename the type to "pepperoni**s**".
 - Unfortunately, both of the two members are using Windows 10. So,
   pytest didn't work as expected, there was always importerror. It
   seemed a PATH issue but we couldn't solve even spending hours on it.
   Later, we found that instead of using pytest directly, we use the
   following command:  
   ``` python3 -m pytest--cov-config=.coverageforclasstest --cov-report term --cov=. tests/class_tests ```
