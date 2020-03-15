from classes.Item import Item
class Drink(Item):
   def __init__(this,type, number, new_item_id):
      this.number = number
      this.item_id = new_item_id
      super().__init__(type)

   def get_price(this, menu):
      return menu.get_price_for_specific_item(this.type) * this.number