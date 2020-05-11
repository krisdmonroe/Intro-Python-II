class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def onTake(self, item):
        print("You have picked up {self.item}")

    def onDrop(self, item):
        print("You have droped {self.item}")

    def __str__(self):
        return f"{self.name}, {self.description}"