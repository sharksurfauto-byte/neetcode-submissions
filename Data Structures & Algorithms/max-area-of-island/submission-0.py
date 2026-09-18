class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            # base case
            if 0>r or 0>c or r>=ROWS or c>=COLS or grid[r][c]==0:
                return 0
            
            grid[r][c]=0

            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    maxArea = max(maxArea, dfs(i,j))
        
        return maxArea