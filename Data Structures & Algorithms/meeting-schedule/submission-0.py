"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        def overlaps(i1: Interval, i2: Interval) -> bool:
            if i1.start < i2.start:
                return i2.start < i1.end
            else:
                return i1.start < i2.end
        for i in range(n):
            for j in range(i+1, n):
                if overlaps(intervals[i], intervals[j]):
                    return False
        return True