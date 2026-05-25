class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = {}, {}

        for letter in s:
            ss[letter] = ss.get(letter, 0) + 1

        for letter in t:
            tt[letter] = tt.get(letter, 0) + 1

        return ss == tt
        