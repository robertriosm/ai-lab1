
class Path:
    """
    path para mapear los estados con sus fronteras
    """

    def __init__(self, initial: tuple or None) -> None:
        if initial:
            self.states = [initial]
        else:
            self.states = []
        self.end = 0

    
    def extend_from():
        pass


    def add_step(self, v):
        self.states.append(v)

    