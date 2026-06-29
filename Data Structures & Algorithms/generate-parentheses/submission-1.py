class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        curr = []

        def backtrack(open, close, curr):
            if open == close == n:
                output.append(''.join(curr))
                return 

            if open < n:
                curr.append('(')
                backtrack(open + 1, close, curr)
                curr.pop()
            if close < open:
                curr.append(')')
                backtrack(open, close + 1, curr)
                curr.pop()

        backtrack(0, 0, [])
        return output

        