class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self._items = []  # protected attribute

    def add_item(self, item):
        self._items.append(item)

# Your solution here

    def remove_item(self, item):
        self._items.remove(item)

    def get_items(self):
        print(self._items)
    

my_stuff = Inventory("Ing")
my_stuff.add_item("fish sauce")
my_stuff.add_item("rice")
my_stuff.add_item("iron wok")

my_stuff.get_items() #['fish sauce', 'rice', 'iron wok']

print(my_stuff._items) #['fish sauce', 'rice', 'iron wok'] because we execute in the same file

my_stuff.remove_item("fish sauce")

print(my_stuff._items)#['rice', 'iron wok']

class Preferences:
    def __init__(self, settings):
        self._settings = settings

# Your solution here