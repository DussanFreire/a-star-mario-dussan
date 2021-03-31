from mario_map.board_space.free_space import FreeSpace
from mario_map.board_space.pipeline import Pipeline


class BoardValidations:
    @staticmethod
    def _is_a_valid_row(row, boar_dimensions):
        return 0 <= row < boar_dimensions.num_rows

    @staticmethod
    def _is_a_valid_col(col, boar_dimensions):
        return 0 <= col < boar_dimensions.num_cols

    @staticmethod
    def _is_a_valid_child(state, successor):
        return state.father != successor

    @staticmethod
    def _is_a_valid_distance_to_change(state, successor):
        return successor.distance == 0  # or successor.distance > state.distance + 1

    @staticmethod
    def is_a_valid_successor(successor, state):
        if isinstance(state, Pipeline):
            return True
        return BoardValidations._is_a_valid_child(state, successor) and BoardValidations._is_a_valid_distance_to_change(
            state, successor)

    @staticmethod
    def is_a_valid_space(position, boar_dimensions):
        return BoardValidations._is_a_valid_row(position.row, boar_dimensions) and BoardValidations._is_a_valid_col(
            position.col, boar_dimensions)

    @staticmethod
    def is_a_successor(board, state_position, successor_position, boar_dimensions):
        state = board[state_position.row][state_position.col]
        return BoardValidations.is_a_valid_space(successor_position, boar_dimensions) and \
               isinstance(board[successor_position.row][successor_position.col], FreeSpace) and \
               BoardValidations.is_a_valid_successor(board[successor_position.row][successor_position.col], state)
