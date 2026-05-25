"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        start_ptr, end_ptr = 0, 0
        count, res = 0, 0

        while start_ptr < len(start):
            if start[start_ptr] < end[end_ptr]:
                count += 1
                start_ptr += 1
            else:
                count -= 1
                end_ptr += 1
            res = max(res, count)

        return res

        