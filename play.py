from board import GameBoard

g = GameBoard(3)

g[3] = 'X'
g[4] = 'O'


g['A3'] = 'X'
g['C3'] = 'X'
print(g._matrix)
print(g)
