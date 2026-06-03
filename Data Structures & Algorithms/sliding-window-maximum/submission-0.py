from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque() # Stores indices of elements
        l = 0
        
        for r in range(len(nums)):
            # 1. Remove smaller elements from the back of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # 2. Add current element's index
            q.append(r)
            
            # 3. Remove left element if it is out of the window bounds
            if l > q[0]:
                q.popleft()
                
            # 4. Once window reaches size k, append max to result
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1 # Slide the left pointer
                
        return res