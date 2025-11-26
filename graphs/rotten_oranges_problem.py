from collections import deque


class Solution:
    def count_time(self,grid):
        row = len(grid)
        col = len(grid[0])
        ans = 0
        visited = [[False for c in range(col)]for r in range(row)]
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append(((i,j),0))
                    visited[i][j] = True

        while q:
            (i,j),time = q.popleft()
            ans = max(ans,time)

            if i-1 >=0 and not visited[i-1][j] and grid[i-1][j]==1:
               q.append(((i-1,j),time+1))
               visited[i-1][j] = True
            if i+1 <row and not visited[i+1][j] and grid[i+1][j]==1:
               q.append(((i+1,j),time+1))
               visited[i+1][j] = True
            if j - 1 >= 0 and not visited[i][j-1] and grid[i][j-1] == 1:
               q.append(((i, j-1), time + 1))
               visited[i][j-1] = True
            if j + 1 < col and not visited[i][j+1] and grid[i][j+1] == 1:
               q.append(((i, j+1), time + 1))
               visited[i][j+1] = True

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    return -1

        return ans

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

solution = Solution()
result = solution.count_time(grid)
print("Time to rot all oranges:", result)




