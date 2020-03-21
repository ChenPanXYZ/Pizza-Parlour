import json
import csv

class FileDealer:
    def load_menu(this):
        with open('data/Menu.json', 'r') as f:
            return json.load(f)

    def load_orders(this):
        with open('data/Orders.json', 'r') as f:
            return json.load(f)

    def load_types(this):
        with open('data/Types.json', 'r') as f:
            return json.load(f)

    def load_uber_json(this):
        uber_deliveries = {}
        with open('data/Uber.json', 'r') as f:
            uber_deliveries = json.load(f)
        return uber_deliveries

    def load_foodora_csv(this):
        foodora_deliveries = {}
        with open('data/Foodora.csv', 'r') as f:
            rows = csv.reader(f)
            for row in rows:
                delivery_id_info = row[0]
                pizzas_info = row[1]
                drinks_info = row[2]
                order_address_info = row[3]
                order_price = row[4]
                order_number = row[5]
                pizzas_info = pizzas_info.split("|")
                pizzas = []
                if(pizzas_info != ['']):
                    for pizza_info in pizzas_info:
                        pizza_info = pizza_info.split("-")
                        pizza = {}
                        pizza['item_id'] = int(pizza_info[0])
                        pizza['number'] = int(pizza_info[1])
                        pizza['size'] = pizza_info[2]
                        pizza['type'] = pizza_info[3]
                        pizza['toppings'] = {}
                        i = 4
                        while i < len(pizza_info) - 1:
                            pizza['toppings'][pizza_info[i]] = int(pizza_info[i+1])
                            i = i + 2
                        pizzas.append(pizza)
                drinks = []
                drinks_info = drinks_info.split("|")
                if(drinks_info != ['']):
                    for drink_info in drinks_info:
                        drink_info = drink_info.split("-")
                        drink = {}
                        drink['item_id'] = int(drink_info[0])
                        drink['drink_name'] = drink_info[1]
                        drink['number'] = int(drink_info[2])
                        drinks.append(drink)
                
                foodora_deliveries[delivery_id_info] = {}
                foodora_deliveries[delivery_id_info]['order_details'] = {}
                foodora_deliveries[delivery_id_info]['order_details']['pizzas'] = pizzas
                foodora_deliveries[delivery_id_info]['order_details']['drinks'] = drinks
                foodora_deliveries[delivery_id_info]['order_details']['address'] = order_address_info
                foodora_deliveries[delivery_id_info]['order_details']['price'] = float(order_price)
                foodora_deliveries[delivery_id_info]['order_number'] = int(order_number)

        return foodora_deliveries


    def write_to_types(this, types):
        with open('data/Types.json', 'w') as f:
            json.dump(types, f)

    def write_to_orders(this, orders):
        with open('data/Orders.json', 'w') as f:
            json.dump(orders, f)

    def write_to_uber_json(this, uber_deliveries):
        with open('data/Uber.json', 'w') as f:
            json.dump(uber_deliveries, f)

    def write_to_foodora_csv(this, foodora_deliveries):
        with open('data/Foodora.csv', 'w') as f:
            write_rows = foodora_deliveries
            for row in write_rows:
                f.write(row)
                f.write('\n')

    def write_to_menu(this, menu):
        with open('data/Menu.json', 'w') as f:
            json.dump(menu, f)