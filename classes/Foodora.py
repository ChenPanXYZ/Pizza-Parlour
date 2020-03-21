from classes.Delivery import Delivery
class Foodora(Delivery):
    def __init__(this, order):
        super().__init__(order)

    def toCSV(this):
        result = this.order_details.toCSV()
        return result