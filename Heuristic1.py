import math

from Heuristic import Heuristic


class Heuristic1(Heuristic):
    max_score = math.pow(10, 12)

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
                    score += self.solve_group(player, start_j, space_before, first_group, 0, 0)
                    continue

                # case of: some empty cells + consecutive group + some empty cells
                space_between = 0
                while j < 7 and board[i][j] == 0:  # count spaces after first_group
                    space_between += 1
                    j += 1
                if space_between > 1 or j == 7 or board[i][j] != player:  # case of space(s) + group + 2 or more spaces
                    score += self.solve_group(player, start_j, space_before, first_group, space_between, 0)
                    space_before = space_between
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
                    score += self.solve_group(player, start_j, space_before,
                                              first_group, space_between, second_group)
        return score

    def col_score(self, board: list):
        score: int = 0
        for j in range(7):  # iterate over each col
            i = 0
            while i < 6:
                if board[i][j] == 0:
                    break
                player = board[i][j]
                group = 0
                while i < 6 and board[i][j] == player:
                    group += 1
                    i += 1
                if i < 6 and board[i][j] == 0:  # there is space above
                    score += self.solve_group(player, j, 0, group, 6 - i, 0)
                else:  # no space above
                    score += self.solve_group(player, j, 0, group, 0, 0)
        return score

    def solve_group(self, player, j, space_before, first_group, space_between, second_group):
        score: int = 0
        spaces = space_before + space_between
        if first_group == 1 and second_group == 0:  # single chip
            score += self.solve_single_chip(j, spaces)
        elif first_group == 2 and second_group == 0:  # Two chips
            score += self.solve_two_chips(spaces)
        elif first_group + second_group == 3:  # Three chips
            score += self.solve_three_chips(space_before, first_group, space_between)
        else:  # Four or more chips
            score += self.solve_four_or_more_chips(space_before, first_group, space_between, second_group)
        return self.get_score_sign(player) * score

    def solve_single_chip(self, j, spaces):
        if spaces < 3:
            return 0
        if j == 3:
            return 200
        if j == 0 or j == 6:
            return 40
        if j == 1 or j == 5:
            return 70
        return 120

    def solve_two_chips(self, spaces):
        if spaces < 2:
            return 0
        return (spaces - 1) * 10000

    def solve_three_chips(self, space_before, first_group, space_between):
        score: int = 0
        if space_before + space_between < 1:
            return 0
        if first_group == 3 and space_before >= 1 and space_between >= 1:  # this is an unstoppable case
            score += self.max_score
        else:
            score += 900000
        return score

    def solve_four_or_more_chips(self, space_before, first_group, space_between, second_group):
        score: int = 0
        if first_group >= 4 and space_before >= 1 and space_between >= 1:  # this is an unstoppable case
            score += (first_group - 2) * self.max_score
        elif first_group >= 4:
            score += (first_group - 3) * self.max_score
        if second_group >= 4:
            score += (second_group - 3) * self.max_score
        if space_between == 1:  # combine both groups
            new_group = first_group + second_group - 2
            if first_group >= 4:
                new_group -= (first_group - 3)
            if second_group >= 4:
                new_group -= (second_group - 3)
            if new_group > 0:
                score += new_group * 900000
        return score

    def get_score_sign(self, player):
        if player == 1:
            return -1
        return 1
