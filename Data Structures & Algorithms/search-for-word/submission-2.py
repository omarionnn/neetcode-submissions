class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])


        def backtrack(i, r, c):
            if i == len(word):
                return True

            if (min(r, c) < 0 or r >= rows or c >= cols or board[r][c] != word[i] or i >= len(word)):
                return 

            temp = board[r][c]
            board[r][c] = '#'
            
            res = backtrack(i + 1, r + 1, c) or backtrack(i + 1, r - 1, c) or backtrack(i + 1, r, c + 1) or backtrack(i + 1, r, c - 1)

            board[r][c] = temp

            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(0, r, c):
                        return True

        return False

        
        
        