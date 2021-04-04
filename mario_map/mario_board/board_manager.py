from mario_map.mario_board.pipeline_finder import PipelineFinder
from mario_map.mario_board.position import Position
from mario_map.mario_board.html_generator import HtmlGenerator
from mario_map.mario_board.heuristic_factory import HeuristicFactory
from mario_map.mario_board.board import Board
from mario_map.mario_board.board_marker import BoardMarker


class BoardManager:
    def __init__(self):
        self.board = Board()
        self.total_states = 0
        self.current_h = HeuristicFactory.rect_line_h

    def _find_pipeline(self):
        if self.board.mario is not None:
            HeuristicFactory.reset()
            _, self.total_states = PipelineFinder.a_star(self.board, self.current_h)
            BoardMarker.mark_all_paths(self.board)

    def create_new_board(self, num_rows, num_cols):
        self.board.init_mario_world(num_rows, num_cols)

    def load_board(self, difficulty):
        if difficulty == "easy":
            self.board.create_easy_board()
        if difficulty == "medium":
            self.board.create_medium_board()
        if difficulty == "difficult":
            pass
        self._find_pipeline()

    def get_html_board(self):
        return HtmlGenerator.create_html_board(self.board)

    def add_element_and_reload(self, name_element, row_pos, col_pos):
        if name_element == "mario":
            self.board.add_mario(Position(row_pos - 1, col_pos - 1))
        if name_element == "pipeline":
            self.board.add_pipelines(Position(row_pos - 1, col_pos - 1))
        if name_element == "wall":
            self.board.add_walls(Position(row_pos - 1, col_pos - 1))
        self.board.reload_board()
        self.total_states = 0
        self._find_pipeline()

    def change_pipe_finder_method(self, name_method):
        if name_method == "rect_line_h":
            self.current_h = HeuristicFactory.rect_line_h
        if name_method == "near_borders_h":
            self.current_h = HeuristicFactory.near_borders_h
        if name_method == "radar_h":
            self.current_h = HeuristicFactory.radar_h
        self.board.reload_board()
        self.total_states = 0
        self._find_pipeline()

#
# a = BoardManager()
# a.load_easy_board()
# print(a.total_states)
# a.get_html_board()
# a = BoardManager()
# a.create_new_board(5, 5)
# a.add_element_and_reload("pipeline", 5, 5)
# print(a.total_states)
# a.get_html_board()
# a = BoardManager()
# a.load_board("medium")
