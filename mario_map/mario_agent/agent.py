from mario_map.mario_board.position import Position
from mario_map.mario_agent.successor import Successor


def _create_successor_with_pos(position, father):
    successor = Successor(position, father)
    return successor


class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function(self, father, actions):
        successors = []
        pos = None
        for action in actions:
            if action == self.settings.UP:
                pos = Position(father.position.row - 1, father.position.col)
            if action == self.settings.DOWN:
                pos = Position(father.position.row + 1, father.position.col)
            if action == self.settings.LEFT:
                pos = Position(father.position.row, father.position.col - 1)
            if action == self.settings.RIGHT:
                pos = Position(father.position.row, father.position.col + 1)
            successors.append(_create_successor_with_pos(pos, father))
        return successors
