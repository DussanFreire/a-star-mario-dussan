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
    def is_a_valid_space(position, boar_dimensions):
        return BoardValidations._is_a_valid_row(position.row, boar_dimensions) and BoardValidations._is_a_valid_col(
            position.col, boar_dimensions)

    @staticmethod
    def is_a_successor(board, state, successor):
        if isinstance(board.get_board_element(state.position), Pipeline):
            return True
        return BoardValidations.is_a_valid_space(successor.position, board.boar_dimensions) and isinstance(board.get_board_element(successor.position), FreeSpace) and BoardValidations._is_a_valid_child(state, successor)
