class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        # Using standard dict or defaultdict works perfectly here
        checker = defaultdict(int)
        
        # freq array needs size len(nums) + 1 to handle maximum possible frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 1: Count frequencies
        for number in nums:
            checker[number] += 1

        # Step 2: Map frequency to the list of numbers
        for num, val in checker.items():
            freq[val].append(num)
        
        # Step 3: Iterate backwards from the maximum possible frequency down to 0
        for i in range(len(freq) - 1, -1, -1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res
        