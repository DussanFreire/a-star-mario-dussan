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
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
            pipe_row = int(request.form.get("_pipe_row"))
            pipe_col = int(request.form.get("_pipe_col"))
            board_manager.add_element_and_reload("pipeline", pipe_row, pipe_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/wallAdded', methods=["GET", "POST"])
def add_wall():
    if request.method == "POST":
        try:
            if request is None:
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
            wall_row = int(request.form.get("_wall_row"))
            wall_col = int(request.form.get("_wall_col"))
            board_manager.add_element_and_reload("wall", wall_row, wall_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/marioAdded', methods=["GET", "POST"])
def add_mario():
    if request.method == "POST":
        try:
            if request is None:
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
            mario_row = int(request.form.get("_mario_row"))
            mario_col = int(request.form.get("_mario_col"))
            board_manager.add_element_and_reload("mario", mario_row, mario_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/easyMap', methods=["GET", "POST"])
def load_easy_map():
    if request.method == "POST":
        board_manager.load_board("easy")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/medium', methods=["GET", "POST"])
def load_medium_map():
    if request.method == "POST":
        board_manager.load_board("medium")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/difficult', methods=["GET", "POST"])
def load_difficult_map():
    if request.method == "POST":
        board_manager.load_board("difficult")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/rect_line_h', methods=["GET", "POST"])
def use_rect_line_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("rect_line_h")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/near_borders_h', methods=["GET", "POST"])
def use_near_borders_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("near_borders_h")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/radar_h', methods=["GET", "POST"])
def use_radar_heuristic():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("radar_h")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


@app.route('/bfs', methods=["GET", "POST"])
def use_bfs():
    if request.method == "POST":
        board_manager.change_pipe_finder_method("bfs")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states, Time=board_manager.time, Deep=board_manager.deep, Branch_Factor=board_manager.branch_factor)


if __name__ == "__main__":
    board_manager = BoardManager()
    app.run(debug=True)
