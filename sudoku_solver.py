import math
from time import process_time

# used to time the execution speed
start = process_time()

################################
##   insert your board here   ##
################################
my_board = []
#   requires: 
#     - blank spaces are indicated by 0, other spaces corresponding to natural numbers
#     - length of array and each sub-array are equal, with a perfect square length
#     - if you're using an example board, scroll down to replace my_board with 
#       the desired board when solve() is called

#########################
##   example boards    ##
#########################

# boards for testing
example_board = [[9,2,0,3,0,6,0,0,0],
                 [0,0,1,0,2,4,6,0,0],
                 [5,0,0,0,0,0,0,0,1],
                 [0,4,0,0,0,7,0,0,0],
                 [1,0,3,4,0,2,7,0,6],
                 [0,0,0,1,0,0,0,8,0],
                 [8,0,0,0,0,0,0,0,2],
                 [0,0,7,2,8,0,9,0,0],
                 [0,0,0,6,0,1,0,3,7]]

invalid_board = [[9,2,0,3,0,6,0,4,0],
                 [0,0,1,0,2,4,6,0,0],
                 [5,0,8,0,0,0,0,0,1],
                 [0,4,0,0,0,7,0,0,0],
                 [1,0,3,4,0,2,7,0,6],
                 [0,0,0,1,0,0,0,8,0],
                 [8,0,0,0,0,0,0,0,2],
                 [0,0,7,2,8,0,9,0,0],
                 [0,0,0,6,0,1,0,3,7]]

sixteenbysixteen = [[4,0,1,7,0,0,0,12,0,0,0,6,0,8,15,9],
                    [0,12,16,0,11,0,0,0,9,15,0,0,0,5,2,0],
                    [0,15,14,0,9,0,6,0,16,0,1,8,3,4,0,0],
                    [5,9,3,13,0,8,15,2,0,0,0,0,16,0,7,0],
                    [11,0,0,0,0,0,0,4,0,0,5,16,0,2,14,0],
                    [2,3,0,0,0,13,0,0,0,14,9,1,12,0,6,16],
                    [0,14,7,16,0,0,0,9,0,0,8,0,5,10,0,3],
                    [0,0,0,5,14,0,0,0,0,0,10,11,8,1,4,0],
                    [12,0,0,0,0,0,0,11,1,0,0,0,0,0,10,0],
                    [0,0,0,15,6,10,0,14,11,8,0,13,4,0,0,2],
                    [0,0,0,0,0,0,0,0,2,0,0,9,0,0,0,0],
                    [16,0,0,0,4,1,0,0,6,0,0,15,0,9,0,5],
                    [13,7,0,0,12,0,4,8,0,1,16,14,0,6,3,0],
                    [14,0,0,8,7,0,0,0,0,0,15,3,1,0,0,0],
                    [0,6,0,0,10,14,3,0,7,0,11,4,2,0,16,8],
                    [0,0,4,0,0,11,0,1,8,12,6,2,0,7,0,0]]

fourbyfour = [[0,1,0,2],
              [2,0,0,3],
              [1,0,0,4],
              [0,3,0,1]]

################################################
##   check if it is possible for some number  ##
##       to be in some spot on the board      ##
################################################

# checks if it is possible for num to be in the row
def check_row(board,rown,num):
    return False if (num in board[rown]) else True

# checks if it is possible for num to be in the column
def check_col(board,coln,num):
    for i in range(len(board)):
        if num == board[i][coln]:
            return False
    return True

# checks if it is possible for num to be in the box
def check_box(board,rown,coln,num):
    box_length = int(math.sqrt(len(board)))

    # the row and col values for indexing the box
    box_rindex = math.floor(rown/box_length)*box_length
    box_cindex = math.floor(coln/box_length)*box_length

    for i in range(box_rindex,box_rindex+box_length):
        for j in range(box_cindex,box_cindex+box_length):
            if num == board[i][j]:
                return False
            
    return True

# check if it is possible for num to be in some spot on the board
def check_num(board,rown,coln,num):
    return check_row(board,rown,num) and check_col(board,coln,num) and check_box(board,rown,coln,num)

###################################
##   solving with backtracking   ##
###################################

# supports perfect square dimensions

# finds the nearest empty spot on the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    # in the case that there is no empty spot
    return None

# main function to solve the board
def solve(board):
    # checks if the board is solved
    next_empty = find_empty(board)

    # board is solved
    if not next_empty:
        return board
    # or set rown, coln to be the next empty spot
    else:
        rown, coln = next_empty

    # check numbers in empty spot
    for num in range(1,len(board)+1):
        # if number can be in spot, then replace spot with number
        if check_num(board,rown,coln,num):
            board[rown][coln] = num

            if solve(board):
                return board

            # reset the last empty spot
            else:
                board[rown][coln] = 0
    # invalid
    return False

#####################################################
##   replace my_board with desired example board   ##
#####################################################

print("No Solution") if not solve(my_board) else print(solve(my_board))

end = process_time() - start

print("Solve Time: "+ end)


    


        



