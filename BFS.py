

from problem import Problem
from path import Path


class BFS(Problem):


    def actions(self, s, a):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """

        if a == 'up':
            # up
            try:
                if self.graph[s[0]+1][s[1]]:
                    return self.graph[s[0]+1][s[1]]
            except Exception:
                pass


        if a == 'right':
            
            # right
            try:
                if self.graph[s[0]][s[1]+1]:
                    return self.graph[s[0]][s[1]+1]
            except Exception:
                pass



        if a == 'down':
            # down
            try:
                if self.graph[s[0]-1][s[1]]:
                    return self.graph[s[0]-1][s[1]]
            except Exception:
                pass
            


        if a == 'left':
            # left
            try:
                if self.graph[s[0]][s[1]-1]:
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
            if self.graph[s[0]+1][s[1]]:
                r.append(self.graph[s[0]+1][s[1]])
        except Exception:
            pass
        
        # down
        try:
            if self.graph[s[0]-1][s[1]]:
                r.append(self.graph[s[0]-1][s[1]])
        except Exception:
            pass

        # left
        try:
            if self.graph[s[0]][s[1]-1]:
                r.append(self.graph[s[0]][s[1]-1])
        except Exception:
            pass

        # right
        try:
            if self.graph[s[0]][s[1]+1]:
                r.append(self.graph[s[0]][s[1]+1])
        except Exception:
            pass

        
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


