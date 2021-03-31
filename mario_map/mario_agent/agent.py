from mario_map.mario_board.position import Position


class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function(self, position, actions):
        successors = []
        for action in actions:
            if action == self.settings.UP:
                successors.append(Position(position.row - 1, position.col))
            if action == self.settings.DOWN:
                successors.append(Position(position.row + 1, position.col))
            if action == self.settings.LEFT:
                successors.append(Position(position.row, position.col - 1))
            if action == self.settings.RIGHT:
                successors.append(Position(position.row, position.col + 1))

        return successors
