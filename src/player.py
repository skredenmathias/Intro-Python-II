# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_to(direction, current_loc):
        # try to move in the specified direction
        attribute = direction + '_to'

        # check if we can move in the specified direction
        if hasattr(current_loc, attribute):
            # get the room in the specified direction
            return getattr(current_loc, attribute)

        # if we cannot
        print('cannot go there\n ')

        return current_loc