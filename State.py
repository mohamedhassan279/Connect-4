"""
************* State Representation *************
each column is represented using 9 bits
---> 6 bits for the cells in the col + 3 bits to tell number of occupied cells
7 cols * 9 bits = 63 bits
---> state is represented using 64 bits --> the 64th bit is not used
if cell is occupied --> 0 means player 1, 1 means player 2
col 0 --> bit 0 to bit 8  [from bit 6 to bit 8 --> number of occupied cells]
col 1 --> bit 9 to bit 17 [from bit 15 to bit 17 --> number of occupied cells]
.
.
col 6 --> bit 54 to bit 62 [from bit 60 to bit 62 --> number of occupied cells]
"""
from copy import deepcopy

col_mask = [511, 261632, 133955584, 68585259008, 35115652612096, 17979214137393152, 9205357638345293824]


class State:

    def __init__(self):
        self.state = 0
        self.moves = 0

    """
    Convert the state to 2d board
    board: rows = 6, cols = 7
    board[i][j] = 0 if empty, 1 if player 1, 2 if player 2
    board[0][0] is the bottom left corner in the game
    increasing i moves up in the board
    increasing j moves right in the board
    """
    def convert_to_board(self):
        board = [[0 for _ in range(7)] for _ in range(6)]
        for j in range(7):
            col_list = self.get_col_list(j)
            for i in range(6):
                board[i][j] = col_list[i]
        return board

    # get the successors of the current state
    def get_successors(self):
        successors = []
        for j in range(7):
            col_rep = self.get_col(j)
            occupied = self.get_occupied(col_rep)
            if occupied < 6:  # can drop a chip
                successor = deepcopy(self)
                successor.drop_chip(j, col_rep, occupied)
                successors.append(successor)
        return successors

    def get_col(self, col_number):  # return the 9 bits of this column
        return (self.state & self.get_col_mask(col_number)) >> (9 * col_number)

    def get_occupied(self, col_rep):  # number of occupied cells in the col
        return (col_rep & 448) >> 6

    def get_col_list(self, col_number):  # returns a list representation of the col
        col_rep = self.get_col(col_number)
        occupied = self.get_occupied(col_rep)
        col = []
        for i in range(6):
            if i < occupied:
                row_bit = col_rep & (1 << i)
                if row_bit == 0:
                    col.append(1)
                else:
                    col.append(2)
            else:
                col.append(0)
        return col

    def drop_chip(self, col_number, col_rep, occupied):
        turn = self.get_cur_turn()
        col_rep |= (turn << occupied)
        occupied += 1
        pw = 2
        while pw >= 0:
            exp = 1 << pw
            if occupied >= exp:
                col_rep |= (1 << (6 + pw))
                occupied -= exp
            else:
                col_rep &= ~(1 << (6 + pw))
            pw -= 1
        self.state &= (((1 << 64) - 1) ^ self.get_col_mask(col_number))
        self.state |= (col_rep << (9 * col_number))
        self.moves += 1

    """
    return the current player turn
    0 --> player 1 turn
    1 --> player 2 turn
    """
    def get_cur_turn(self):
        return self.moves & 1  # if odd --> player 2 turn --> return 1

    def get_col_mask(self, col_number):  # helping function
        return col_mask[col_number]
