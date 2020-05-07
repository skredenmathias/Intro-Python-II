import textwrap
from room import Room
import os

# os.system('cls')

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
player = Player('Mathias', room = room['outside'])

done = False

def print_help_text():
    print('available commands are n, e, s, w')

# Write a loop that:
while not done:

# * Prints the current room name
print(player.location)
# * Prints the current description (the textwrap module might be useful here).
for line in textwrap.wrap(player.location.print_description()):
    print(line)
# * Waits for user input and decides what to do.
command = input('Oi traveller ')

# check that the command is properly formatted
if len(command) > 2 or len(command) < 1:
    print('\n invalid command\n')
    continue

if command in ['n', 's', 'e', 'w']:
    player.location = player.move_to(command, player.location)
    continue

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if command in ['q', 'quit', 'exit']:
    done = True

if command in ['?', 'help']:
    print_help_text()
    continue

else:
    print('\n invalid command\n')
    continue