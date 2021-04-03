from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from mario_map.board_space.free_space import FreeSpace
from mario_map.board_space.wall import Wall
from mario_map.mario_agent.settings import Settings
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
    def a_star(board, boar_dimensions, mario):
        open_states = queue.PriorityQueue()
        closed_states = []
        mario.set_costs(0, 0)
        number_of_state = 1
        open_states.put((0, number_of_state, mario))
        while open_states.qsize() != 0:
            f, _, state = open_states.get()
            closed_states.append(state)
            if isinstance(state, Pipeline):  # goal_state(state):
                return True, number_of_state
            PipelineFinder.mark_element(state)
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN,
                       PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            # se agregara la option de ver a lo lejos
            successors_pos = PipelineFinder.agent.transition_function(state, actions)
            for successor_pos in successors_pos:
                if successor_pos in closed_states:
                    continue
                if not BoardValidations.is_in_the_board(successor_pos, boar_dimensions):
                    continue
                successor = board[successor_pos.row][successor_pos.col]
                successor.position = successor_pos
                if isinstance(successor, Wall):
                    continue
                if not BoardValidations.is_a_valid_child(state, successor):
                    continue
                if successor.visited:
                    continue
                successor.father = state
                if isinstance(successor, Pipeline):
                    number_of_state += 1
                    open_states.put((1, number_of_state, successor))
                    successor.space_visited(PipelineFinder.settings.COLOR_GREEN)
                    break
                else:
                    successor.set_costs(PipelineFinder.rect_line_h(successor), state.g + 1)
                    successor.space_visited(PipelineFinder.settings.COLOR_GREEN, successor.f)
                    number_of_state += 1
                    open_states.put((successor.f, number_of_state, successor))

                # if successor in open_states:
                #     if successor.g >= state.g in open_states:
                #         continue

        return False, number_of_state

    @staticmethod
    def mark_element(state):
        if state.mario_is_here:
            state.space_visited(PipelineFinder.settings.COLOR_GREEN)
        else:
            state.space_visited(PipelineFinder.settings.COLOR_GREEN, state.f)

    @staticmethod
    def rect_line_h(successor):
        if successor.father.father is not None:
            if (successor.father.father.position.col == successor.father.position.col == successor.position.col) or (
                    successor.father.father.position.row == successor.father.position.row == successor.position.row):
                return 0
        if successor.father.position.col == successor.father.position.col or successor.father.position.row == successor.position.row:
            return 1
        return 2
