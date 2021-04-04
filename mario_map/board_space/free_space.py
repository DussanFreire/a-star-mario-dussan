class FreeSpace:
    def __init__(self, father=None, g=None, h=None, f=None):
        self.mario_is_here = False
        self.display_value = "_"
        self.color = "white"
        self.father = father
        self.position = None
        self.visited = False
        self.h = h
        self.g = g
        self.f = f

    def place_mario(self, position):
        self.display_value = "👨"
        self.mario_is_here = True
        self.position = position

    def take_out_mario(self):
        self.display_value = "_"
        self.mario_is_here = False
        self.position = None

    def space_visited(self, color):
        self.visited = True
        self.color = color
        if not self.mario_is_here:
            self.display_value = self.f

    def set_costs(self, h, g):
        self.h = h
        self.g = g
        self.f = g + h

    def reset_space(self):
        self.display_value = "_"
        self.color = "white"
        self.father = None
        self.visited = False
        self.h = None
        self.g = None
        self.f = None
        if self.mario_is_here:
            self.place_mario(self.position)
        else:
            self.position = None
