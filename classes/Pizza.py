from classes.Item import Item
class Pizza(Item):
    def __init__(this, pizza):
        this.size = pizza["size"]
        this.toppings = pizza["toppings"]
        this.number = pizza["number"]
        this.item_id = pizza["item_id"]
        super().__init__(pizza["type"])

    def get_price(this, menu):
        price = 0
        size_ratio = menu.get_price_for_specific_item(this.size)
        type_price = menu.get_price_for_specific_item(this.type)
        toppings_price = 0
        for topping in this.toppings:
            toppings_price += menu.get_price_for_specific_item(topping) * this.toppings[topping]
        
        return size_ratio * (type_price + toppings_price) * this.number
        
    def toJSON(this):
        result = {}
        result['item_id'] = this.item_id
        result['size'] = this.size
        result['type'] = this.type
        result['toppings'] = {}
        for topping in this.toppings:
            result['toppings'][topping] = this.toppings[topping]
        result['number'] = this.number
        return result