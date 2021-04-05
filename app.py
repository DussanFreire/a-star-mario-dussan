from flask import Flask, render_template, request
from mario_map.mario_board.board_manager import BoardManager

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        try:
            if request is None:
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states)
            rows = int(request.form.get("_rows"))
            cols = int(request.form.get("_cols"))
            board_manager.create_new_board(rows, cols)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
        except:
            render_template('home.html')
    return render_template('home.html')


@app.route('/pipeAdded', methods=["GET", "POST"])
def add_pipeline():
    if request.method == "POST":
        try:
            if request is None:
                return load_board()
            pipe_row = int(request.form.get("_pipe_row"))
            pipe_col = int(request.form.get("_pipe_col"))
            board_manager.add_element_and_reload("pipeline", pipe_row, pipe_col)
            return load_board()
        except:
            return load_board()
    return load_board()


@app.route('/wallAdded', methods=["GET", "POST"])
def add_wall():
    if request.method == "POST":
        try:
            if request is None:
                return load_board()
            wall_row = int(request.form.get("_wall_row"))
            wall_col = int(request.form.get("_wall_col"))
            board_manager.add_element_and_reload("wall", wall_row, wall_col)
            return load_board()
        except:
            return load_board()
    return load_board()


@app.route('/marioAdded', methods=["GET", "POST"])
def add_mario():
    if request.method == "POST":
        try:
            if request is None:
                return load_board()
            mario_row = int(request.form.get("_mario_row"))
            mario_col = int(request.form.get("_mario_col"))
            board_manager.add_element_and_reload("mario", mario_row, mario_col)
            return load_board()
        except:
            return load_board()
    return load_board()


@app.route('/easyMap', methods=["GET", "POST"])
def load_easy_map():
    if request.method == "POST":
        board_manager.load_board("easy")
        return load_board()
    return load_board()


@app.route('/medium', methods=["GET", "POST"])
def load_medium_map():
    if request.method == "POST":
        board_manager.load_board("medium")
        return load_board()
    return load_board()


@app.route('/difficult', methods=["GET", "POST"])
def load_difficult_map():
    if request.method == "POST":
        board_manager.load_board("difficult")
        return load_board()
    return load_board()


@app.route('/rect_line_h', methods=["GET", "POST"])
def use_rect_line_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("rect_line_h")
        return load_board()
    return load_board()


@app.route('/near_borders_h', methods=["GET", "POST"])
def use_near_borders_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("near_borders_h")
        return load_board()
    return load_board()


@app.route('/radar_h', methods=["GET", "POST"])
def use_radar_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("radar_h")
        return load_board()
    return load_board()


@app.route('/bfs', methods=["GET", "POST"])
def use_bfs():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("bfs")
        return load_board()
    return load_board()


def load_board():
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep,
                           Branch_Factor=board_manager.branch_factor)


if __name__ == "__main__":
    board_manager = BoardManager()
    app.run(debug=True)
