from classes.Menu import Menu
from classes.Orders import Orders
class System:
    def __init__(this):
        this.menu = Menu()
        this.orders = Orders(this.menu)
        this.deliveries = {}

        uber_deliveries = {}
        with open('uber.json', 'r') as f:
            uber_deliveries = json.load(f)
        
        for delivery_id in uber_deliveries:
            delivery = uber_deliveries[delivery_id]
            this.deliveries['uber'][delivery_id] = Uber(delivery)

        