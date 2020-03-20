import json
import csv

class FileDealer:
    def load_menu(this):
        with open('data/Menu.json', 'r') as f:
            return json.load(f)

    def load_orders(this):
        with open('data/Orders.json', 'r') as f:
            return json.load(f)