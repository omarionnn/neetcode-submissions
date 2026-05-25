class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or grid[r][c] == '0' or (r, c) in visit):
                return 

            visit.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands 
        