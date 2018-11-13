# Our Game Class

class GameBoard:
    def __init__(self, cols, rows=None):
        if rows is None:
            rows = cols
        self.cols = cols
        self.rows = rows
        self._matrix = [None] * (rows*cols)

    def _convert_to_pos(self, key):
        if isinstance(key, int):
            return key
        if isinstance(key, str):
            c = ord(key[0]) - ord('A')
            r = int(key[1]) - 1
            return r * self.cols + c

    def __str__(self):
        row = '|'.join([' {} ' for _ in range(self.cols)])
        line = '\n' + '+'.join(['---' for _ in range(self.cols)]) + '\n'
        layout = line.join(row for _ in range(self.rows))
        markers = [i or ' ' for i in self._matrix]
        return layout.format(*markers)

    def __setitem__(self, key, value):
        pos = self._convert_to_pos(key)
        self._matrix[pos] = value

    def __getitem__(self, key):
        pos = self._convert_to_pos(key)
        return self._matrix[pos]

