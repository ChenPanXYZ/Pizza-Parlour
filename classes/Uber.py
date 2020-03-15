from classes.Delivery import Delivery
class Uber(Delivery):
    def __init__(this, order):
        this.address = order.address
        this.order_details = order
        this.order_number = order.order_number

    def toJSON(this):
        result = {}
        result['address'] = this.address
        result['order_details'] = this.order_details.toJSON()
        result['order_number'] = this.order_number
        return result