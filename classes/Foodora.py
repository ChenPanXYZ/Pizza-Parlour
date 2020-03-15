from classes.Delivery import Delivery
class Foodora(Delivery):
    def __init__(this, order):
        this.address = order.address
        this.order_details = order
        this.order_number = order.order_number

    def toCSV(this):
        result = this.address + ',' + this.order_details.toCSV()
        return result