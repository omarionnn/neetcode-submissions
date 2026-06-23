class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sum, arr):
            if sum == target:
                res.append(arr.copy())
                return 

            if i >= len(nums) or sum > target:
                return 

            arr.append(nums[i])
            dfs(i, sum + nums[i], arr)
            arr.pop()
            dfs(i + 1, sum, arr)

        dfs(0, 0, [])
        return res
        


        