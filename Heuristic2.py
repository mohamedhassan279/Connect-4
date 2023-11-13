from . import Heuristic
from . import State


class Heuristic2(Heuristic):
    def __int__(self):
        pass

    def get_score(self, currentState: State):
        board = currentState.getBoard()
        score: int = 0
        for j in range(7):
            for i in range(6):
                if board[i][j] == 0:  # cell i,j is empty and thus remaning values in column is empty
                    break
                score += self.__calcHeuristic(board[i][j], i, j)
        return score

    # i j|0  1  2  3  4  5  6
    # 0|  3  4  5  7  5  4  3
    # 1|  4  6  8 10  8  6  4
    # 2|  5  8 11 13 11  8  5
    # 3|  5  8 11 13 11  8  5
    # 4|  4  6  8 10  8  6  4
    # 5|  3  4  5  7  5  4  3
    def calcHeuristic(self, player: int, row: int, col: int): #calculate the heuristic for each cell according to the table shown above
        value: int
        if col == 0 or col == 6:
            if row == 0 or row == 5:
                value = 3
            elif row == 1 or row == 4:
                value = 4
            else:
                value = 5
        elif col == 1 or col == 5:
            if row == 0 or row == 5:
                value = 4
            elif row == 1 or row == 4:
                value = 6
            else:
                value = 8
        elif col == 2 or col == 4:
            if row == 0 or row == 5:
                value = 5
            elif row == 1 or row == 4:
                value = 8
            else:
                value = 11
        else:
            if row == 0 or row == 5:
                value = 7
            elif row == 1 or row == 4:
                value = 10
            else:
                value = 13
        if player == 1:  # zero sum game
            return -value
        return value
