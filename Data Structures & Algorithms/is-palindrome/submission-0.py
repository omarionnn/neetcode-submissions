class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = ''

        #iterate and append valid characters to valid_s

        for element in s:
            if element.isalnum():
                valid_s += element.lower()

        #initialize two pointers to use to iterate
        left, right = 0, len(valid_s) - 1
        while left < right:
            if valid_s[left] != valid_s[right]:
                return False
            left += 1
            right -= 1
        return True
        