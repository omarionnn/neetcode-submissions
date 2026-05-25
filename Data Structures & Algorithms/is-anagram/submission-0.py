class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1

        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        return t_dict == s_dict
        