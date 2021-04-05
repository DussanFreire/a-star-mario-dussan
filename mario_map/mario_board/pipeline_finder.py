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
    def bfs_mario_perspective(board):
        open = queue.SimpleQueue()
        num_states = 0
        closed =[]
        # start bfs from Mario:
        d=0
        open.put((board.mario, 0))
        while open.qsize() != 0:
            state, d = open.get()
            if state in closed:
                continue
            closed.append(state)
            num_states += 1
            # PipelineFinder.show_board(board.board)
            # Goal Test: return pipe's position
            if BoardValidations.is_a_pipe(state):
                state.space_visited(PipelineFinder.settings.VISITED_COLOR)
                return True, num_states,d

            # Mark state as visited
            if not state.mario_is_here:
                if state.father.mario_is_here:
                    state.display_value = 1
                else:
                    state.display_value = int(state.father.display_value) + 1
            state.visited = True
            state.color = PipelineFinder.settings.VISITED_COLOR
            # Transition Function
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN, PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            successors_pos = PipelineFinder.agent.transition_function_in_order_to_actions(state, actions)
            successors_pos = PipelineFinder.discard_successors_marios_perspective(board, successors_pos)
            if successors_pos:
                d += 1
            # Put the successors into the queue
            for successor_pos in successors_pos:
                successor = board.get_board_element(successor_pos)
                successor.position = successor_pos
                successor.father = state
                open.put((successor,d))

        # No solution
        return False, num_states,d

    @staticmethod
    def discard_successors_marios_perspective(board, successors_pos):
        filtered_successors = []

        for successor_pos in successors_pos:
            if not BoardValidations.is_in_the_board(successor_pos, board.dimensions):
                continue
            successor = board.get_board_element(successor_pos)
            if not (BoardValidations.is_a_free_space(successor) or BoardValidations.is_a_pipe(successor)):
                continue
            if not successor.visited:
                filtered_successors.append(successor_pos)
        return filtered_successors

    @staticmethod
    def a_star(board, heuristic_function):
        open_states = queue.PriorityQueue()
        closed_states = []
        board.mario.set_costs(0, 0)
        number_of_state = 1
        d = None
        open_states.put((0, number_of_state, board.mario, 0))
        while open_states.qsize() != 0:
            f, _, state, d = open_states.get()
            closed_states.append(state)
            BoardMarker.mark_element(state)
            if BoardValidations.is_a_pipe(state):  # goal_state(state):
                return True, len(closed_states), d
            # PipelineFinder.show_board(board.board)
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN,
                       PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            successors_pos = PipelineFinder.agent.transition_function_in_order_to_actions(state, actions)
            if successors_pos:
                d += 1
            for successor_pos in successors_pos:

                if not BoardValidations.is_in_the_board(successor_pos, board.dimensions):
                    continue
                successor = board.get_board_element(successor_pos)
                successor.position = successor_pos
                if successor in closed_states or BoardValidations.is_not_a_valid_element(successor, state) or successor.visited or successor.father is not None:
                    continue
                successor.father = state
                number_of_state += 1
                if BoardValidations.is_a_pipe(successor):
                    open_states.put((0, number_of_state, successor, d))
                    break
                if BoardValidations.is_a_free_space(successor):
                    successor.set_costs(heuristic_function(successor, state, board), state.g + 1)
                    open_states.put((successor.f, number_of_state, successor,d))
        return False, len(closed_states), d

