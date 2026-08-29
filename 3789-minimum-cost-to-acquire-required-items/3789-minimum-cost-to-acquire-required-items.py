class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        oc1=need1*cost1 
        oc2=need2*cost2 
        cb=max(need1,need2)*costBoth
        partial=min(need1,need2)*costBoth
        p1=(need1-min(need1,need2))*cost1 
        p2=(need2-min(need1,need2))*cost2 
        ptot=partial+p1+p2 
        return min(oc1+oc2,min(cb,ptot))
        