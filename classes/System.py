from classes.Menu import Menu
from classes.Orders import Orders
from classes.Uber import Uber
import json
import csv
class System:
    def __init__(this):
        this.menu = Menu()
        this.orders = Orders(this.menu)
        this.deliveries = {}

        this.deliveries['uber'] = {}

        uber_deliveries = {}
        with open('uber.json', 'r') as f:
            uber_deliveries = json.load(f)
        
        for delivery_id in uber_deliveries:
            delivery = uber_deliveries[delivery_id]
            delivery_order_number = delivery['order_number']
            order = this.orders.details[delivery_order_number]
            this.deliveries['uber'][int(delivery_id)] = Uber(order)

        foodora_deliveries = []
        with open('foodora.csv', 'r') as f:
            foodora_deliveries = csv.reader(f)

    def add_uber(this, order):
        if(not this.deliveries['uber']):
            # No Order in Orders.json
            new_delivery_id = 1
        else:
            new_delivery_id = max(this.deliveries['uber'], key=int) + 1
        this.deliveries['uber'][new_delivery_id] = Uber(order)

    def uber_deliveries_toJSON(this):
        result = {}
        for every_uber_delivery_id in this.deliveries['uber']:
            result[every_uber_delivery_id] = this.deliveries['uber'][every_uber_delivery_id].toJSON()
        return result

    def foodora_deliveries_toCSV(this):
        result = {}
        for every_uber_delivery_id in this.deliveries['uber']:
            result[every_uber_delivery_id] = this.deliveries['uber'][every_uber_delivery_id].toJSON()
        return result

    def update_data(this):
        with open('orders.json', 'w') as f:
            json.dump(this.orders.toJSON(), f)
        with open('uber.json', 'w') as f:
            json.dump(this.uber_deliveries_toJSON(), f)
        with open('foodora.csv', 'w') as f:
            json.dump(this.foodora_deliveries_toCSV(), f)

        