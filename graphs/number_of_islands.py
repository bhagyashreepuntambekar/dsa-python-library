class Solution:
    def num_of_islands(self,grid):
        rows = len(grid)
        col = len(grid[0])
        count = 0
        visited = [[False for _ in range(col)] for _ in range(rows)]

        for i in range(rows):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    self.dfs(i,j,visited,grid,rows,col)
                    count+=1
        return count

    def dfs(self, i, j, visited, grid, rows, col):
        if i < 0 or j < 0 or i >= rows or j >= col or grid[i][j] != 1 or visited[i][j]:
            return
        visited[i][j]=True
        self.dfs(i+1, j, visited, grid, rows, col)
        self.dfs(i, j+1, visited, grid, rows, col)
        self.dfs(i-1, j, visited, grid, rows, col)
        self.dfs(i, j-1, visited, grid, rows, col)


grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 0]
]

sol = Solution()
print(sol.num_of_islands(grid))