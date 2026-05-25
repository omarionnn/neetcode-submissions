class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker1, checker2 = {}, {}

        for a in s:
            checker1[a] = checker1.get(a, 0) + 1
        
        for b in t:
            checker2[b] = checker2.get(b, 0) + 1

        return checker1 == checker2
        