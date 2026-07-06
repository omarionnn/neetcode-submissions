class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        comb = []

        def backtrack(i, sum):
            if target == sum:
                output.append(comb.copy())
                return 

            if sum > target or i >= len(nums):
                return 

            comb.append(nums[i])
            backtrack(i, sum + nums[i])

            comb.pop()
            backtrack(i + 1, sum)

        backtrack(0, 0)
        return output
        