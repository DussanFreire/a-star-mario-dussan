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
    def is_a_valid_child(state, successor):
        return state.father != successor

    @staticmethod
    def is_a_higher_g_cost(state, successor):
        return successor.g >= state.g

    @staticmethod
    def is_in_the_board(position, boar_dimensions):
        return BoardValidations._is_a_valid_row(position.row, boar_dimensions) and BoardValidations._is_a_valid_col(
            position.col, boar_dimensions)

    @staticmethod
    def is_a_successor(board, state, successor_pos, boar_dimensions):
        if not BoardValidations.is_in_the_board(successor_pos.position, boar_dimensions):
            return False
        if isinstance(board[successor_pos.position.row][successor_pos.position.col], Pipeline):
            return True
        if isinstance(board[successor_pos.position.row][successor_pos.position.col], FreeSpace) and BoardValidations.is_a_valid_child(state, board[successor_pos.position.row][successor_pos.position.col]):
            return True
        return False
