class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        checker = {}

        for number in nums:
            checker[number] = 1 + checker.get(number, 0)

        for e, v in checker.items():
            freq[v].append(e)
        output = []


        for i in range(len(freq) - 1, -1, -1):
            for number in freq[i]:
                output.append(number)
                if len(output) == k:
                    return output

        
        