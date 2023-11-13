from abc import ABC, abstractmethod


class Heuristic(ABC):

    @abstractmethod
    def get_score(self, current_state):
        pass
