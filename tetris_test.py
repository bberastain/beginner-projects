# what i have so far

#string = '|'
#for i in range(1,100):
#    if i%11 == 0 or i%13 == 0:
#        string += '|'
#    elif i%12 == 0:
#        string += '\n'
#    else:
#        string += ' '

#print string

string = '|' + ' '*10 + '|'
for i in range(1,21):
    print string
print '-'*12

# for i in array_of_dictionaries

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

def tetris(d):
    '''input list of dictionaries with key-value pairs of "piece: " and "column: "'''
    # do i need to set something to evaluate d so it's read as an array of dictionaries?


    # loop through array of dictionaries, each i is one dictionary
    for i in d:
        # retrieve input dictionary values
        # piece_list is a single index of PIECES
        # column is the index of the ??bottom-left?? piece
        piece_list = PIECES[i[piece]]
        column = i[column]
        # my first thought is to add white space by subtracting
        # the size of the pieces from the total
        string = '|' + ' '*(10-len()              + '|'


# another thought would be that I could represent the whole board
# as a 12 by 20 array with a marker for every point in every line
# for example, after isolating the piece with the for loop above


# !!! strings are not mutable, but arrays are
# !!! so make a combination of arrays, concatenate their strings at the end

# first create an array of arrays for the board             <-----FIRST PART

ws = [' '] # white space
left = column - 1 #
right_white_space =
new_line = ['\n']

# Take the L shaped piece
height_of_piece = len(piece_list) # number of arrays in array piece_list
for i in piece_list #will give me each individual list
    for j in i # gives the string
        x = len(j) # gives lenght of string#


# must a




# it's called array, not list.
# what are the commands for making an array a matrix?
# a 2 x 2?
# a tetris piece?



>>> white_space = [' ']
>>> new_line = ['\n']
>>> piece1 = ['ZZ']
>>> piece2 = ['ZZZZ']
>>> piece3 = ['ZZZ']
>>> array = [white_space, white_space, piece1, new_line, piece2, new_line, white_space, piece3]
>>> string = ''
>>> for i in array:
...     for j in i:
...             string+=j
...
>>> string
'  ZZ\nZZZZ\n ZZZ'
>>> print string
  ZZ
ZZZZ
 ZZZ
