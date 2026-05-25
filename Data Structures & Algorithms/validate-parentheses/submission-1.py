class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            elif element == ')' and (len(stack) != 0 and stack[-1] == '('):
                stack.pop()
            elif element == ']' and (len(stack) != 0 and stack[-1] == '['):
                stack.pop()
            elif element == '}' and (len(stack) != 0 and stack[-1] == '{'):
                stack.pop()
            else:
                return False

        return len(stack) == 0
        