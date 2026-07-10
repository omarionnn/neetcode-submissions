class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(open, close, arr):
            if open == close == n:
                output.append(''.join(arr))
                return 

            if open < n:
                arr.append('(')
                backtrack(open + 1, close, arr)
                arr.pop()
            if close < open:
                arr.append(')')
                backtrack(open, close + 1, arr)
                arr.pop()

        backtrack(0, 0, [])
        return output        