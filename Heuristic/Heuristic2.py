from Heuristic.Heuristic import Heuristic
from State import  State

weights = [[3, 4, 5, 7, 5, 4, 3], [4, 6, 8, 10, 8, 6, 4], [5, 8, 11, 13, 11, 8, 5], [5, 8, 11, 13, 11, 8, 5],
         [4, 6, 8, 10, 8, 6, 4], [3, 4, 5, 7, 5, 4, 3]]


class Heuristic2(Heuristic):
    def __init__(self):
        print("heuristic 2 created")
        pass

    def get_score(self, current_state: State):
        board = current_state.convert_to_board()
        score: int = 0
        for j in range(7):
            for i in range(6):
                if board[i][j] == 0:  # cell i,j is empty and thus remaining values in column is empty
                    break
                score += self.get_score_sign(board[i][j]) * weights[i][j]
        return score

