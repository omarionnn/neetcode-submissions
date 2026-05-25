class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        output = []

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            res[tuple(count)].append(word)

        for key, value in res.items():
            output.append(value)

        return output
