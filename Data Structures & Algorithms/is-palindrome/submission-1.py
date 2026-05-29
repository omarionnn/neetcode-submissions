class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''

        #ensure we only are using qualified elements
        for element in s:
            if element.isalnum():
                res += element.lower()

        print(res)

        #pointers to check palindromic condition
        left, right = 0, len(res) - 1

        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True

        