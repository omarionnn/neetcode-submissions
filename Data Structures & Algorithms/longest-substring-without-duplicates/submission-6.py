class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        output = 0
        left = 0

        for right in range(len(s)):
            while s[right] in checker:
                checker.remove(s[left])
                left += 1

            checker.add(s[right])
            output = max(output, right - left + 1)

        return output
        