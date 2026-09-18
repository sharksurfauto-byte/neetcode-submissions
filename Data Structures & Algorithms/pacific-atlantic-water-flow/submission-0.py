class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(start, visited):
            queue = deque(start)
            visited.update(start)
            while queue:
                r,c = queue.popleft()
                for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                    nr,nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))



        pacific_reach = set()
        atlantic_reach = set()

        pacific_starts = [(0,c) for c in range(COLS)] + [(r,0) for r in range(ROWS)]
        atlantic_starts= [(ROWS-1,c) for c in range(COLS)] + [(r,COLS-1) for r in range(ROWS)]

        bfs(pacific_starts,pacific_reach)
        bfs(atlantic_starts,atlantic_reach)

        return [list(cell) for cell in pacific_reach & atlantic_reach]