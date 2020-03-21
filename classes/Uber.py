from classes.Delivery import Delivery
class Uber(Delivery):
    def __init__(this, order):
        super().__init__(order)

    def toJSON(this):
        result = {}
        result['order_details'] = this.order_details.toJSON()
        return result