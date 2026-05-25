class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        checker = set()

        l = 0

        for r in range(len(s)):
            while s[r] in checker:
                checker.remove(s[l])
                l += 1


            checker.add(s[r])
            res = max(res, r - l + 1)

        return res

        