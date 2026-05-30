class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                triplet = nums[left] + nums[right] + a

                if triplet < 0:
                    left += 1
                elif triplet > 0:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], a])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


        return res


        