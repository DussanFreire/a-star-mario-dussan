from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
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
    def a_star(board, heuristic_function):
        open_states = queue.PriorityQueue()
        closed_states = []
        board.mario.set_costs(0, 0)
        number_of_state = 1
        open_states.put((0, number_of_state, board.mario))
        while open_states.qsize() != 0:
            f, _, state = open_states.get()
            closed_states.append(state)
            if isinstance(state, Pipeline):  # goal_state(state):
                return True, len(closed_states)
            PipelineFinder._mark_element(state)
            # PipelineFinder.show_board(board.board)
            actions = [PipelineFinder.settings.UP, PipelineFinder.settings.DOWN,
                       PipelineFinder.settings.LEFT, PipelineFinder.settings.RIGHT]
            # se agregara la option de ver a lo lejos
            successors_pos = PipelineFinder.agent.transition_function_in_order_to_actions(state, actions)
            for successor_pos in successors_pos:
                if not BoardValidations.is_in_the_board(successor_pos, board.dimensions):
                    continue
                successor = board.get_board_element(successor_pos)
                successor.position = successor_pos
                if successor in closed_states:
                    continue
                if isinstance(successor, Wall):
                    continue
                if not BoardValidations.is_a_valid_child(state, successor):
                    continue
                if successor.visited:
                    continue
                successor.father = state
                if isinstance(successor, Pipeline):
                    number_of_state += 1
                    open_states.put((0, number_of_state, successor))
                    successor.space_visited(PipelineFinder.settings.VISITED_COLOR)
                    break
                else:
                    successor.set_costs(heuristic_function(successor, state, board), state.g + 1)
                    successor.space_visited(PipelineFinder.settings.VISITED_COLOR, successor.f)
                    number_of_state += 1
                    open_states.put((successor.f, number_of_state, successor))

                # if successor in open_states:
                #     if successor.g >= state.g in open_states:
                #         continue

        return False, len(closed_states)

    @staticmethod
    def _mark_element(state):
        if state.mario_is_here:
            state.space_visited(PipelineFinder.settings.PATH_COLOR)
        else:
            state.space_visited(PipelineFinder.settings.VISITED_COLOR, state.f)

    @staticmethod
    def mark_all_paths(board):
        pipelines_found = PipelineFinder._get_pipelines_visited(board)
        if not pipelines_found:
            board.mario.color = PipelineFinder.settings.MARIO_TRAPPED_COLOR
        for pipe in pipelines_found:
            PipelineFinder._mark_one_path(pipe)

    @staticmethod
    def _mark_one_path(pipe):
        while pipe.father is not None:
            pipe.color = PipelineFinder.settings.PATH_COLOR
            pipe = pipe.father

    @staticmethod
    def _get_pipelines_visited(board):
        pipelines_found = []
        for row in range(0, board.dimensions.num_rows):
            for col in range(0, board.dimensions.num_cols):
                if isinstance(board.board[row][col], Pipeline) and board.board[row][col].visited:
                    pipelines_found.append(board.board[row][col])
        return pipelines_found

# hacer un debug mostrando el mapa
