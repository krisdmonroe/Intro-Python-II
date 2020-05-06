from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player("Kris", room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
class UserInterface:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    def __str__(self):
        return f"{self.currentRoom.name}, {self.currentRoom.description}"

user = input("[n] North, [e] East, [s] South [w] West")

if user == "n" and room['outside']:
    print(UserInterface(room['foyer']))
else:
    print("Error User Not allowed to move there")
    print(UserInterface(room['outside']))

if user == "s" and room['foyer']:
    print(UserInterface(room['outside']))
elif user == 'n' and room['foyer']:
    print(UserInterface(room['overlook']))
elif user == 'e' and room['foyer']:
    print(UserInterface(room['narrow']))
else:
    print("Error User Not allowed to move there")
    print(UserInterface(room['foyer']))

# if user == "s" and room['overlook']:
#     print(UserInterface(room['foyer']))
# else:
#     print("Error User Not allowed to move there")
#     print(UserInterface(room['overlook']))

# if user == "w" and room['narrow']:
#     print(UserInterface(room['foyer']))
# elif user == 'n' and room['foyer']:
#     print(UserInterface(room['treasure']))
# else:
#     print("Error User Not allowed to move there")
#     print(UserInterface(room['narrow']))

# if user == "s" and room['treasure']:
#     print(UserInterface(room['narrow']))
# else:
#     print("Error User Not allowed to move there")
#     print(UserInterface(room['treasure']))

