from flask import Flask, render_template, request
from mario_map.mario_board.board import Board

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/board', methods=["GET", "POST"])
def board_created():
    if request.method == "POST":
        rows = int(request.form.get("_rows"))
        cols = int(request.form.get("_cols"))
        board.init_board(rows, cols)
        return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)
    return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)


@app.route('/pipeAdded', methods=["GET", "POST"])
def add_pipeline():
    if request.method == "POST":
        pipe_row = int(request.form.get("_pipe_row"))
        pipe_col = int(request.form.get("_pipe_col"))
        board.add_element_and_reload_distances("pipeline", pipe_row, pipe_col)
        return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)
    return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)


@app.route('/wallAdded', methods=["GET", "POST"])
def add_wall():
    if request.method == "POST":
        wall_row = int(request.form.get("_wall_row"))
        wall_col = int(request.form.get("_wall_col"))
        board.add_element_and_reload_distances("wall", wall_row, wall_col)
        return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)
    return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)


@app.route('/marioAdded', methods=["GET", "POST"])
def add_mario():
    if request.method == "POST":
        mario_row = int(request.form.get("_mario_row"))
        mario_col = int(request.form.get("_mario_col"))
        board.add_element_and_reload_distances("mario", mario_row, mario_col)
        return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)
    return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)


@app.route('/defaultMap', methods=["GET", "POST"])
def load_default_map():
    if request.method == "POST":
        board.load_default_board()
        return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)
    return render_template('board.html', Board_sol=board.get_html_board(), Total_states=board.total_states)


if __name__ == "__main__":
    board = Board()
    app.run(debug=True)
