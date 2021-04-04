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
                                       Total_states=board_manager.total_states)
            pipe_row = int(request.form.get("_pipe_row"))
            pipe_col = int(request.form.get("_pipe_col"))
            board_manager.add_element_and_reload("pipeline", pipe_row, pipe_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


@app.route('/wallAdded', methods=["GET", "POST"])
def add_wall():
    if request.method == "POST":
        try:
            if request is None:
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states)
            wall_row = int(request.form.get("_wall_row"))
            wall_col = int(request.form.get("_wall_col"))
            board_manager.add_element_and_reload("wall", wall_row, wall_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


@app.route('/marioAdded', methods=["GET", "POST"])
def add_mario():
    if request.method == "POST":
        try:
            if request is None:
                return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                       Total_states=board_manager.total_states)
            mario_row = int(request.form.get("_mario_row"))
            mario_col = int(request.form.get("_mario_col"))
            board_manager.add_element_and_reload("mario", mario_row, mario_col)
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
        except:
            return render_template('board.html', Board_sol=board_manager.get_html_board(),
                                   Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


@app.route('/easyMap', methods=["GET", "POST"])
def load_easy_map():
    if request.method == "POST":
        board_manager.load_board("easy")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


@app.route('/medium', methods=["GET", "POST"])
def load_medium_map():
    if request.method == "POST":
        board_manager.load_board("medium")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


@app.route('/difficult', methods=["GET", "POST"])
def load_difficult_map():
    if request.method == "POST":
        board_manager.load_board("difficult")
        return render_template('board.html', Board_sol=board_manager.get_html_board(),
                               Total_states=board_manager.total_states)
    return render_template('board.html', Board_sol=board_manager.get_html_board(),
                           Total_states=board_manager.total_states)


if __name__ == "__main__":
    board_manager = BoardManager()
    app.run(debug=True)
