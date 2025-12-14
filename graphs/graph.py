from collections import deque


class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0]*vertices for _ in range(self.vertices)]

    def add_edge(self, edge,direction):
        x,y = edge
        if not direction:
            self.graph[x][y] = 1
            self.graph[y][x] = 1
        else:
            self.graph[x][y] = 1

    def get_adj_matrix(self):
        print(self.graph)

    def bfs(self,start=0):
        visited = [False] * self.vertices
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            print(u)
            for v in range(self.vertices):
                if self.graph[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    q.append(v)

    def _dfs(self,u,visited):
        visited[u] = True
        print(u)
        for v in range(self.vertices):
            if self.graph[u][v] ==1 and not visited[v]:
                self._dfs(v,visited)


    def dfs(self,start=0):
        visited = [False] * self.vertices
        self._dfs(start,visited)

    def _cycle_dfs_undirected(self, src, parent, visited):
        visited[src] = True
        for v in range(self.vertices):
            if self.graph[src][v] == 1 and not visited[v]:
                if self._cycle_dfs_undirected(v, src, visited):
                    return True
            elif self.graph[src][v] == 1 and visited[v] and v != parent:
                return True
        return False

    def is_cycle_dfs_undirected(self):
        visited = [False] * self.vertices
        for v in range(self.vertices):
            if not visited[v]:
                if self._cycle_dfs_undirected(v, -1, visited):
                    return True
        return False

    def _cycle_bfs_undirected(self,visited,start=0):
        if self.graph:
            q = deque([(start,-1)])
            visited[start] = True
            while q:
              u,parent = q.popleft()
              for v in range(self.vertices):
                  if self.graph[u][v]==1 and not visited[v]:
                      q.append((v,u))
                      visited[v] = True
                  elif self.graph[u][v]==1 and visited[v]:
                      if v != parent:
                          return True
            return False
        return False

    def is_cycle_bfs_undirected(self):
        visited = [False] * self.vertices

        for start in range(self.vertices):
            if not visited[start]:
                if self._cycle_bfs_undirected(visited, start):
                    return True

        return False

    def is_cycle_dfs_directed(self):
        visited = [False] * self.vertices
        path = [False] * self.vertices
        for v in range(self.vertices):
            if not visited[v]:
                if self._cycle_dfs_directed(v,visited,path):
                    return True
        return False
    def _cycle_dfs_directed(self, u, visited,path):
        visited[u] = True
        path[u] = True
        for v in range(self.vertices):
            if self.graph[u][v] ==1 and not visited[v]:
                if self._cycle_dfs_directed(v,visited,path): return True
            elif self.graph[u][v]==1 and visited[v] and path[v]:
                return True
        path[u]= False
        return False

    def topological_sort(self):
        visited = [False] * self.vertices
        sol = deque()
        for v in range(self.vertices):
            if not visited[v]:
                sol= self.dfs_topological_sort(v,visited,sol)
        result = []
        while sol:
            result.append(sol.pop())
        return result

    def dfs_topological_sort(self,u,visited,sol):
        visited[u] = True
        for v in range(self.vertices):
            if self.graph[u][v]==1 and not visited[v]:
                self.dfs_topological_sort(v,visited,sol)
        sol.append(u)
        return sol



if __name__ == "__main__":
    # creating an undirected graph
    # graph = Graph(5)
    # graph.add_edge((0, 1),False)
    # graph.add_edge((1, 2),False)
    # graph.add_edge((0, 2),False)
    # graph.add_edge((3, 4),False)
    # graph.add_edge((0, 3),False)

    # graph.get_adj_matrix()
    # graph.bfs()
    # graph.dfs()
    # print(graph.is_cycle_dfs_undirected())
    # print(graph.is_cycle_bfs_undirected())

    # creating a directed graph
    # graph = Graph(4)
    # graph.add_edge((1,0),True)
    # graph.add_edge((3,0),True)
    # graph.add_edge((0,2),True)
    # graph.add_edge((2,3),True)
    # print(graph.is_cycle_dfs_directed())

    graph = Graph(6)
    graph.add_edge((5,0),True)
    graph.add_edge((5,2),True)
    graph.add_edge((2,3),True)
    graph.add_edge((3,1),True)
    graph.add_edge((4,1),True)
    graph.add_edge((4,0),True)
    print(graph.topological_sort())

