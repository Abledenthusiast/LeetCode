# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        list.sort(intervals, key = lambda x : x.start)
        min_rooms = 1
        heap = []
        heapq.heapify(heap)
        for i in range(0, len(intervals)):
            if not heap:
                heapq.heappush(heap, intervals[i].end)
            else:
                if heap[0] <= intervals[i].start:
                    #next meeting starts after others have ended
                    heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
        return max(min_rooms, len(heap))
                