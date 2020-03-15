import json
class Menu:
    def __init__(this):
        with open('menu.json', 'r') as f:
            this.content = json.load(f)


            #  开始创建this.items。这是为了日后方便获取item价钱而为之。

            # drinks = this.content['drink]
            # 遍历所有drinks，每一个for loop中，都让this.items[drinks.key: Drink[drinks.key, drinks.key.value]]

            # pizza_type = this.content["pizza"]['type']
            # for loop 

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
            return -1 # tell the fron-end that this item doesn't exist

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