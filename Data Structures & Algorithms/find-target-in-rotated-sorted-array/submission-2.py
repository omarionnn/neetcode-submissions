class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # STEP 1: Determine which side is "properly sorted"
            # If the left element is <= middle, the left side is a continuous range.
            if nums[l] <= nums[m]:
                
                # STEP 2: Check if target is inside this sorted left range
                if nums[l] <= target < nums[m]:
                    # Target is definitely here, move right boundary in
                    r = m - 1
                else:
                    # Target is not in the sorted left, search the right side
                    l = m + 1
            
            # STEP 3: Otherwise, the right side must be the "properly sorted" one
            else:
                
                # STEP 4: Check if target is inside this sorted right range
                if nums[m] < target <= nums[r]:
                    # Target is definitely here, move left boundary in
                    l = m + 1
                else:
                    # Target is not in the sorted right, search the left side
                    r = m - 1

        return -1