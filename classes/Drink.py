from classes.Item import Item
class Drink(Item):
   def __init__(this, drink):
      this.number = drink["number"]
      this.item_id = drink["item_id"]
      Item.__init__(this, drink["drink_name"])

   def get_price(this, menu):
      return menu.get_price_for_specific_item(this.type) * this.number

   def toJSON(this):
      result = {}
      result['item_id'] = this.item_id
      result['drink_name'] = this.type
      result['number'] = this.number
      return result

   def toCSV(this):
      result = ''
      result = str(this.item_id) + "-" + this.type + "-" + str(this.number)
      return result