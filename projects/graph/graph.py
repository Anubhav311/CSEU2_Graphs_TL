"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Cannot create edge based on given vertices!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        visited = set()
        qq.enqueue(starting_vertex)
        while qq.size() > 0:
            vertex = qq.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    qq.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()
        qq.enqueue([starting_vertex])
        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def bfs_path(self, starting_vertex_id, target_value):
        # create a queue
        qq = Queue()
        # enqueue a list holding the starting vertex id
        qq.enqueue([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the queue is not empty
        while qq.size > 0:
            # dequeue to the path
            qq.dequeue()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert is not in visited:
                # if vert is equal to target_value
                if vert == target_value
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # enqueue the new path
                    qq.enqueue(new_path)
        # return None
        return None

    def dfs_path(self, starting_vertex_id, target_value):
        # create a stack
        stack = Stack()
        # push a list holding the starting vertex id
        stack.push([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the stack is not empty
        while stack.size > 0:
            # pop to the path
            stack.pop()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert is not in visited:
                # if vert is equal to target_value
                if vert == target_value
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # push the new path
                    stack.push(new_path)
        # return None
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\n', "Starting DFT")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('\n', "Starting BFT")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\n', "Starting DFT_Recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('\n', "Starting BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('\n', "Starting DFS")
    print(graph.dfs(1, 6))