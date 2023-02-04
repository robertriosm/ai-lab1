

from problem import Problem
from path import Path
# from queue import Queue


class BFS(Problem):


    def __init__(self, graph) -> None:
        super().__init__(graph)
        self.path = Path(self.actual)


    def result(self, s):
        return super().result(s)


    def actions(self, s):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """

        x = s[0]
        y = s[1]

        dirs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


        return [(x, y) for x,y in dirs if self.is_valid((x,y)) and self.graph[x][y] != 0 ]

 

    def is_valid(self, s):
        return s[0] >= 0 and s[1] >= 0 and s[0] < len(self.graph) and s[1] < len(self.graph[0])
    


    def goal_test(self,s):
        for goal in self.goal:
            if goal[0] == s[0] and goal[1] == s[1]:
                return True


    
    def step_cost(self, s, a, s1):
        return super().step_cost(s, a, s1)

    

    def path_cost(self, ss: list):
        return super().path_cost(ss)



    def is_explored(self, l:list,x,y):
        return (x,y) in l



    def bfs(self):
        queue = [self.initial]
        explored = []
        
        while True:
            if len(queue) > 0:    
                x,y = self.remove_choice(queue)
                explored.append((x,y))

                if self.goal_test((x,y)):
                    return self.graph

                self.graph[x][y] = 4 # cuatro es camino
                print(self.graph, "\n\n")

                for i,j in self.actions((x,y)):
                    if not self.is_explored(explored,i,j):
                        queue.append((i,j))
                
            else:
                return False

            # return self.graph



    def __repr__(self) -> str:
        # return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.graph])
        return ''


        

    def remove_choice(self, queue:list):
        return queue.pop(0)

 


"""
def graph_search(problem:Problem):
    frontier = [Path([problem.initial])]
    explored = []

    while True:
        if len(frontier):
            path = criteria(frontier)
            s = path.end
            explored.append(path)

            if problem.goal_test(s):
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)
                
                if not is_explored(path, result, explored):
                    new_path = Path([])
                    new_path.extend_from(path)
                    new_path.add_step(problem.result(s, a))
                    frontier.append(new_path)
        else:
            return False


"""