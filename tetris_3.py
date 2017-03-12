# in this attempt I start at the top and check for white space below
# more logical than indexing backwards
# also, don't delete squares until the end, keeps a constant total index
# instead, place fillers until all pieces are placed

# works for pieces H, B, and L
# doesn't work for Z and S yet

# filler arrays
l = ['|']    # border line
ws = [' ']   # white space
b = ['-']    # bottom
nl = ['\n']  # new line
dl = ['d']   # delete later

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
    array = []
    for row in range(1, 21):
        array.append(l)
        for i in range(1, 11):
            array.append(ws)
        array.append(l)
        array.append(nl)
    for i in range(1, 13):
        array.append(b)
    # array length is 272
    return array


def board_to_string(array):
    # delete dl arrays
    while dl in array:
        del array[array.index(dl)]

    # concatenate arrays into a string
    string = ''
    for i in array:
        for j in i:
            string += j
    return string


def update_board_with_piece(array, entry):
    piece_array = PIECES[entry['piece']]
    column = entry['column']
    al = len(piece_array)  # array length
    # takes part of a piece individually, not good for Z and S
    while al >= 1:
        part = piece_array[al - 1]  # start at the last/bottom part
        for string in part:
            pl = len(string)
        row = 0
        while row < 21:
            if all(array[row * 13 + column + space] is ws
                   for space in range(0, pl)):
                # if all spaces below the piece are blank, return true
                row += 1
            else:
                array[(row-1)*13 + column] = part
                for fill in range(1, pl):
                    array[(row-1)*13 + column + fill] = dl
                break
        al -= 1


def tetris(pieces_to_drop):
    # create a blank board
    array = create_board()

    # replace blank arrays with pieces
    for entry in pieces_to_drop:
        update_board_with_piece(array, entry)

    return board_to_string(array)


print(tetris([{'piece': 4, 'column': 4},
              {'piece': 3, 'column': 5},
              {'piece': 0, 'column': 1}]))
# nice
print(tetris([{'piece': 4, 'column': 4},
              {'piece': 3, 'column': 5},
              {'piece': 2, 'column': 2}]))
# dang
