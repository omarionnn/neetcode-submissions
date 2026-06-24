class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, sum, arr):
            if sum == target:
                res.append(arr.copy())
                return 


            if sum > target or i >= len(candidates):
                return 

            arr.append(candidates[i])
            dfs(i+ 1, sum + candidates[i], arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum, arr)

        dfs(0, 0, [])
        return res
        