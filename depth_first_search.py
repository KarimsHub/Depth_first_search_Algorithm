from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v): # want to add the edge from u to v
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.graph[v].remove(u) # want the nodes without executing edge in our list as well
    
    def use(self, v):
        print(v)
    
    def _depth_first_search(self, v, visited): # we need the node and the visited array
        visited[v] = True
        self.use(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self._depth_first_search(i, visited) #recursion
    
    def depth_first_search(self, start):
        visited = [False] * len(self.graph)
        print(self.graph)
        self._depth_first_search(start, visited)

g = Graph()
g.add_edge(0,2) # edge from 0 to 2
g.add_edge(0,4)
g.add_edge(2,4)
g.add_edge(1,3)
g.add_edge(4,1)
g.add_edge(4,0)
g.add_edge(4,2)

print('Starting depth first search')
g.depth_first_search(0)