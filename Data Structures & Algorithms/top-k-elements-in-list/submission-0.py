class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = {}
        output = []

        for number in nums:
            checker[number] = checker.get(number, 0) + 1

        while k > 0:
            maxxie = max(checker, key = checker.get)
            output.append(maxxie)
            del checker[maxxie]
            k -= 1

        return output 
        