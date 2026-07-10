class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or r == rows or i >= len(word) or c == cols or board[r][c] != word[i]):
                return 

            temp = board[r][c]
            board[r][c] = '#'

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if backtrack(row, col, i + 1):
                    return True

            board[r][c] = temp

            return False
                

            

            


        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
        