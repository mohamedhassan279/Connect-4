from . import Heuristic
from . import State

array = [[3, 4, 5, 7, 5, 4, 3], [4, 6, 8, 10, 8, 6, 4], [5, 8, 11, 13, 11, 8, 5], [5, 8, 11, 13, 11, 8, 5],
         [4, 6, 8, 10, 8, 6, 4], [3, 4, 5, 7, 5, 4, 3]]


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
    def calcHeuristic(self, player: int, row: int,
                      col: int):  # calculate the heuristic for each cell according to the table shown above
        value: int = array[row][col]
        if player == 1:  # zero sum game
            return -value
        return value
