class FreeSpace:
    def __init__(self):
        self.mario_is_here = False
        self.value = "_"
        self.distance = 0
        self.color = "white"
        self.father = None
        self.position = None
        self.visited = False

    def place_mario(self, position):
        self.value = "👨"
        self.mario_is_here = True
        self.position = position

    def take_out_mario(self):
        self.value = "_"
        self.mario_is_here = False
        self.position = None
