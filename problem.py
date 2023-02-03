
from abc import ABC, abstractmethod


class Problem(ABC):
    """
    framework para definir formalmente un problema
    """
    
    def __init__(self, graph) -> None:

        self.graph = graph

        self.goal = []

        for x in range(len(self.graph)):
            for y in range(len(self.graph)):
                if self.graph[x][y] == 2:
                    self.initial = (x,y)
                if self.graph[x][y] == 3:
                    self.goal.append((x,y))
        
        self.actual = self.initial

        
    
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


