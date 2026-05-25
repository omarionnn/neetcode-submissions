class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)

            else:
                res.append([start, end])

        return res
        