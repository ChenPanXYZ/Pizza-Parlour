from classes.FileDealer import FileDealer
from classes.Menu import Menu
from classes.Order import Order
class System:
    def __init__(this):
        this.file_dealer = FileDealer()
        this.menu = Menu(this.file_dealer.load_menu())
        this.orders = []
        this.load_orders()

    def load_orders(this):
        orders = this.file_dealer.load_orders()
        for order in orders:
            this.orders.append(Order(order, this.menu))

    def show_all_orders(this):
        return this.OrdersToJSON()


    def OrdersToJSON(this):
        result = []
        for order in this.orders:
            result.append(order.toJSON())
        return result