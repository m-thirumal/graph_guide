import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, vertex1, vertex2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, vertex):
        pass

    @abc.abstractmethod
    def get_degree_of_vertex(self, vertex):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, vertex1, vertex2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 >= self.num_vertices or vertex2 >= self.num_vertices or vertex1 < 0 or vertex2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (vertex1, vertex2))
        if weight < 1:
            raise ValueError("Weight must be greater than 1")
        self.matrix[vertex1][vertex2] = weight
        if not self.directed:  # Undirected Graph connected both way
            self.matrix[vertex2][vertex1] = weight

    def check_boundary_conditions(self, vertex):
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)

    def get_adjacent_vertices(self, vertex):
        self.check_boundary_conditions(vertex)
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_degree_of_vertex(self, vertex):
        self.check_boundary_conditions(vertex)
        degree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][vertex] > 0:
                degree = degree + 1
        return degree

    def get_edge_weight(self, vertex1, vertex2):
        return self.matrix[vertex1][vertex2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


g = AdjacencyMatrixGraph(4, directed=True)  # directed can be True / False
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
    print("Degree: ", i, g.get_degree_of_vertex(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge Weight: ", i, " ", j, "Weight: ", g.get_edge_weight(i, j))

g.display()

