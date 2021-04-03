class HtmlGenerator:
    @staticmethod
    def create_html_board(board):
        table = "<head> <table style='background-color:black;'>"
        table += "<tr><td></td>"
        table += HtmlGenerator._get_col_indexes(board)
        table += "</tr>"
        table += HtmlGenerator.get_rows(board)
        table += "</table> </head>"
        return table

    @staticmethod
    def _get_col_indexes(board):
        row = ""
        for col in range(0, board.dimensions.num_cols):
            row += "<td width=20 border=1 style=' border-color: black;color: white; background-color: " \
                     "black;text-align:center;'>" + str(col + 1) + "</td>"
        return row

    @staticmethod
    def get_rows(board):
        table = ""
        for row in range(0, board.dimensions.num_rows):
            table += "<tr>"
            table += "<td width=20 border=1 style='border-color: black;color: white; background-color: " \
                     "black;text-align:center;'>" + str(row + 1) + "</td>"
            for col in range(0, board.dimensions.num_cols):
                value = board.board[row][col].display_value
                table += "<td width=20 border=1 style='border-color: black;color: black; background-color: " + \
                         board.board[row][col].color + ";text-align:center;'>" + str(value) + "</td>"
            table += "</tr>"
        return table
