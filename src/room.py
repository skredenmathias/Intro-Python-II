# Implement a class to hold room information. This should have name and
# description attributes.








class Room(self, name, description, items):

    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.pop(item)
    
    def __str__(self):
        return f'{self.name}, {self.description}'

    def print_description():




['outside', 'foyer', 'overlook', 'narrow', 'treasure']


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']