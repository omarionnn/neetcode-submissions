class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for number in nums:
            freq[number] += 1

        bucket = [[] for i in range(len(nums) + 1)]
        for number, count in freq.items():
            bucket[count].append(number)

        output = []
        for i in range(len(bucket) - 1, 0, -1):
            for number in bucket[i]:
                output.append(number)
                if len(output) == k:
                    return output
        