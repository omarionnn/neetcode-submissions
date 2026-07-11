class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        comb = []
        candidates.sort()

        def backtrack(i, sum):
            if sum == target:
                output.append(comb.copy())
                return 

            if sum > target or i >= len(candidates):
                return 

            comb.append(candidates[i])
            backtrack(i + 1, sum + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, sum)

        backtrack(0, 0)
        return output
        