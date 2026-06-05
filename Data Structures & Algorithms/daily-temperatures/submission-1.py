class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for i, a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                stackNum, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([a, i])
        return res
        