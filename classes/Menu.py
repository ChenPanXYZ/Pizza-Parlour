class Menu:
    def __init__(this, data):
        this.content = data
    

    def change_price_for_item(this, item, price, method):
        if item in this.content['pizza']['size']:
            this.content['pizza']['size'][item] = price
        elif item in this.content['pizza']['topping']:
            old_price = this.content['pizza']['topping'][item]
            this.content['pizza']['topping'][item] = price
            for type in this.content['pizza']['type']:
                if item in method[type]:
                    this.content['pizza']['type'][type] -= old_price * method[type][item]
                    this.content['pizza']['type'][type] += price * method[type][item]
        elif item in this.content['drink']:
            this.content['drink'][item] = price

    def get_price_for_specific_item(this, item):
        if item in this.content['pizza']['size']:
            return this.content['pizza']['size'][item]
        elif item in this.content['pizza']['type']:
            return this.content['pizza']['type'][item]
        elif item in this.content['pizza']['topping']:
            return this.content['pizza']['topping'][item]
        elif item in this.content['drink']:
            return this.content['drink'][item]
        else:
            return -1

    def get_full_content(this):
        return this.content

    def toJSON(this):
        result = {}
        result['pizza'] = {}
        result['pizza']['size'] = {}
        result['pizza']['type'] = {}
        result['pizza']['topping'] = {}
        for size in this.content['pizza']['size']:
            result['pizza']['size'][size] = this.content['pizza']['size'][size]
        for type in this.content['pizza']['type']:
            result['pizza']['type'][type] = this.content['pizza']['type'][type]
        for topping in this.content['pizza']['topping']:
            result['pizza']['topping'][topping] = this.content['pizza']['topping'][topping]


        result['drink'] = {}

        for drink in this.content['drink']:
            result['drink'][drink] = this.content['drink'][drink]
        
        return result