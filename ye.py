def result(self, s):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """

        r = []

        """
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

        """
        
        return r







def result(self, s):
        """
        hay 4 tipos de movimientos:
        up ⬆️
        right ➡️
        down ⬇️
        left ⬅️
        """
        # x = s[0]
        # y = s[1]

        # dirs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # return [(x, y) for x, y in dirs if self.is_valid(s) and self.graph[x][y] == self.graph[self.actual[0]][self.actual[1]]]

"""


def actions(a):
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

"""