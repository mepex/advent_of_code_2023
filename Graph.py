import pprint
from collections import defaultdict
from heapq import heapify, heappop, heappush


class Graph(object):
    """ Graph data structure, undirected by default. """
    """ Implemented as adjacency matrix- each node has a list with all the nodes it's connected to"""
    _nodes = set()
    _adjacency_matrix = None
    _has_hamilton_cycle = False

    def __init__(self, connections={}, directed=False, weighted=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._weighted = weighted
        self.add_connections(connections)

    @property
    def weighted(self):
        return self._weighted

    @weighted.setter
    def weighted(self, value):
        self._weighted = value

    @property
    def directed(self):
        return self._directed

    @directed.setter
    def directed(self, value):

        self._directed = value

    @property
    def nodes(self):
        """I'm the 'x' property."""
        return self._nodes

    @property
    def adjacency_matrix(self):
        """I'm the 'x' property."""
        if not self._adjacency_matrix:
            self.make_adjacency_matrix()
        return self._adjacency_matrix

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for c in connections:
            if self._weighted:
                self.add(c[0], c[1], c[2])
            else:
                self.add(c[0], c[1])

    def add(self, node1, node2, weight=0):
        """ Add connection between node1 and node2 """
        self._nodes.add(node1)
        self._nodes.add(node2)
        if not isinstance(self._graph[node1], dict):
            self._graph[node1] = {}
        self._graph[node1][node2] = weight
        if not self._directed:
            if not isinstance(self._graph[node2], dict):
                self._graph[node2] = {}
            self._graph[node2][node1] = weight

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def get_connections(self, node1):
        return list(self._graph[node1])

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def countPaths(self, s, d):

        # Mark all the vertices
        # as not visited
        visited = {}
        pathCount = {}
        for k in self._nodes:
            visited[k] = False
            pathCount[k] = 0
        # Call the recursive helper
        # function to print all paths
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[d]

    # A recursive function to print all paths
    # from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]
    # stores actual vertices and path_index
    # is current index in path[]
    def countPathsUtil(self, u, d,
                       visited, pathCount):
        visited[u] = True

        # If current vertex is same as
        # destination, then increment count
        if u == d:
            pathCount[u] += 1

        # If current vertex is not destination
        else:

            # Recur for all the vertices
            # adjacent to current vertex
            for i in self._graph[u]:
                if not visited[i]:
                    self.countPathsUtil(i, d, visited, pathCount)

        visited[u] = False

    def shortest_distances(self, source: str):
        # from https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self._graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(
                pq
            )  # Get the node with the min distance

            if current_node in visited:
                continue  # Skip already visited nodes
            visited.add(current_node)  # Else, add the node to visited set
            for neighbor, weight in self._graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

        predecessors = {node: None for node in self._graph}

        for node, distance in distances.items():
            for neighbor, weight in self._graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors

    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path

    def get_path_weight(self, path):
        w = 0
        for i in range(len(path) - 1):
            w += self._graph[path[i]][path[i+1]]
        return w

    def get_hamiltonian_paths(self, start_v):
        # a hamiltonian path is a path that visits every node exactly once
        size = len(self._nodes)
        # if None we are -unvisiting- comming back and pop v
        to_visit = [None, start_v]
        path = [[]]
        while to_visit:
            v = to_visit.pop()
            if v:
                path[-1].append(v)
                if len(path[-1]) == size:
                    path.append(path[-1].copy())
                for x in set(self._graph[v].keys()) - set(path[-1]):
                    to_visit.append(None)  # out
                    to_visit.append(x)  # in
            else:  # if None we are comming back and pop v
                path[-1].pop()
        path.pop()
        return path

    def make_adjacency_matrix(self):
        self._adjacency_matrix = []
        sn = sorted(self._nodes)
        for i in range(len(sn)):
            n = sn[i]
            self._adjacency_matrix.append([0] * len(sn))
            for j in self._graph[n].keys():
                x = sn.index(j)
                self._adjacency_matrix[i][x] = 1

    def is_safe_to_add(self, v, pos, path):
        # if v is also connected to previous vertex in path, not safe
        if self.adjacency_matrix[path[-1][pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamiltonian_cycle_util(self, path, pos, visited):
        if pos == len(self.nodes):
            if self.adjacency_matrix[path[-1][pos - 1]][path[-1][0]] == 1:
                # found a path, now make a new possible path
                path.append([-1] * len(self.nodes))
                path[-1] = path[-2].copy()
            return

        for v in range(1, len(self.nodes)):
            if self.is_safe_to_add(v, pos, path) and not visited[v]:
                path[-1].append(v)
                visited[v] = True

                self.hamiltonian_cycle_util(path, pos + 1, visited)

                visited[v] = False
                path[-1].pop()


    def get_hamiltonian_cycles(self):
        # A list of paths, will find all paths
        path = [[0]]

        visited = [False] * len(self.nodes)
        visited[0] = True

        self.hamiltonian_cycle_util(path, 1, visited)
        path.pop()
        if len(path) == 0:
            return None

        p2 = []
        for i in range(len(path)):
            p2.append([])
            for j in range(len(path[i])):
                p2[i].append(sorted(self.nodes)[path[i][j]])
            p2[i].append(sorted(self.nodes)[0])
        return p2

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


if __name__ == '__main__':

    #
    #             A
    #            / \
    #           /   \
    #          B --- C
    #           \   /
    #            \ /
    #             D
    # cycles: ABDCA, ACDBA
    pretty_print = pprint.PrettyPrinter()
    G = Graph()
    G.weighted = False
    G.directed = False

    G.add("A", "B")
    G.add("A", "C")
    G.add("B", "C")
    G.add("B", "D")
    G.add("C", "D")

    pretty_print.pprint(G.adjacency_matrix)
    print('Hamiltonian paths:')
    for n in G.nodes:
      pretty_print.pprint(G.get_hamiltonian_paths(n))

    paths = G.get_hamiltonian_cycles()
    print("Hamiltonian cycles:")
    pretty_print.pprint(paths)

    # Add A and its neighbors
    # G.add("A", "B", 3)
    # G.add("A", "C", 3)
    #
    # # Add B and its neighbors
    # G.add("B", "D", 3.5)
    # G.add("B", "E", 2.8)
    #
    # G.add("C", "E", 2.8)
    # G.add("C", "F", 3.5)
    #
    # G.add("E", "D", 3.1)
    #
    # G.add("E", "G", 7)
    #
    # G.add("F", "G", 2.5)
    # G.add("G", "D", 10)
    #
    # distances = G.shortest_distances("B")
    # print(distances, "\n")
    #
    # b2f = G.shortest_path("B", "F")
    # print(f"The shortest distance from B to F is {b2f}")



    #
    # connections = [('0,0', '1,0'), ('0,0', '1,1')]
    # g = Graph(connections, directed=True)
    # size = 20
    # for i in range(1, size):
    #     for j in range(i + 1):
    #         g.add(f"{i},{j}", f"{i + 1},{j}")
    #         g.add(f"{i},{j}", f"{i + 1},{j + 1}")
    #
    # g.add(f"{size * 2 - 1},0", f"{size * 2},0")
    # g.add(f"{size * 2 - 1},1", f"{size * 2},0")
    # for i in range(size * 2 - 1, size, -1):
    #     for j in range(size * 2 - i + 1):
    #         g.add(f"{i - 1},{j}", f"{i},{j}")
    #         g.add(f"{i - 1},{j + 1}", f"{i},{j}")
    #
    # pretty_print = pprint.PrettyPrinter()
    # pretty_print.pprint(g._graph)
    #
    # print(g.countPaths("0,0", f"{size * 2},0"))
