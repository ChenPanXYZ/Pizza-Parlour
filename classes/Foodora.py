from classes.Delivery import Delivery
class Foodora(Delivery):
    def __init__(this, order):
        Delivery.__init__(this, order)

    def toCSV(this):
        result = this.order_details.toCSV()
        return result