from classes.Delivery import Delivery
class Uber(Delivery):
    def __init__(this, delivery):
        this.address = delivery['address']
        this.order_details = delivery['order_details']
        this.order_number = delivery['order_number']

    def toJSON(this):
        result = {}
        result['address'] = this.address
        result['order_details'] = this.address
        result['order_number'] = this.address
        return result