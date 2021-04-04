from mario_map.mario_board.position import Position
from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from mario_map.board_space.wall import Wall


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
        if state.f == 0 or state.f == HeuristicFactory.pipe_searching_interval:
            HeuristicFactory.pipe_position = HeuristicFactory._get_positions_of_closest_pipe(successor.position, board)
            HeuristicFactory.pipe_searching_interval += 10
        # perception_scope = abs(successor.position.row - PipelineFinder.pipe_position.row) if abs(
        #     successor.position.row - PipelineFinder.pipe_position.row) >= abs(
        #     successor.position.col - PipelineFinder.pipe_position.col) else abs(
        #     successor.position.col - PipelineFinder.pipe_position.col)
        # _context = PipelineFinder._get_positions_percepted(successor.position, perception_scope, board)
        pipe_quadrant = HeuristicFactory._find_quadrant(HeuristicFactory.pipe_position, state.position)
        if pipe_quadrant == "down_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row + 1:
                return 2
        if pipe_quadrant == "upper_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row - 1:
                return 2
        if pipe_quadrant == "upper_right":
            if successor.position.col == state.position.col + 1 or successor.position.row == state.position.row - 1:
                return 2
        if pipe_quadrant == "down_left":
            if successor.position.col == state.position.col - 1 or successor.position.row == state.position.row + 1:
                return 2
        if pipe_quadrant == "down":
            if successor.position.col == state.position.col and successor.position.row == state.position.row + 1:
                return 1
        if pipe_quadrant == "up":
            if successor.position.col == state.position.col and successor.position.row == state.position.row - 1:
                return 1
        if pipe_quadrant == "left":
            if successor.position.col == state.position.col - 1 and successor.position.row == state.position.row:
                return 1
        if pipe_quadrant == "right":
            if successor.position.col == state.position.col + 1 and successor.position.row == state.position.row:
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
        radar_size = 1
        ri = rf = ci = cf = None
        while radar_size < board.dimensions.num_rows or radar_size < board.dimensions.num_cols:
            radar_size += 1
            ri = state_position.row - radar_size if 0 <= state_position.row - radar_size else 0
            rf = state_position.row + radar_size if state_position.row + radar_size <= board.dimensions.num_rows else board.dimensions.num_rows
            ci = state_position.col - radar_size if 0 <= state_position.col - radar_size else 0
            cf = state_position.col + radar_size if state_position.col + radar_size <= board.dimensions.num_cols else board.dimensions.num_cols
            for row in [ri, rf]:
                for col in range(ci, cf):
                    if BoardValidations.is_in_the_board(Position(row, col), board.dimensions) and isinstance(
                            board.board[row][col], Pipeline):
                        return Position(row, col)
            for row in range(ri, rf):
                for col in [ci, cf]:
                    if BoardValidations.is_in_the_board(Position(row, col), board.dimensions) and isinstance(
                            board.board[row][col], Pipeline):
                        return Position(row, col)

    @staticmethod
    def _get_positions_percepted(state_position, perception_scope, board):
        positions_percepted = []
        # right perception
        positions_percepted.append([])
        for row in range(state_position.row + 1, state_position.row + perception_scope + 1):
            if row >= board.dimensions.num_rows:
                positions_percepted[0].append(None)
            elif isinstance(board.board[row][state_position.col], Wall):
                positions_percepted[0].append("wall")
            else:
                positions_percepted[0].append(Position(row, state_position.col))
        # left perception
        positions_percepted.append([])
        for row in range(state_position.row - 1, state_position.row - perception_scope - 1, -1):
            if row <= 0:
                positions_percepted[1].append(None)
            elif isinstance(board.board[row][state_position.col], Wall):
                positions_percepted[1].append("wall")
            else:
                positions_percepted[1].append(Position(row, state_position.col))
        # up perception
        positions_percepted.append([])
        for col in range(state_position.col - 1, state_position.col - perception_scope - 1, -1):
            if col <= 0:
                positions_percepted[2].append(None)
            elif isinstance(board.board[state_position.row][col], Wall):
                positions_percepted[2].append("wall")
            else:
                positions_percepted[2].append(Position(state_position.row, col))
        # down perception
        positions_percepted.append([])
        for col in range(state_position.col + 1, state_position.col + perception_scope + 1):
            if col >= board.dimensions.num_cols:
                positions_percepted[3].append(None)
            elif isinstance(board.board[state_position.row][col], Wall):
                positions_percepted[3].append("wall")
            else:
                positions_percepted[3].append(Position(state_position.row, col))
        return positions_percepted