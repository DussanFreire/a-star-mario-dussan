from mario_map.mario_board.pipeline_finder import PipelineFinder
from mario_map.mario_board.position import Position
from mario_map.mario_board.html_generator import HtmlGenerator
from mario_map.mario_board.heuristic_factory import HeuristicFactory
from mario_map.mario_board.board import Board
from mario_map.mario_board.board_marker import BoardMarker
import datetime


class BoardManager:
    def __init__(self):
        self.board = Board()
        self.current_h = HeuristicFactory.rect_line_h
        self.total_states = 0
        self.deep = 0
        self.branch_factor = 0

    def _init_calculable_prop(self):
        self.total_states = 0
        self.deep = 0
        self.branch_factor = 0

    def _find_pipeline_using_a_star(self):
        if self.board.mario is not None:
            HeuristicFactory.reset()
            start = datetime.datetime.now()
            _, self.total_states, self.deep = PipelineFinder.a_star(self.board, self.current_h)
            self.time = (datetime.datetime.now() - start).microseconds
            BoardMarker.mark_all_paths(self.board)
            self._calculate_branching_factor()

    def _find_pipeline_using_bfs(self):
        if self.board.mario is not None:
            HeuristicFactory.reset()
            start = datetime.datetime.now()
            _, self.total_states, self.deep = PipelineFinder.bfs_mario_perspective(self.board)
            self.time = (datetime.datetime.now() - start).microseconds
            BoardMarker.mark_all_paths(self.board)
            self._calculate_branching_factor()

    def create_new_board(self, num_rows, num_cols):
        self.board.init_mario_world(num_rows, num_cols)

    def load_board(self, difficulty):
        self._init_calculable_prop()
        if difficulty == "easy":
            self.board.create_easy_board()
        if difficulty == "medium":
            self.board.create_medium_board()
        if difficulty == "difficult":
            self.board.create_difficult_board()
        self._find_pipeline_using_a_star()

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
        self._init_calculable_prop()
        self._find_pipeline_using_a_star()

    def change_pipe_finder_method(self, name_method):
        self.board.reload_board()
        self._init_calculable_prop()
        if name_method == "rect_line_h":
            self.current_h = HeuristicFactory.rect_line_h
            self._find_pipeline_using_a_star()
        if name_method == "near_borders_h":
            self.current_h = HeuristicFactory.near_borders_h
            self._find_pipeline_using_a_star()
        if name_method == "radar_h":
            self.current_h = HeuristicFactory.radar_h
            self._find_pipeline_using_a_star()
        if name_method == "bfs":
            self._find_pipeline_using_bfs()

    def _calculate_branching_factor(self):
        aux_deep = self.deep
        exp = 0
        while aux_deep > 0:
            exp += aux_deep
            aux_deep -= 1
        self.branch_factor = (self.total_states + 2) ** (1/exp)

