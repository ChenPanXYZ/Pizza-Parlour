from classes.Item import Item
class Pizza(Item):
    def __init__(this,pizza):
        this.size = pizza["size"]
        this.toppings = pizza["toppings"]
        super().__init__(pizza["type"])
    