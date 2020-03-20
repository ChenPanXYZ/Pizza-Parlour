class Menu:
    def __init__(this, data):
        this.content = data
    

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