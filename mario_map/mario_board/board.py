from mario_map.board_space.wall import Wall
from mario_map.board_space.free_space import FreeSpace
from mario_map.board_space.pipeline import Pipeline
from mario_map.mario_board.position import Position
from mario_map.mario_board.dimensions import Dimensions


class Board:
    def __init__(self):
        self.dimensions = None
        self.board = None
        self.mario = FreeSpace()

    def init_mario_world(self, num_rows, num_cols):
        self.dimensions = Dimensions(num_rows, num_cols)
        self.board = self._init_board()
        self.add_mario(Position(0, 0))

    def _init_board(self):
        matrix = []
        for row in range(0, self.dimensions.num_rows):
            matrix.append([])
            for col in range(0, self.dimensions.num_cols):
                matrix[row].append(FreeSpace())
        return matrix

    def reload_board(self):
        for row in range(0, self.dimensions.num_rows):
            for col in range(0, self.dimensions.num_cols):
                if isinstance(self.board[row][col], Pipeline) or isinstance(self.board[row][col], FreeSpace):
                    self.board[row][col].reset_space()

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall()

    def add_mario(self, position):
        self.mario.take_out_mario()
        new_mario = FreeSpace()
        new_mario.place_mario(position)
        self.board[position.row][position.col] = new_mario
        self.mario = new_mario

    def get_board_element(self, position):
        return self.board[position.row][position.col]

    def create_easy_board(self):
        self.init_mario_world(20, 40)
        self.add_pipelines(Position(10, 35))
        self.add_mario(Position(10, 5))

    def create_medium_board(self):
        self.init_mario_world(10, 10)
        self.add_pipelines(Position(2, 9))
        self.add_walls(Position(3, 1),
                       Position(4, 1),
                       Position(5, 1),
                       Position(6, 1),
                       Position(7, 1),
                       Position(8, 1),
                       Position(0, 3),
                       Position(1, 3),
                       Position(2, 3),
                       Position(3, 3),
                       Position(4, 3),
                       Position(5, 3),
                       Position(6, 3),
                       Position(7, 3),
                       Position(8, 3))
        self.add_mario(Position(6, 0))

    def create_difficult_board(self):
        self.init_mario_world(20, 40)
        self.add_pipelines(Position(0, 1))
        self.add_pipelines(Position(12, 26))
        self.add_pipelines(Position(14, 24))

        self.add_walls(Position(3, 1),
                       Position(18, 13),
                       Position(18, 14),
                       Position(18, 15),
                       Position(18, 16),
                       Position(18, 17),
                       Position(18, 18),
                       Position(18, 19),
                       Position(13, 19),
                       Position(14, 19),
                       Position(15, 19),
                       Position(16, 19),
                       Position(17, 19),
                       Position(18, 19),
                       Position(1, 29),
                       Position(14, 21),
                       Position(15, 21),
                       Position(16, 21),
                       Position(17, 21),
                       Position(18, 21),
                       Position(19, 21),
                       Position(2, 29),
                       Position(3, 29),
                       Position(4, 29),
                       Position(4, 30),
                       Position(4, 31),
                       Position(4, 32),
                       Position(4, 33),
                       Position(5, 33),
                       Position(6, 33),
                       Position(7, 33),
                       Position(8, 33),
                       Position(9, 33),
                       Position(10, 33),
                       Position(11, 33),
                       Position(12, 33),
                       Position(13, 33),
                       Position(0, 3),
                       Position(1, 3),
                       Position(2, 3),
                       Position(3, 3),
                       Position(4, 3),
                       Position(5, 3),
                       Position(6, 3),
                       Position(7, 3),
                       Position(8, 3),
                       Position(9, 3),
                       Position(10, 3),
                       Position(11, 3),
                       Position(12, 3),
                       Position(13, 3),
                       Position(14, 3),
                       Position(15, 3),
                       Position(16, 3),
                       Position(17, 3),
                       Position(8, 3),
                       Position(11, 30),
                       Position(11, 29),
                       Position(11, 28),
                       Position(11, 27),
                       Position(11, 26),
                       Position(11, 25),
                       Position(12, 25),
                       Position(13, 25),
                       Position(14, 25),
                       Position(15, 25),
                       Position(16, 25),
                       Position(17, 25),
                       Position(18, 25),
                       Position(19, 25),
                       Position(8, 0),
                       Position(8, 1),
                       Position(12, 27),
                       Position(13, 27),
                       Position(14, 28),
                       Position(15, 28),
                       Position(16, 28),
                       Position(17, 27),
                       Position(18, 29),
                       Position(16, 29),
                       Position(16, 30),
                       Position(17, 31),
                       Position(18, 27),
                       Position(19, 29),
                       Position(18, 31),
                       Position(19, 33),
                       Position(15, 26),
                       Position(6, 24),
                       Position(7, 24),
                       Position(8, 24),
                       Position(9, 24),
                       Position(10, 24),
                       Position(11, 24),
                       Position(12, 24),
                       Position(13, 24),
                       Position(12,19),
                       Position(12,20),
                       Position(12,21),
                       Position(12,22),
                       Position(12,23),
                       Position(12,24),
                       Position(17,4),
                       Position(17,5),
                       Position(17,6),
                       Position(17,7),
                       Position(17,8),
                       Position(17,9),
                       Position(14,5),
                       Position(14,6),
                       Position(14,7),
                       Position(14,8),
                       Position(14,9),
                       Position(14,10),
                       Position(14,11),
                       Position(15,11),
                       Position(16,11),
                       Position(17,11),
                       Position(18,11),
                       Position(19,11),
                       Position(6,26),
                       Position(7,26),
                       Position(8,26),
                       Position(9,26),
                       Position(9,27),
                       Position(9,28),
                       Position(9,29),
                       Position(9,30),
                       Position(9,31),
                       Position(9,32),
                       Position(15,6),
                       Position(16,8),
                       Position(18,6),
                       Position(19,8),
                       Position(16,33),
                       Position(15,33),
                       Position(14,33),
                       Position(17,33),
                       Position(18,33),
                       Position(19,33),
                       Position(13,23),
                       Position(14,23),
                       Position(15,23),
                       Position(16,23),
                       Position(17,23),
                       Position(18,23),
                       Position(15,12),
                       Position(15,13),
                       Position(15,14),
                       Position(15,15),
                       Position(15,16),
                       Position(15,17),


                       )
        self.add_mario(Position(0, 15))

    def _show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.display_value, end="\t")
            print()
        print()
