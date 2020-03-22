from classes.Item import Item
class Pizza(Item):
    def __init__(this, pizza):
        this.size = pizza["size"]
        this.toppings = pizza["toppings"]
        this.number = pizza["number"]
        this.item_id = pizza["item_id"]
        Item.__init__(this, pizza["type"])

    def get_price(this, menu):
        price = 0
        size_ratio = menu.get_price_for_specific_item(this.size)
        #type_price = menu.get_price_for_specific_item(this.type)
        toppings_price = 0
        for topping in this.toppings:
            toppings_price += menu.get_price_for_specific_item(topping) * this.toppings[topping]
        
        return size_ratio * toppings_price * this.number
        
    def toJSON(this):
        result = {}
        result['size'] = this.size
        result['type'] = this.type
        result['toppings'] = {}
        for topping in this.toppings:
            result['toppings'][topping] = this.toppings[topping]
        result['number'] = this.number
        result['item_id'] = this.item_id
        return result


    def toCSV(this):
        result = ''
        result = result + str(this.item_id) + "-" + str(this.number) + "-" + this.size + "-" + this.type
        for topping in this.toppings:
            result = result + "-" + topping + "-" + str(this.toppings[topping])
        return result