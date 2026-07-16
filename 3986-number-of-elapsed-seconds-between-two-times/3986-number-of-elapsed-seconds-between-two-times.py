class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        l=startTime.split(":")
        e=endTime.split(":")
        h=(int(e[0])-int(l[0]))*60*60 
        m=(int(e[1])-int(l[1]))*60 
        s=int(e[2])-int(l[2])
        return h+m+s

        