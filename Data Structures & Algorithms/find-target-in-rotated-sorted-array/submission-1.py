class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            #if target on left side:
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            #target on right side
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1       




        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m

            #on the left side
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            #on the right side
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


        
         