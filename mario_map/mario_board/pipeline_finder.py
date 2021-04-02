from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from mario_map.board_space.free_space import FreeSpace
from mario_map.mario_agent.settings import Settings
from mario_map.mario_agent.successor import Successor
from mario_map.mario_agent.agent import Agent
import queue


class PipelineFinder:
    settings = Settings()
    agent = Agent(settings)

    @staticmethod
    def show_board(board):
        for line in board:
            for elem in line:
                print(elem.display_value, end="\t")
            print()
        print()

    @staticmethod
    def clean_board(board):
        for row in board:
            for element in row:
                element.color = PipelineFinder.settings.COLOR_WHITE
                if isinstance(element, FreeSpace):
                    element.distance = 0

    @staticmethod
    def a_star(board, mario):
        open_states = queue.SimpleQueue()
        closed_states = []
        root = Successor(mario, mario.position, None, 0, 0, 0)
        open_states.put(root)
        while open_states.qsize() != 0:
            state = open_states.get()
            PipelineFinder.mark_element(state)
            closed_states.append(state)
            if isinstance(state.element, Pipeline):  # goal_state(state):
                return True
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN,
                       PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            # se agregara la option de ver a lo lejos
            successors = PipelineFinder.agent.transition_function(state, actions)
            for successor in successors:
                if successor in closed_states:
                    continue
                if not BoardValidations.is_a_valid_space(successor.position, board.boar_dimensions):
                    continue
                successor.set_costs(PipelineFinder.rect_line_h(successor), state.g + 1)
                if successor in open_states:
                    if successor.g >= state.g in open_states:
                        continue
                open_states.put(successor)
        return False

    @staticmethod
    def mark_element(state):
        if not state.element.mario_is_here():
            state.element.space_visited(PipelineFinder.settings.COLOR_GREEN, state.father.distance)
        else:
            state.element.space_visited(PipelineFinder.settings.COLOR_GREEN, - 1)

    @staticmethod
    def rect_line_h(successor):
        if successor.father is None:
            return 0
        if (successor.father.position.col == successor.col) or (successor.father.position.row == successor.row):
            return 1
        return 2
