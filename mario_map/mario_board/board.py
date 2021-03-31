from mario_map.board_space.wall import Wall
from mario_map.board_space.free_space import FreeSpace
from mario_map.board_space.pipeline import Pipeline
from mario_map.mario_board.board_distance_finder import BoardDistanceFinder
from mario_map.mario_board.position import Position
from mario_map.mario_board.dimensions import Dimensions
from mario_map.board_space.mario import Mario


class Board:
    def __init__(self):
        self.boar_dimensions = None
        self.board = None
        self.mario = None
        self.total_states = 0

    def init_board(self, num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(FreeSpace())
        self.boar_dimensions = Dimensions(num_rows, num_cols)
        self.mario = None
        self.board = matrix
        self.total_states = 0

    def _add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def _add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall()

    def _add_mario(self, position):
        if self.mario is not None:
            self.board[self.mario.position.row][self.mario.position.col] = FreeSpace()
        self.mario = Mario()
        self.mario.position = position
        self.board[position.row][position.col] = self.mario

    def load_default_board(self):
        self.init_board(4, 4)
        self._add_pipelines(Position(0, 3), Position(3, 0))
        self._add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3))
        self._add_mario(Position(0, 0))
        self._mark_distances()
        self._find_shortest_path()

    def _mark_distances(self):
        self.total_states = BoardDistanceFinder.mark_distances(self.board, self.boar_dimensions)

    def _find_shortest_path(self):
        if self.mario is not None:
            return BoardDistanceFinder.find_shortest_path(self.board, self.mario.position, self.boar_dimensions)
        return None

    def get_html_board(self):
        tabla = "<head> <table style='background-color:black;'>"
        tabla += "<tr><td></td>"
        for col in range(0, self.boar_dimensions.num_cols):
            tabla += "<td width=20 border=1 style=' border-color: black;color: white; background-color: " \
                     "black;text-align:center;'>" + str(col + 1) + "</td>"
        tabla += "</tr>"
        for row in range(0, self.boar_dimensions.num_rows):
            tabla += "<tr>"
            tabla += "<td width=20 border=1 style='border-color: black;color: white; background-color: " \
                     "black;text-align:center;'>" + str(row + 1) + "</td>"
            for col in range(0, self.boar_dimensions.num_cols):
                value = self.board[row][col].distance if isinstance(self.board[row][col], FreeSpace) else \
                    self.board[row][
                        col].value
                tabla += "<td width=20 border=1 style='border-color: black;color: black; background-color: " + \
                         self.board[row][col].color + ";text-align:center;'>" + str(value) + "</td>"
            tabla += "</tr>"
        tabla += "</table> </head>"
        return tabla

    def _show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    def add_element_and_reload_distances(self, name_element, row_pos, col_pos):
        if name_element == "mario":
            self._add_mario(Position(row_pos - 1, col_pos - 1))
        if name_element == "pipeline":
            self._add_pipelines(Position(row_pos - 1, col_pos - 1))
        if name_element == "wall":
            self._add_walls(Position(row_pos - 1, col_pos - 1))
        self._mark_distances()
        self._find_shortest_path()
