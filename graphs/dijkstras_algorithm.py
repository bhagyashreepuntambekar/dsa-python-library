import heapq
class Solution:
    def dijkstras_algorithm(self,numVertices,edges,src):
        adj_list = [[] for _ in range(numVertices)]
        dist = [float('inf')] * numVertices
        dist[src] = 0
        min_heap = [(0, src)]

        for u,v,w in edges:
            adj_list[u].append((v,w))

        while min_heap:
            curr_dist,u = heapq.heappop(min_heap)
            if curr_dist > dist[u]:
                continue
            for v,w in adj_list[u]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] =new_dist
                    heapq.heappush(min_heap,(new_dist,v))
        return dist

def main():
    numVertices = 5
    edges = [
        [0, 1, 2],
        [0, 2, 4],
        [1, 2, 1],
        [1, 3, 7],
        [2, 4, 3],
        [3, 4, 1]
    ]
    src = 0
    sol = Solution()
    result = sol.dijkstras_algorithm(numVertices,edges,src)
    print("Shortest distances from source:", result)

if __name__== "__main__":
    main()