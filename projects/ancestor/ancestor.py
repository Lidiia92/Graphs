
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("VERTEX ALREADY EXISTS")



    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print("VERTEX DOES NOT EXIST")
        else:
            #Setting direction from v1 to v2
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)


#ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        #Child --> Parent edges

        graph.add_edge(pair[1], pair[0])

    queue = Queue()
    queue.enqueue([starting_node])

    path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        shortest_path = queue.dequeue()
        vertex = shortest_path[-1]

        if len(shortest_path) > path_length or (len(shortest_path) == path_length and vertex < earliest_ancestor):

            earliest_ancestor = vertex
            path_length = len(shortest_path)

        
        for neighbor in graph.vertices[vertex]:
            shortest_path_copy = list(shortest_path)
            shortest_path_copy.append(neighbor)
            queue.enqueue(shortest_path_copy)

    return earliest_ancestor