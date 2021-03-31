from mario_map.mario_board.board_validations import BoardValidations
from mario_map.board_space.pipeline import Pipeline
from mario_map.board_space.free_space import FreeSpace
from mario_map.mario_agent.settings import Settings
from mario_map.mario_agent.agent import Agent
from mario_map.board_space.mario import Mario
import queue


class BoardDistanceFinder:
    settings = Settings()
    agent = Agent(settings)

    @staticmethod
    def select_next_step(board, boar_dimensions, successors_positions, state_position):
        state = board[state_position.row][state_position.col]
        for successor_position in successors_positions:
            if not BoardValidations.is_a_valid_space(successor_position, boar_dimensions):
                continue
            successor = board[successor_position.row][successor_position.col]
            if isinstance(successor, Mario):
                continue
            if isinstance(successor, Pipeline) or (
                    isinstance(successor, FreeSpace) and state.distance == successor.distance + 1):
                successor.color = "#2ECC71"
                return successor_position
        return None

    @staticmethod
    def select_initial_step(board, boar_dimensions, successors_positions):
        best_option = None
        for successor_position in successors_positions:
            if not BoardValidations.is_a_valid_space(successor_position, boar_dimensions):
                continue
            successor = board[successor_position.row][successor_position.col]
            if isinstance(successor, Pipeline):
                successor.color = "#2ECC71"
                return successor_position
            if isinstance(successor, FreeSpace) and successor.distance != 0:
                if best_option is None:
                    best_option = [successor_position, successor]
                elif successor.distance < best_option[1].distance:
                    best_option = [successor_position, successor]
        if best_option is None:
            return None
        best_option[1].color = "#2ECC71"
        return best_option[0]

    @staticmethod
    def find_shortest_path(board, mario_position, boar_dimensions):
        shortest_path = []
        actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN,
                   BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
        posible_steps = BoardDistanceFinder.agent.transition_function(mario_position, actions)
        initial_step_position = BoardDistanceFinder.select_initial_step(board, boar_dimensions, posible_steps)
        if initial_step_position is None:
            board[mario_position.row][mario_position.col].color = "red"
            return shortest_path
        board[mario_position.row][mario_position.col].color = "#2ECC71"
        shortest_path.append(initial_step_position)
        if isinstance(board[initial_step_position.row][initial_step_position.col], Pipeline):
            return shortest_path
        while not isinstance(board[initial_step_position.row][initial_step_position.col], Pipeline):
            actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN,
                       BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
            posible_steps = BoardDistanceFinder.agent.transition_function(initial_step_position, actions)
            next_step_position = BoardDistanceFinder.select_next_step(board, boar_dimensions, posible_steps,
                                                                      initial_step_position)
            if next_step_position is not None:
                shortest_path.append(next_step_position)
                initial_step_position = next_step_position
        return shortest_path

    @staticmethod
    def show_board(board):
        for line in board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    @staticmethod
    def mark_distances(board, boar_dimensions):
        pipelines = []
        total_states = 0
        BoardDistanceFinder.clean_board(board)
        for row in board:
            for element in row:
                if isinstance(element, Pipeline):
                    pipelines.append(element.position)
        total_states = BoardDistanceFinder._mark_distance_in_the_board_bfs(board, pipelines, boar_dimensions)
        return total_states

    @staticmethod
    def clean_board(board):
        for row in board:
            for element in row:
                element.color = "white"
                if isinstance(element, FreeSpace):
                    element.distance = 0

    @staticmethod
    def _discard_successors(board, boar_dimensions, successors_positions, state_position):
        filtered_successors = []
        for successor_position in successors_positions:
            if BoardValidations.is_a_successor(board, state_position, successor_position, boar_dimensions):
                filtered_successors.append(successor_position)
        return filtered_successors

    @staticmethod
    def _mark_successors_distance(board, successors_positions, state_position):
        state = board[state_position.row][state_position.col]
        for successor_position in successors_positions:
            successor = board[successor_position.row][successor_position.col]
            successor.distance = 1 if isinstance(state, Pipeline) else state.distance + 1
            successor.father = state

    @staticmethod
    def _mark_distance_in_the_board_bfs(board, pipelines_positions, boar_dimensions):
        open = queue.SimpleQueue()
        close = []
        for pipeline_position in pipelines_positions:
            open.put(pipeline_position)
        while open.qsize() != 0:
            state_position = open.get()

            actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN,
                       BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
            successors_positions = BoardDistanceFinder.agent.transition_function(state_position, actions)
            successors_positions = BoardDistanceFinder._discard_successors(board, boar_dimensions, successors_positions,
                                                                           state_position)
            BoardDistanceFinder._mark_successors_distance(board, successors_positions, state_position)
            close.append(state_position)
            for successor_position in successors_positions:
                open.put(successor_position)
        return len(close)

    @staticmethod
    def _mark_distance_in_the_board_dfs(board, pipelines_positions, boar_dimensions):
        open = []
        close = []

        for pipeline_position in pipelines_positions:
            open.append(pipeline_position)
        while len(open) != 0:
            state_position = open.pop()
            # mark it as visited
            actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN,
                       BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
            successors_positions = BoardDistanceFinder.agent.transition_function(state_position, actions)
            successors_positions = BoardDistanceFinder._discard_successors(board, boar_dimensions, successors_positions,
                                                                           state_position)
            BoardDistanceFinder._mark_successors_distance(board, successors_positions, state_position)

            close.append(state_position)

            for successor_position in successors_positions:
                open.append(successor_position)
        return len(close)
