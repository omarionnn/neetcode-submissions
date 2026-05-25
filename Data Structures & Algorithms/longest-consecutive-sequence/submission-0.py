class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)

        res = 0

        for number in nums:
            if number - 1 not in checker:
                length = 0

                while (number + length) in checker:
                    length += 1

                res = max(res, length)

        return res
        