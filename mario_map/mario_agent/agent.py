from mario_map.mario_board.position import Position


class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function_in_order_to_actions(self, state, actions):
        successors_positions = []
        pos = None
        for action in actions:
            if action == self.settings.UP:
                successors_positions.append(Position(state.position.row - 1, state.position.col))
            if action == self.settings.DOWN:
                successors_positions.append(Position(state.position.row + 1, state.position.col))
            if action == self.settings.LEFT:
                successors_positions.append(Position(state.position.row, state.position.col - 1))
            if action == self.settings.RIGHT:
                successors_positions.append(Position(state.position.row, state.position.col + 1))
        return successors_positions

