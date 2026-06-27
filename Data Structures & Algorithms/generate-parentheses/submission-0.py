class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def backtrack(open, close):
            if open == close == n:
                output.append("".join(stack))
                return 

            if open < n:
                stack.append('(')
                backtrack(open + 1, close)
                stack.pop()

            if open > close:
                stack.append(')')
                backtrack(open, close + 1)
                stack.pop()
       


        backtrack(0, 0)
        return output



        