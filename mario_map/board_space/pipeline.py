from mario_map.mario_board.position import Position


class Pipeline:
    def __init__(self, row, col):
        self.display_value = "🏁"
        self.position = Position(row, col)
        self.color = "white"
        self.father = None
        self.visited = False

    def space_visited(self, color):
        self.visited = True
        self.color = color

    def reset_space(self):
        self.display_value = "🏁"
        self.color = "white"
        self.father = None
        self.visited = False
