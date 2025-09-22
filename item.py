from random import *
Item_list = {"Sword": {"type": "equipment", "value": 2},
             "Samll Gold Pouch": {"type": "gold-item", "value": 50},
             "Leather Boots": {"type": "equipment", "value": 1}}
class Item():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def drop_gold(self):
        return randint(10, 100)

    def drop_item(self):
        item_name = choice(list(Item_list.keys()))
        item_data = Item_list[item_name]
        new_item = Item(item_name, item_data["type"], item_data["value"])
        return new_item
    
    def __str__(self):
        return f"{self.name} ({self.type}, {self.value})"

class Inventory():
    def __init__(self, items: list[Item]):
        self.items = items

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, name: str):
        if name in self.items:
            self.items.remove(name)
            print(f"{name} 아이템을 버렸습니다.")
            return True
        else:
            print(f"{name} 아이템을 찾지 못했습니다.")
            return False
        
    def show_inventory(self):
        for item in self.items:
            print(item)