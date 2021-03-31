class Dimensions:
    def __init__(self, num_rows, num_cols):
        self.num_rows = None
        self.num_cols = None
        self._set_dimensions(num_rows, num_cols)

    def _set_dimensions(self,  num_rows, num_cols):
        if num_rows < 1:
            self.num_rows = 1
        else:
            self.num_rows = num_rows
        if num_cols < 1:
            self.num_cols = 1
        else:
            self.num_cols = num_cols
