from mario_map.mario_board.position import Position
from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from math import floor

class HeuristicFactory:
    pipe_position = None
    pipe_searching_interval = 0

    @staticmethod
    def reset():
        HeuristicFactory.pipe_position = None
        HeuristicFactory.pipe_searching_interval = 0

    @staticmethod
    def rect_line_h(successor, state, board):
        if state.father is not None:
            if (state.father.position.col == state.position.col == successor.position.col) or (
                    state.father.position.row == state.position.row == successor.position.row):
                return 1
        return 3

    @staticmethod
    def near_borders_h(successor, state, board):
        if successor.position.col == 0 or successor.position.col == board.dimensions.num_cols - 1:
            return 1
        if successor.position.row == 0 or successor.position.row == board.dimensions.num_rows - 1:
            return 1
        else:
            return 2

    @staticmethod
    def radar_h(successor, state, board):
        if HeuristicFactory.pipe_position is None or state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
            HeuristicFactory.pipe_position = HeuristicFactory._get_positions_of_closest_pipe(state.position, board)
            if HeuristicFactory.pipe_position is None:
                return 1
        pipe_quadrant = HeuristicFactory._find_quadrant(HeuristicFactory.pipe_position, state.position)
        if pipe_quadrant == "down_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return 2
        if pipe_quadrant == "upper_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return 2
        if pipe_quadrant == "upper_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return 2
        if pipe_quadrant == "down_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return 2
        if pipe_quadrant == "down":
            if successor.position.col == state.position.col and successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return 1
        if pipe_quadrant == "up":
            if successor.position.col == state.position.col and successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return 1
        if pipe_quadrant == "left":
            if successor.position.col == state.position.col - 1 and successor.position.row == state.position.row:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return 1
        if pipe_quadrant == "right":
            if successor.position.col == state.position.col + 1 and successor.position.row == state.position.row:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(state.position.row - HeuristicFactory.pipe_position.row) >= abs(
                        state.position.col - HeuristicFactory.pipe_position.col) else abs(state.position.col - HeuristicFactory.pipe_position.col)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return 1
        return 8

    @staticmethod
    def _find_quadrant(pipe_position, state_position):
        if pipe_position.col > state_position.col and pipe_position.row > state_position.row:
            return "down_right"
        if pipe_position.col < state_position.col and pipe_position.row < state_position.row:
            return "upper_left"
        if pipe_position.col > state_position.col and pipe_position.row < state_position.row:
            return "upper_right"
        if pipe_position.col < state_position.col and pipe_position.row > state_position.row:
            return "down_left"
        if pipe_position.col < state_position.col and pipe_position.row == state_position.row:
            return "left"
        if pipe_position.col > state_position.col and pipe_position.row == state_position.row:
            return "right"
        if pipe_position.col == state_position.col and pipe_position.row < state_position.row:
            return "up"
        if pipe_position.col == state_position.col and pipe_position.row > state_position.row:
            return "down"

    @staticmethod
    def _get_positions_of_closest_pipe(state_position, board):
        radar_size = 0
        ri = rf = ci = cf = None
        while radar_size < board.dimensions.num_rows or radar_size < board.dimensions.num_cols:
            radar_size += 1
            ri = state_position.row - radar_size if 0 <= state_position.row - radar_size else 0
            rf = state_position.row + radar_size if state_position.row + radar_size <= board.dimensions.num_rows else board.dimensions.num_rows
            ci = state_position.col - radar_size if 0 <= state_position.col - radar_size else 0
            cf = state_position.col + radar_size if state_position.col + radar_size <= board.dimensions.num_cols else board.dimensions.num_cols
            aux = floor((rf-ri)/2) + ri
            ctt= -1
            for c in range(ci, cf+1):
                row = aux +1
                columna = c +1
                if aux == ri:
                    ctt = 1
                if BoardValidations.is_in_the_board(Position(aux, c), board.dimensions) and isinstance(board.board[aux][c], Pipeline):
                    return Position(((ri + rf)/2) + 1 - aux, c)
                aux += ctt
            aux = floor((rf-ri)/2) + ri
            ctt= 1
            for c in range(ci, cf+1):
                row_1 = aux +1
                columna_1 = c +1
                if aux == rf:
                    ctt = -1
                if BoardValidations.is_in_the_board(Position(aux, c), board.dimensions) and isinstance(board.board[aux][c], Pipeline):
                    return Position(((ri + rf)/2) + 1 - aux, c)
                aux += ctt
        return None
