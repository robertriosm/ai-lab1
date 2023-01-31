
from abc import ABC, abstractmethod


class Problem(ABC):
    """
    framework para definir formalmente un problema
    """
    
    def __init__(self, graph) -> None:

        self.graph = graph

        self.goal = []

        for x in self.graph:
            for y in x:
                if y == 2:
                    self.initial = (x,y)
                if y == 3:
                    self.goal.append((x,y))
        
        self.actual = set(self.initial)

        
    
    @abstractmethod
    def actions(self, s):
        pass


    @abstractmethod
    def result(self, s):
        pass


    @abstractmethod
    def goal_test(self, s):
        return s == self.goal


    @abstractmethod
    def step_cost(self, s, a, s1):
        pass


    @abstractmethod
    def path_cost(self, ss: list):
        pass


