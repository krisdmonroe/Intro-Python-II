# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    def insertItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.name}, {self.description}"

