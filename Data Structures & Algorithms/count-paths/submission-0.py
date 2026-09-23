class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            grid[0][i] = 1
        for i in range(m+1):
            grid[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
            
        return grid[m-1][n-1]