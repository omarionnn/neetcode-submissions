class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])

        lastend = intervals[0][1]

        res = 0

        for start, end in intervals[1:]:
            if start < lastend:
                res += 1
            else:
                lastend = end

        return res
        