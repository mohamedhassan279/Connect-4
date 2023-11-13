from abc import ABC, abstractmethod


class Heuristic(ABC):

    def get_score_sign(self, player):
        if player == 1:  # if it's the human player then we return negative one (human is player 1)
            return -1
        return 1  # if it's our AI agent then we return one because we want our agent to win

    @abstractmethod
    def get_score(self, current_state):
        pass
