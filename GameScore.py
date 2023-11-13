from State import State


def get_game_score(state: State):
    board = state.convert_to_board()
    human_score = __row_score(1, board) + __col_score(1, board) + __diagonal_score(1, board)
    agent_score = __row_score(2, board) + __col_score(2, board) + __diagonal_score(2, board)
    return human_score, agent_score


def __row_score(player, board):
    score = 0
    for i in range(6):
        j = 0
        while j < 4:
            counter = 0
            for k in range(0, 4):
                if board[i][j + k] != player:
                    j = j + k + 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                j += 1
    return score


def __col_score(player, board):
    score = 0
    for j in range(7):
        i = 0
        while i < 3 and board[i][j] != 0:
            counter = 0
            for k in range(0, 4):
                if board[i + k][j] != player:
                    i = i + k + 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                i += 1
        return score


def __diagonal_score(player, board):
    return __lower_main_diagonal(player, board) + __upper_main_diagonal(player, board) + \
        __lower_reversed_diagonal(player, board) + __upper_reversed_diagonal(player, board)


def __lower_main_diagonal(player, board):
    score = 0
    for diagonal in range(3, 6):
        i, j = diagonal, 0
        while i > 2:
            counter = 0
            for k in range(4):
                if board[i - k][j + k] != player:
                    i = i - k - 1
                    j = j + k + 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                i -= 1
                j += 1
    return score


def __upper_main_diagonal(player, board):
    score = 0
    for diagonal in range(0, 3):
        i, j = diagonal, 6
        while i < 3:
            counter = 0
            for k in range(4):
                if board[i + k][j - k] != player:
                    i = i + k + 1
                    j = j - k - 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                i += 1
                j -= 1
    return score


def __upper_reversed_diagonal(player, board):
    score = 0
    for diagonal in range(0, 3):
        i, j = diagonal, 0
        while i < 3:
            counter = 0
            for k in range(4):
                if board[i + k][j + k] != player:
                    i = i + k + 1
                    j = j + k + 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                i += 1
                j += 1
    return score


def __lower_reversed_diagonal(player, board):
    score = 0
    for diagonal in range(3, 6):
        i, j = diagonal, 6
        while i > 2:
            counter = 0
            for k in range(4):
                if board[i - k][j - k] != player:
                    i = i - k - 1
                    j = j - k - 1
                    break
                counter += 1
            if counter == 4:
                score += 1
                i -= 1
                j -= 1
    return score
