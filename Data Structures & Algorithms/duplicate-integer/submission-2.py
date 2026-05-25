class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for number in nums:
            if number in checker:
                return True
            checker.add(number)
        return False 
        