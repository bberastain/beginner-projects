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

#class tetris(object):

#    def __init__(self, input_array):
#        self.input_array = input_array


            # my board is a 13x20 array of arrays before adding the bottom
            # that means there are 260 arrays
            # indexed from 0 to 259
            # every 13th array is a new line (first index [12])

            # i have to account for when they try to put something somewhere it can't go
            # like on the border line on either side
            # but to start I'll assume they all are well put


            #I'll start at the bottom, go backwards with the indexes
            #I can use the column to check if anything is in that point at regular distances
            #Then if nothing is immediately above it it also checks on each side of the nothing
            #If there is, it goes up another level and does that again,
            #If there isn't, then it doesn't go up that level and just finishes
