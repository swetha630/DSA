class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l=len(landStartTime)
        w=len(waterStartTime)
        tot=float('inf')
        for i in range(l):
            for j in range(w):
                lt=max(landStartTime[i]+landDuration[i],waterStartTime[j])
                lt+=waterDuration[j]

                wt=max(waterStartTime[j]+waterDuration[j],landStartTime[i])
                wt+=landDuration[i]
                tot=min(tot,min(lt,wt))
        return tot

       