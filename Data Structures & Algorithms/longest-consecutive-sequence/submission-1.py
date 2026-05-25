class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        checker = set()
        output = 0

        for number in nums:

            if number not in checker:
                length = 0
                while number + length in all_nums:
                    checker.add(number + length)
                    length += 1
                output = max(output, length)
            else:
                continue
        return output


        