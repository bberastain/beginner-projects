l = ['|']
ws = [' ']
b = ['-']
nl = ['\n']

PIECES = [
  [['HHHH']],
  [['ZZ'],
   [' ZZ']],
  [[' SS'],
   ['SS']],
  [['BB'],
   ['BB']],
  [['L'],
   ['L'],
   ['LL']],
]


def create_board():
    board = []
    for row in range(1, 21):
        board.append(l)
        for i in range(1, 11):
            board.append(ws)
        board.append(l)
        board.append(nl)
    for i in range(1, 13):
        board.append(b)
    return board


def board_to_string(board):
    string = ''
    for i in board:
        for j in i:
            string += j
    return string


def update_board_with_piece(board, entry):
    piece_array = PIECES[entry['piece']]
    al = len(piece_array)
    bottom_row = find_bottom_row(board, entry)
    while al >= 1:
        part = piece_array[al - 1]
        string = part[0]
        pl = len(string)
        col = entry['column']
        string, col, pl = remove_blank(string, col, pl)
        for index in range(0, pl):
            board[bottom_row*13 + col + index] = [string[index]]
        bottom_row -= 1
        al -= 1
    return board


def find_bottom_row(board, entry):
    piece_array = PIECES[entry['piece']]
    al = len(piece_array)
    bottom_row = 0
    while al >= 1:
        part = piece_array[al - 1]  # start at the last/bottom part
        string = part[0]
        pl = len(string)
        col = entry['column']
        row = 0
        string, col, pl = remove_blank(string, col, pl)
        while row < 21:
            if all(board[row * 13 + col + space] is ws
                   for space in range(0, pl)):
                # if all spaces below the piece are blank, return true
                row += 1
            elif bottom_row == 0:
                bottom_row = row-1
                break
            elif bottom_row > row:
                bottom_row = row
                break
            else:
                break
        al -= 1
    return bottom_row


def remove_blank(string, col, pl):
    if string[0] == ' ':
        string = string[1:]
        col += 1
        pl -= 1
    elif string[-1] == ' ':
        string = string[:-1]
        pl -= 1
    else:
        pass
    return string, col, pl


def tetris(pieces_to_drop):
    board = create_board()
    for entry in pieces_to_drop:
        update_board_with_piece(board, entry)
    return board_to_string(board)


print(tetris([{'piece': 4, 'column': 4},
              {'piece': 3, 'column': 5},
              {'piece': 2, 'column': 2}]))
