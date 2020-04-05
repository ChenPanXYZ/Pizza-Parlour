from classes.FileDealer import FileDealer
from classes.Menu import Menu
from classes.Order import Order
from classes.Uber import Uber
from classes.Foodora import Foodora
class System:
    def __init__(this):
        this.file_dealer = FileDealer()
        this.menu = Menu(this.file_dealer.load_menu())
        this.orders = []
        this.load_orders()
        this.types = this.file_dealer.load_types()
        this.deliveries = {}
        this.load_foodora()
        this.load_uber()

    def add_new_type(this, type):
        type_name = type["name"]
        type_method = type["method"]
        this.types[type_name] = type_method

        new_type_price = 0
        for topping in type_method:
            new_type_price += this.menu.get_price_for_specific_item(topping) * type_method[topping]

        this.menu.content['pizza']['type'][type_name] = new_type_price
        this.file_dealer.write_to_types(this.types)
        this.file_dealer.write_to_menu(this.menu.content)
        return this.menu.content


    def make_a_new_order(this):
        order_number = this.unique_key_maker(this.orders)
        order = {}
        order["order_number"] = order_number
        order["pizzas"] = []
        order["drinks"] = []
        order["address"] = ""
        order["price"] = ""
        this.orders.append(Order(order))
        return order_number

    def change_an_order(this, order_number, pizzas, drinks):
        order = this.find_order_by_order_number(order_number)
        if order is None:
            return order
        for pizza in pizzas:
            order.change_pizza(pizza, this.menu, this.types)
        for drink in drinks:
            order.change_drink(drink, this.menu, this.types)
        return order

    def cancel_order(this, order_number):
        order = this.find_order_by_order_number(order_number)
        if order is None:
            return 404
        this.orders.remove(order)
        for uber_id, uber in this.deliveries['uber'].items():
            if uber.order_details == order:
                del this.deliveries['uber'][uber_id]
                break
        for foodora_id, foodora in this.deliveries['foodora'].items():
            if foodora.order_details == order:
                del this.deliveries['foodora'][foodora_id]
                break

    def unique_key_maker(this, dict_list):
        # The list consists of dicts.
        if(not dict_list):
            return 1
        else:
            return max(dict_list, key=lambda item: item.order_number).order_number + 1

    def load_orders(this):
        orders = this.file_dealer.load_orders()
        for order in orders:
            this.orders.append(Order(order, this.menu))

    def load_uber(this):
        this.deliveries['uber'] = {}
        uber_deliveries = this.file_dealer.load_uber_json()
        for delivery_id in uber_deliveries:
            delivery = uber_deliveries[delivery_id]
            order_number = delivery['order_details']['order_number']
            order = this.find_order_by_order_number(order_number)

            this.deliveries['uber'][delivery_id] = Uber(order)



    def load_foodora(this):
        this.deliveries['foodora'] = {}
        foodora_deliveries = this.file_dealer.load_foodora_csv()
        for delivery_id in foodora_deliveries:
            delivery = foodora_deliveries[delivery_id]
            order_number = delivery['order_number']
            order = this.find_order_by_order_number(order_number)
            this.deliveries['foodora'][delivery_id] = Foodora(order)

    def show_all_orders(this):
        return this.OrdersToJSON()

    
    # Deliveries
    def add_uber(this, order):
        # Here, we assume that the deleivery-id for uber eats is Uber-ID, we assume that we have sent the order data to uber and gotten the Uber-ID back.
        if(not this.deliveries['uber']):
            # No Order in Orders.json
            new_delivery_id = "Uber-1"
        else:
            new_delivery_id = max(this.deliveries['uber'], key=str)
            new_delivery_id = new_delivery_id[0: 5] + str(int(new_delivery_id[5:]) + 1)
        this.deliveries['uber'][new_delivery_id] = Uber(order)
        return new_delivery_id

    def add_foodora(this, order):
        if(not this.deliveries['foodora']):
            new_delivery_id = "Foodora-1"
        else:
            new_delivery_id = max(this.deliveries['foodora'], key=str)

            new_delivery_id = new_delivery_id[0: 8] + str(int(new_delivery_id[8:]) + 1)
        this.deliveries['foodora'][new_delivery_id] = Foodora(order)
        return new_delivery_id


    # ToJSON helpers


    def OrdersToJSON(this):
        result = []
        for order in this.orders:
            result.append(order.toJSON())
        return result

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
        this.file_dealer.write_to_orders(this.OrdersToJSON())
        this.file_dealer.write_to_uber_json(this.uber_deliveries_toJSON())
        this.file_dealer.write_to_foodora_csv(this.foodora_deliveries_toCSV())


    def find_order_by_order_number(this, order_number):
        for order in this.orders:
            if order.order_number == order_number:
                return order
        return None