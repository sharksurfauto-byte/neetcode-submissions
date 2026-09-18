class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if 0>r or 0>c or r>=ROWS or c>=COLS or grid[r][c]=="0":
                return
            
            grid[r][c]="0"

            neighbors = [(r+1,c),(r-1,c), (r,c-1), (r,c+1)]
            for row, col in neighbors:
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col]=="1":
                    dfs(row, col)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)

        return count
        
