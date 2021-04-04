from mario_map.mario_board.board_marker import BoardMarker
from mario_map.mario_board.board_validations import BoardValidations
from mario_map.mario_agent.settings import Settings
from mario_map.mario_agent.agent import Agent
import queue


class PipelineFinder:
    settings = Settings()
    agent = Agent(settings)

    @staticmethod
    def show_board(board):
        print("****************************************************************************************************")
        for line in board:
            for elem in line:
                print(elem.display_value, end="\t")
            print()
        print()

    @staticmethod
    def a_star(board, heuristic_function):
        open_states = queue.PriorityQueue()
        closed_states = []
        board.mario.set_costs(0, 0)
        number_of_state = 1
        open_states.put((0, number_of_state, board.mario))
        while open_states.qsize() != 0:
            f, _, state = open_states.get()
            closed_states.append(state)
            BoardMarker.mark_element(state)
            if BoardValidations.is_a_pipe(state):  # goal_state(state):
                return True, len(closed_states)
            # PipelineFinder.show_board(board.board)
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN,
                       PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            successors_pos = PipelineFinder.agent.transition_function_in_order_to_actions(state, actions)
            for successor_pos in successors_pos:
                if not BoardValidations.is_in_the_board(successor_pos, board.dimensions):
                    continue
                successor = board.get_board_element(successor_pos)
                successor.position = successor_pos
                # la primera condicion es experimental
                if successor in closed_states or BoardValidations.is_not_a_valid_element(successor, state) or successor.visited or successor.father is not None:
                    continue
                successor.father = state
                number_of_state += 1
                if BoardValidations.is_a_pipe(successor):
                    open_states.put((0, number_of_state, successor))
                    break
                if BoardValidations.is_a_free_space(successor):
                    successor.set_costs(heuristic_function(successor, state, board), state.g + 1)
                    open_states.put((successor.f, number_of_state, successor))


                # if successor in open_states:
                #     if successor.g >= state.g in open_states:
                #         continue

        return False, len(closed_states)


# hacer un debug mostrando el mapa
