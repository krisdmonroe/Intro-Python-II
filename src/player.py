# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, inventory = None):
        self.name = name
        self.currentRoom = currentRoom
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    # Allows player to get an item from a room
    def getItem(self, item):
        self.inventory.append(item)
    # Allows player to drop an item
    def dropItem(self, item):
        self.inventory.remove(item)
