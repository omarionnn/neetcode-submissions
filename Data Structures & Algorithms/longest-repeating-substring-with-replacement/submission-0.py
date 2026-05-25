class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        checker = {}
        l = 0
        res = 0

        for r in range(len(s)):
            checker[s[r]] = 1 + checker.get(s[r], 0)

            while (r - l + 1) - max(checker.values()) > k:
                checker[s[l]] -= 1
                l += 1


            res = max(res, r - l + 1)

        return res



               

           

        
        