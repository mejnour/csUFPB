import sys
import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False  
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def dijkstra(graph, start, target):
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(),v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)

        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('c = %s n = %s n_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('c = %s n = %s n_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)

def populate_matrix(matrix_size, file_contents):
    matrix = []

    for i in file_contents:
        i.reverse()
        i.append(0)
        i = [int(x) for x in i]
        matrix.append(i)
    matrix.append([0])

    return matrix

def generate_graph(matrix):
    graph = Graph()

    for i in range(len(matrix)):
        graph.add_vertex(i)

    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            graph.add_edge(i, j, matrix[i][j])

    return graph

def build_shortest(vertex, path):
    if vertex.previous:
        path.append(vertex.previous.get_id())
        build_shortest(vertex.previous, path)
    return

if __name__ == '__main__':
    try:
        file = open(sys.argv[1], 'r')
        file_contents = file.read().splitlines()

        matrix_size = int(file_contents[0])
        del file_contents[0]
        file_contents = [x.split() for x in file_contents]

        matrix = populate_matrix(matrix_size, file_contents)
        graph = generate_graph(matrix)

        dijkstra(graph, graph.get_vertex(0), graph.get_vertex(matrix_size - 1))

        target = graph.get_vertex(1)
        path = [target.get_id()]
        build_shortest(target, path)
        print('%s' %(path[::-1]))

    finally:
        pass