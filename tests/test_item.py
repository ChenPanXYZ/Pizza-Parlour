from classes.Item import Item

def test_new_item():
    item = Item("Coke")
    assert item.type == "Coke"