class Node:
    def __init__(self):
        self.neighbours = []
        self.visited = False
        self.parent = None

    def add_neighbour(self, index):
        self.neighbours += [index]
