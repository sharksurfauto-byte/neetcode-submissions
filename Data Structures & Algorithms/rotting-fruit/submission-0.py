class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = []
        minutes = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh +=1 
                elif grid[i][j]==2:
                    rotten.append((i,j))
        
        while rotten and fresh>0:
            minutes +=1
            current = []
            for i,j in rotten:
                check = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
                for r,c in check:
                    if 0<=r<ROWS and 0<=c<COLS and grid[r][c]==1:
                        grid[r][c]=2
                        current.append((r,c))
                        fresh-=1
                        if fresh==0:
                            return minutes
            rotten = current
        
        if fresh==0:
            return minutes
        
        else:
            return -1