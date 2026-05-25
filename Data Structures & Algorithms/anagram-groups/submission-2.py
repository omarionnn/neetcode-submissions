class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            checker[tuple(count)].append(word)

        output = []

        for batch in checker.values():
            output.append(batch)

        return output 
        