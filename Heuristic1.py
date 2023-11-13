from Heuristic import Heuristic


class Heuristic1(Heuristic):
    def get_score(self, current_state):
        pass

    def row_score(self, board: list):
        score: int = 0
        for i in range(6):  # iterate over each row
            j = 0
            space_before = 0
            while j < 7:
                while j < 7 and board[i][j] == 0:  # count spaces before group
                    space_before += 1
                    j += 1
                if j == 7:  # all row is empty --> break the current row
                    break

                # count the consecutive chips
                player = board[i][j]
                start_j = j
                first_group = 0
                while j < 7 and board[i][j] == player:
                    first_group += 1
                    j += 1
                if j == 7 or board[i][j] != 0:  # the row ends, or we found the opponent in the way --> stop
                    score += self.solve_row_group(player, start_j, space_before, first_group, 0, 0)
                    continue

                # case of: some empty cells + consecutive group + some empty cells
                space_between = 0
                while j < 7 and board[i][j] == 0:  # count spaces after first_group
                    space_between += 1
                    j += 1
                if space_between > 1 or j == 7 or board[i][j] != player:  # case of space(s) + group + 2 or more spaces
                    score += self.solve_row_group(player, start_j, space_before, first_group, space_between, 0)
                    continue
                second_group = 0
                while j < 7 and board[i][j] == player:  # count the second group of consecutive chips
                    second_group += 1
                    j += 1
                if first_group == 1 and second_group == 1:  # in case space + 1 chip + 1 space + 1 chip
                    score += self.get_score_sign(player) * self.solve_single_chip(start_j, space_before + space_between)
                    j -= 1
                    space_before = space_between
                    continue
                else:
                    score += self.solve_row_group(player, start_j, space_before,
                                                  first_group, space_between, second_group)
        return score

    def solve_row_group(self, player, j, space_before, first_group, space_between, second_group):
        pass

    def solve_single_chip(self, j, spaces):
        pass

    def solve_two_chips(self, spaces):
        pass

    def solve_three_chips(self, space_before, first_group, spce_between, second_group):
        pass

    def solve_four_or_more_chips(self, space_before, first_group, spce_between, second_group):
        pass

    def get_score_sign(self, player):
        if player == 1:
            return -1
        return 1
