from classes.Menu import Menu
from classes.Orders import Orders
from classes.Uber import Uber
from classes.Foodora import Foodora
import json
import csv
class System:
    def __init__(this):
        this.menu = Menu()
        this.orders = Orders(this.menu)
        this.deliveries = {}

        this.deliveries['uber'] = {}
        this.deliveries['foodora'] = {}

        uber_deliveries = {}
        with open('uber.json', 'r') as f:
            uber_deliveries = json.load(f)
        
        for delivery_id in uber_deliveries:
            delivery = uber_deliveries[delivery_id]
            delivery_order_number = delivery['order_number']
            order = this.orders.details[delivery_order_number]
            this.deliveries['uber'][int(delivery_id)] = Uber(order)



        foodora_deliveries = {}
        with open('foodora.csv', 'r') as f:
            rows = csv.reader(f)
            for row in rows:
                delivery_id_info = row[0]
                address_info = row[1]
                pizzas_info = row[2]
                drinks_info = row[3]
                order_address_info = row[4]
                order_price = row[5]
                order_number = row[6]

                pizzas_info = pizzas_info.split("|")

                pizzas = []
                for pizza_info in pizzas_info:
                    pizza_info = pizza_info.split("-")
                    pizza = {}
                    pizza['item_id'] = pizza_info[0]
                    pizza['number'] = pizza_info[1]
                    pizza['size'] = pizza_info[2]
                    pizza['type'] = pizza_info[3]
                    pizza['toppings'] = {}
                    i = 4 
                    while i < len(pizza_info) - 1:
                        pizza['toppings'][pizza_info[i]] = pizza_info[i+1]
                        i = i + 2

                    pizzas.append(pizza)
                drinks = []
                drinks_info = drinks_info.split("|")
                for drink_info in drinks_info:
                    drink_info = drink_info.split("-")
                    drink = {}
                    drink['item_id'] = drink_info[0]
                    drink[drink_info[1]] = drink_info[2]
                    drinks.append(drink)

                foodora_deliveries[delivery_id_info] = {}
                foodora_deliveries[delivery_id_info]['address'] = address_info
                foodora_deliveries[delivery_id_info]['order_details'] = {}
                foodora_deliveries[delivery_id_info]['order_details']['pizzas'] = pizzas
                foodora_deliveries[delivery_id_info]['order_details']['drinks'] = drinks
                foodora_deliveries[delivery_id_info]['order_details']['drinks'] = drinks
                foodora_deliveries[delivery_id_info]['order_details']['address'] = order_address_info
                foodora_deliveries[delivery_id_info]['order_details']['price'] = order_price
                foodora_deliveries[delivery_id_info]['order_details']['price'] = delivery_id_info
                foodora_deliveries[delivery_id_info]['order_number'] = order_number

        for delivery_id in foodora_deliveries:
            delivery = foodora_deliveries[delivery_id]
            delivery_order_number = delivery['order_number']
            order = this.orders.details[int(delivery_order_number)]
            this.deliveries['foodora'][int(delivery_id)] = Foodora(order)

    def add_uber(this, order):
        if(not this.deliveries['uber']):
            # No Order in Orders.json
            new_delivery_id = 1
        else:
            new_delivery_id = max(this.deliveries['uber'], key=int) + 1
        this.deliveries['uber'][new_delivery_id] = Uber(order)

    def add_foodora(this, order):
        if(not this.deliveries['foodora']):
            new_delivery_id = 1
        else:
            new_delivery_id = max(this.deliveries['foodora'], key=int) + 1
        this.deliveries['foodora'][new_delivery_id] = Foodora(order)

    def uber_deliveries_toJSON(this):
        result = {}
        for every_uber_delivery_id in this.deliveries['uber']:
            result[every_uber_delivery_id] = this.deliveries['uber'][every_uber_delivery_id].toJSON()
        return result

    def foodora_deliveries_toCSV(this):
        result_rows = []
        for every_foodora_delivery_id in this.deliveries['foodora']:
            result = ''
            result += str(every_foodora_delivery_id) + ',' + this.deliveries['foodora'][every_foodora_delivery_id].toCSV()
            result_rows.append(result)
        return result_rows

    def update_data(this):
        with open('orders.json', 'w') as f:
            json.dump(this.orders.toJSON(), f)
        with open('uber.json', 'w') as f:
            json.dump(this.uber_deliveries_toJSON(), f)
        with open('foodora.csv', 'w') as f:
            write_rows = this.foodora_deliveries_toCSV()
            print(write_rows)
            for row in write_rows:
                f.write(row)
                f.write('\n')

        