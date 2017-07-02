import sys

# filler arrays
l = ['|'] # border line
ws = [' '] # white space
b = ['-'] # bottom
nl = ['\n'] # new line

# start testing with only [['HHHH']] in PIECES array
PIECES = [[['HHHH']]]

def tetris(d):
    # create a blank board (without the bottom)
    array = []
    for row in range(1,21):
        array.append(l)
        for i in range(1,11):
            array.append(ws)
        array.append(l)
        array.append(nl)

    # replace blank arrays with pieces
    for entry in d:
        piece_array = PIECES[entry['piece']]
        column = entry['column']
        al = len(piece_array) # array length
        while al >= 1: # go through all array components of a tetris piece
            part = piece_array[al-1] # starting at the last/bottom one
            al -= 1
            for string in part:
                pl = len(string) # part length
            fs = column - 13 # first space of piece
            ls = fs + pl - 1 # last space of piece
            for index in array[fs:ls+1]:
                if index == ws:
                    continue
                else:
                    print "Piece doesn't fit"
                    sys.exit(0)
                # instead of quitting, move to row above and try again
                # by making a while loop that will subtract 13
            array.insert(fs, part)
            while pl > 0:
                    pl -= 1
                    array.pop(ls)

    # add the bottom
    for i in range(1,13):
        array.append(b)

    # concatenate arrays into a string
    string = ''
    for i in array:
        for j in i:
            string += j
    return string


# test case
print(tetris([{'piece': 0, 'column':1}]))
print '__________________________________'
print(tetris([{'piece': 0, 'column':4}]))
print '__________________________________'
print(tetris([{'piece': 0, 'column':7}]))
print '__________________________________'
print(tetris([{'piece': 0, 'column':8}]))
