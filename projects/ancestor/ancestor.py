class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage > 0:
            return self.storage.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.storage)

class Graph:
    """
    Represent a graph as a dictionary
    of vertexes mapping labels to edge.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist!")

def earliest_ancestor(ancestors, starting_node):
    pass