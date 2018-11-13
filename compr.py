print(['x' + str(_) for _ in range(15)])

row = '|'.join([' {} ' for _ in range(5)])
line = '\n' + '+'.join(['---' for _ in range(5)]) + '\n'

board_layout = line.join(row for _ in range(5))

print(row)
print(line)

print(board_layout)