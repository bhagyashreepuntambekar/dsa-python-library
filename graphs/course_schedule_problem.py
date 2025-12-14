from collections import deque



class Solution:
    def find_order(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
                Return one valid order to complete all courses.

                Args:
                    numCourses (int)
                    prerequisites (List[List[int]])

                Returns:
                    List[int]: A valid ordering if possible, otherwise an empty list.
                """
        adj_list = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)

        visited = [False] * numCourses
        path = [False] * numCourses
        solution = deque()
        result = []
        for v in range(numCourses):
            if not visited[v]:
                is_cycle,solution = self._dfs(v,path,visited,adj_list,solution)
                if is_cycle:
                    return []
        while solution:
            result.append(solution.pop())
        return result

    def _dfs(self,u,path,visited,adj_list,solution):
        visited[u] = True
        path[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                if self._dfs(v,path,visited,adj_list,solution):return True,[]
            elif path[v]:
                return True,[]
        path[u] = False
        solution.append(u)
        return False,solution

def main():
    sol = Solution()

    # Sample Input
    # numCourses = 7
    # prerequisites = [
    #     [1, 0],
    #     [2, 0],
    #     [3, 1],
    #     [4, 1],
    #     [5, 2],
    #     [6, 3],
    #     [6, 4]
    # ]

    numCourses = 4
    prerequisites = [
        [1, 0],  # 0 → 1
        [2, 1],  # 1 → 2
        [3, 2],  # 2 → 3
        [1, 3]  # 3 → 1 creates a cycle
    ]

    # Run canFinish
    # can_finish = sol.canFinish(numCourses, prerequisites)
    # print("Can finish all courses:", can_finish)

    # Run findOrder
    order = sol.find_order(numCourses, prerequisites)
    print("Course order:", order)


if __name__ == "__main__":
    main()




