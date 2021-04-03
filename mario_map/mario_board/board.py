from mario_map.board_space.wall import Wall
from mario_map.board_space.free_space import FreeSpace
from mario_map.board_space.pipeline import Pipeline
from mario_map.mario_board.pipeline_finder import PipelineFinder
from mario_map.mario_board.position import Position
from mario_map.mario_board.dimensions import Dimensions
from mario_map.mario_board.html_generator import HtmlGenerator


class Board:
    def __init__(self):
        self.boar_dimensions = None
        self.board = None
        self.mario = FreeSpace()
        self.total_states = 0

    def init_mario_world(self, num_rows, num_cols):
        self.boar_dimensions = Dimensions(num_rows, num_cols)
        self.board = self.init_board()
        self.total_states = 0
        self._add_mario(Position(0, 0))

    def init_board(self):
        matrix = []
        for row in range(0, self.boar_dimensions.num_rows):
            matrix.append([])
            for col in range(0, self.boar_dimensions.num_cols):
                matrix[row].append(FreeSpace())
        return matrix

    def reload_board(self):
        for row in range(0, self.boar_dimensions.num_rows):
            for col in range(0, self.boar_dimensions.num_cols):
                if isinstance(self.board[row][col], Pipeline) or isinstance(self.board[row][col], FreeSpace):
                    self.board[row][col].reset_space()
        self.total_states = 0

    def _add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def _add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall()

    def _add_mario(self, position):
        self.mario.take_out_mario()
        new_mario = FreeSpace()
        new_mario.place_mario(position)
        self.board[position.row][position.col] = new_mario
        self.mario = new_mario

    def load_easy_board(self):
        self.init_mario_world(10, 10)
        self._add_pipelines(Position(2, 9))
        self._add_walls(Position(3, 1),
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
        self._add_mario(Position(6, 0))
        return self._find_pipeline()

    def _find_pipeline(self):
        if self.mario is not None:
            _, self.total_states = PipelineFinder.a_star(self.board, self.boar_dimensions, self.mario)

    def get_html_board(self):
        return HtmlGenerator.create_html_board(self.board, self.boar_dimensions)

    def _show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.display_value, end="\t")
            print()
        print()

    def add_element_and_reload(self, name_element, row_pos, col_pos):
        if name_element == "mario":
            self._add_mario(Position(row_pos - 1, col_pos - 1))
        if name_element == "pipeline":
            self._add_pipelines(Position(row_pos - 1, col_pos - 1))
        if name_element == "wall":
            self._add_walls(Position(row_pos - 1, col_pos - 1))
        self.reload_board()
        self._find_pipeline()

    def get_board_element(self, position):
        return self.board[position.row][position.col]


#
# a = Board()
# print(a.load_easy_board())
