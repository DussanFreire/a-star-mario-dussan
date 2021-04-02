from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from mario_map.board_space.free_space import FreeSpace
from mario_map.mario_agent.settings import Settings
from mario_map.mario_agent.successor import Successor
from mario_map.mario_agent.agent import Agent
import queue


class BoardDistanceFinder:
    settings = Settings()
    agent = Agent(settings)

    @staticmethod
    def show_board(board):
        for line in board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    @staticmethod
    def clean_board(board):
        for row in board:
            for element in row:
                element.color = BoardDistanceFinder.settings.COLOR_WHITE
                if isinstance(element, FreeSpace):
                    element.distance = 0

    @staticmethod
    def a_star(board, marios_position):
        open_states = queue.SimpleQueue()
        closed_states = []
        root = Successor(marios_position, None, 0, 0, 0)
        open_states.put(root)
        while open_states.qsize() != 0:
            state = open_states.get()
            closed_states.append(state)
            if isinstance(state, Pipeline):  # goal_state(state):
                return True
            actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN,
                       BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
            # se agregara la opcion de ver a lo lejos
            successors = BoardDistanceFinder.agent.transition_function(state, actions)
            for successor in successors:
                if successor in closed_states:
                    continue
                if not BoardValidations.is_a_valid_space(successor.position, board.boar_dimensions):
                    continue
                successor.h = BoardDistanceFinder.rect_line_h(successor)
                successor.g = state.g + 1  # cost(state,successor)
                successor.f = successor.g + successor.h
                if successor in open_states:
                    if successor.g >= state.g in open_states:
                        continue
                open_states.put(successor)
        return False

    @staticmethod
    def rect_line_h(successor):
        if successor.father is None:
            return 0
        if (successor.father.position.col == successor.col) or (successor.father.position.row == successor.row):
            return 1
        return 2
