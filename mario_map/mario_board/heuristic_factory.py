from mario_map.mario_board.position import Position
from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline


class HeuristicFactory:
    pipe_position = None
    pipe_searching_interval = 0

    @staticmethod
    def reset():
        # reset pipe property's used in radar_h
        HeuristicFactory.pipe_position = None
        HeuristicFactory.pipe_searching_interval = 0

    @staticmethod
    def rect_line_h(successor, state, board):
        # rect line based on the board dimensions
        if state.father is not None:
            if (state.father.position.col == state.position.col == successor.position.col) or (
                    state.father.position.row == state.position.row == successor.position.row):
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        return (board.dimensions.num_cols * board.dimensions.num_rows) + 3

    @staticmethod
    def near_borders_h(successor, state, board):
        # near borders based on the board dimensions
        if successor.position.col == 0 or successor.position.col == board.dimensions.num_cols - 2:
            return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        if successor.position.row == 0 or successor.position.row == board.dimensions.num_rows - 2:
            return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        else:
            return (board.dimensions.num_cols * board.dimensions.num_rows) + 2

    @staticmethod
    def radar_h(successor, state, board):
        # radar based on the board dimensions and the pipe position
        if HeuristicFactory.pipe_position is None or state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
            HeuristicFactory.pipe_position = HeuristicFactory._get_positions_of_closest_pipe(state.position, board)
            if HeuristicFactory.pipe_position is None:
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        pipe_quadrant = HeuristicFactory._classified_pipe(HeuristicFactory.pipe_position, state.position)
        if pipe_quadrant == "down_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 2
        if pipe_quadrant == "upper_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 2
        if pipe_quadrant == "upper_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 2
        if pipe_quadrant == "down_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 2 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 2
        if pipe_quadrant == "down":
            if successor.position.col == state.position.col and successor.position.row == state.position.row + 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        if pipe_quadrant == "up":
            if successor.position.col == state.position.col and successor.position.row == state.position.row - 1:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        if pipe_quadrant == "left":
            if successor.position.col == state.position.col - 1 and successor.position.row == state.position.row:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        if pipe_quadrant == "right":
            if successor.position.col == state.position.col + 1 and successor.position.row == state.position.row:
                if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
                    perception_scope = HeuristicFactory.get_perception_scope(state)
                    HeuristicFactory.pipe_searching_interval = perception_scope + 1 + state.f
                return (board.dimensions.num_cols * board.dimensions.num_rows) + 1
        return (board.dimensions.num_cols * board.dimensions.num_rows) + 8

    @staticmethod
    def get_perception_scope(state):
        perception_scope = abs(state.position.row - HeuristicFactory.pipe_position.row) if abs(
            state.position.row - HeuristicFactory.pipe_position.row) >= abs(
            state.position.col - HeuristicFactory.pipe_position.col) else abs(
            state.position.col - HeuristicFactory.pipe_position.col)
        return perception_scope

    @staticmethod
    def _classified_pipe(pipe_position, state_position):
        # classified pipe based in it's position in comparison of the state position
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
        # find the closest pipe
        radar_size = 0
        while radar_size < board.dimensions.num_rows or radar_size < board.dimensions.num_cols:
            # set range for the quick search
            radar_size += 1
            ri = state_position.row - radar_size
            rf = state_position.row + radar_size
            ci = state_position.col - radar_size
            cf = state_position.col + radar_size
            aux = state_position.row
            ctt = -1
            for c in range(ci, cf + 1):
                if aux == ri:
                    ctt = 1
                if BoardValidations.is_in_the_board(Position(aux, c), board.dimensions) and isinstance(
                        board.board[aux][c], Pipeline):
                    return Position(aux, c)
                aux += ctt
            aux = state_position.row
            ctt = 1
            for c in range(ci, cf + 1):
                if aux == rf:
                    ctt = -1
                if BoardValidations.is_in_the_board(Position(aux, c), board.dimensions) and isinstance(
                        board.board[aux][c], Pipeline):
                    return Position(aux, c)
                aux += ctt
        return None
