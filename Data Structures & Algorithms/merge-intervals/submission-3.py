class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals.sort(key=lambda i:i[0])

        res.append(intervals[0])

        for start, end in intervals[1:]:
            lastend = res[-1][1]
            if start <= lastend:
                res[-1][1] = max(lastend, end)
            else:
                res.append([start, end])

        return res 
        