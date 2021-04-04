from mario_map.board_space.pipeline import Pipeline
from mario_map.mario_agent.settings import Settings


class BoardMarker:
    settings = Settings()

    @staticmethod
    def mark_element(state):
        if isinstance(state, Pipeline) or state.mario_is_here:
            state.space_visited(BoardMarker.settings.PATH_COLOR)
        else:
            state.space_visited(BoardMarker.settings.VISITED_COLOR)

    @staticmethod
    def mark_all_paths(board):
        pipelines_found = BoardMarker._get_pipelines_visited(board)
        if not pipelines_found:
            board.mario.color = BoardMarker.settings.MARIO_TRAPPED_COLOR
        for pipe in pipelines_found:
            BoardMarker._mark_one_path(pipe)

    @staticmethod
    def _mark_one_path(pipe):
        while pipe.father is not None:
            pipe.color = BoardMarker.settings.PATH_COLOR
            pipe = pipe.father

    @staticmethod
    def _get_pipelines_visited(board):
        pipelines_found = []
        for row in range(0, board.dimensions.num_rows):
            for col in range(0, board.dimensions.num_cols):
                if isinstance(board.board[row][col], Pipeline) and board.board[row][col].visited:
                    pipelines_found.append(board.board[row][col])
        return pipelines_found
