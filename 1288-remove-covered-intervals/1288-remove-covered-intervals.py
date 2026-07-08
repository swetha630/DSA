class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=0
        intervals.sort()
        l=len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i!=j:
                    if (intervals[i][0]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]):
                        c+=1
                        break
        return l-c
        