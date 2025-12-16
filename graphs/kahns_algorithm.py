from collections import deque


class Solution:
    def topological_sort(self,numVertices,edges):
        in_degree =[0] * numVertices
        adjacency_list = [[] for _ in range(numVertices)]

        topo_sorted = []
        q = deque()
        for a,b in edges:
            adjacency_list[a].append(b)
            in_degree[b] = in_degree[b]+1

        for i,in_deg in enumerate(in_degree):
            if in_deg ==0:
                q.append(i)
        while q:
            u = q.popleft()
            topo_sorted.append(u)
            for v in adjacency_list[u]:
                in_degree[v] = in_degree[v] -1
                if in_degree[v] == 0:
                    q.append(v)
        if len(topo_sorted) != numVertices:
            return []
        return topo_sorted



def main():
    sol = Solution()
    numVertices = 4
    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3],
        [3,2]

    ]

    result = sol.topological_sort(numVertices,edges)

    if result:
        print("Topological Order:", result)
    else:
        print("Cycle detected. Topological ordering not possible.")

if __name__ == "__main__":
    main()
