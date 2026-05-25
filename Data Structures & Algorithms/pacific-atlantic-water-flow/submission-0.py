class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []

        def dfs(r, c, visit, prevH):
            if(min(r, c) < 0 or r == rows or c == cols or heights[r][c] < prevH or (r, c) in visit):
                return 

            visit.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, visit, heights[r][c])

        #atl check
        for r in range(rows):
            dfs(r, cols - 1, atl, 0)

        for c in range(cols):
            dfs(rows - 1, c, atl, 0)

        #pac check
        for r in range(rows):
            dfs(r, 0, pac, 0)

        for c in range(cols):
            dfs(0, c, pac, 0)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res


        