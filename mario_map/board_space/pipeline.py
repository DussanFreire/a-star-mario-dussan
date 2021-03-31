from mario_map.mario_board.position import Position


class Pipeline:
    def __init__(self, row, col):
        self.value = "🏁"
        self.position = Position(row, col)
        self.color = "white"


