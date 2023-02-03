

from problem import Problem
from path import Path
from queue import Queue


class BFS(Problem):


    def __init__(self, graph) -> None:
        super().__init__(graph)
        self.marked = [False for i in range(len(self.graph)**2)]
        self.path = Path(self.actual)
        
 


    def actions(self, s, a):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """

        if a == 'u':
            # up
            try:
                if self.graph[s[0]+1][s[1]] != 0:
                    return self.graph[s[0]+1][s[1]]
            except Exception:
                pass


        if a == 'r':
            # right
            try:
                if self.graph[s[0]][s[1]+1] != 0:
                    return self.graph[s[0]][s[1]+1]
            except Exception:
                pass



        if a == 'd':
            # down
            try:
                if self.graph[s[0]-1][s[1]] != 0:
                    return self.graph[s[0]-1][s[1]]
            except Exception:
                pass
            


        if a == 'l':
            # left
            try:
                if self.graph[s[0]][s[1]-1] != 0:
                    return self.graph[s[0]][s[1]-1]
            except Exception:
                pass

            


    def result(self, s):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """

        r = []

        # up
        try:
            if self.graph[s[0]+1][s[1]] != 0:
                r.append(self.graph[s[0]+1][s[1]])
        except Exception:
            pass
        
        # down
        try:
            if self.graph[s[0]-1][s[1]] != 0:
                r.append(self.graph[s[0]-1][s[1]])
        except Exception:
            pass

        # left
        try:
            if self.graph[s[0]][s[1]-1] != 0:
                r.append(self.graph[s[0]][s[1]-1])
        except Exception:
            pass

        # right
        try:
            if self.graph[s[0]][s[1]+1] != 0:
                r.append(self.graph[s[0]][s[1]+1])
        except Exception:
            pass

        return r
    


    def goal_test(self, s):
        return super().goal_test(s)


    
    def step_cost(self, s, a, s1):
        return super().step_cost(s, a, s1)

    

    def path_cost(self, ss: list):
        return super().path_cost(ss)
    


    def visit(self, v):
        self.path.add_step(v)



    def bfs(self):
        queue = [self.actual]
        while len(queue) > 0:
            v = queue.pop(0)
            if not self.marked[v]: 
                self.visit(v)
                self.marked[v] = True
                for w in self.result(v):
                    if not self.marked[w]:
                        queue.append(w)





    def __repr__(self) -> str:
        r = ""
        for i in self.graph:
            r = r + str(i) + "\n"
        return r



    def remove_choice():
        return Path()





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




def criteria(list:list):
    pass



def is_explored(path,result,explored):
    pass




