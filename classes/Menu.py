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





    def get_full_content(this):
        return this.content