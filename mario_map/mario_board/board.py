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

    def create_medium_board(self):
        self.init_mario_world(20, 40)
        self.add_pipelines(Position(10, 10))
        self.add_pipelines(Position(5, 13))

    # self.add_walls(Position(3, 1),
        #                Position(4, 1),
        #                Position(5, 1),
        #                Position(6, 1),
        #                Position(7, 1),
        #                Position(8, 1),
        #                Position(0, 3),
        #                Position(1, 3),
        #                Position(2, 3),
        #                Position(3, 3),
        #                Position(4, 3),
        #                Position(5, 3),
        #                Position(6, 3),
        #                Position(7, 3),
        #                Position(8, 3))
        self.add_mario(Position(10, 20))

    def _show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.display_value, end="\t")
            print()
        print()
