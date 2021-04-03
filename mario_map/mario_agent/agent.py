from mario_map.mario_board.position import Position


class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function(self, father, actions):
        successors_positions = []
        pos = None
        for action in actions:
            if action == self.settings.UP:
                successors_positions.append(Position(father.position.row - 1, father.position.col))
            if action == self.settings.DOWN:
                successors_positions.append(Position(father.position.row + 1, father.position.col))
            if action == self.settings.LEFT:
                successors_positions.append(Position(father.position.row, father.position.col - 1))
            if action == self.settings.RIGHT:
                successors_positions.append(Position(father.position.row, father.position.col + 1))
        return successors_positions
