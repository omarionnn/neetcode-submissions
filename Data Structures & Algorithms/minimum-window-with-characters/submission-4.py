class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''

        countT, window = defaultdict(int), defaultdict(int)

        for letter in t:
            countT[letter] += 1

        have, need = 0, len(countT)
        resLen, res = float('inf'), [-1, -1]

        left = 0
        for right in range(len(s)):
            c = s[right]

            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while need == have:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1
        left, right = res
        return s[left: right + 1] if resLen != float('inf') else ""





        