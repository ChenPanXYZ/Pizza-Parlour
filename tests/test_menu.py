from classes.Menu import Menu

# Assume that FileDealer works as expected, and it is the mocked data which we will obtained from FileDealer in the functional test.
data = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}

menu = Menu(data)
def test_menu_get_price_for_specific_item():
    price = menu.get_price_for_specific_item("Coke")
    expected = 2
    assert price == expected

    price = menu.get_price_for_specific_item("tomatoes")
    expected = 1

def test_menu_get_full_content():
    content = menu.get_full_content()
    expected = {"pizza": {"size": {"S": 0.8, "M": 1.0, "L": 1.5}, "type": {"pepperoni": 2, "margherita": 3, "vegetarian": 4, "Neapolitan": 1, "Yuwan": 2, "NewType": 5}, "topping": {"olives": 3, "tomatoes": 1, "mushrooms": 2, "jalapenos": 6, "chicken": 2.0, "beef": 4.3, "pepperoni": 2.5}}, "drink": {"Coke": 2, "Diet Coke": 3, "Coke Zero": 4, "Pepsi": 2, "Diet Pepsi": 1, "Dr. Pepper": 3, "Water": 4, "Juice": 2}}
    assert content == expected
