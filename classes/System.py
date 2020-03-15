from classes.Menu import Menu
from classes.Orders import Orders
class System:
    def __init__(this):
        this.menu = Menu()
        this.orders = Orders(this.menu)
