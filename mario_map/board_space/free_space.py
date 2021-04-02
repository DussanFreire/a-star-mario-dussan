class FreeSpace:
    def __init__(self):
        self.mario_is_here = False
        self.display_value = "_"
        self.color = "white"
        self.father = None
        self.position = None
        self.visited = False

    def place_mario(self, position):
        self.display_value = "👨"
        self.mario_is_here = True
        self.position = position

    def take_out_mario(self):
        self.display_value = "_"
        self.mario_is_here = False
        self.position = None

    def space_visited(self, color, father_distance):
        self.visited = True
        self.color = color
        self.display_value = father_distance + 1
