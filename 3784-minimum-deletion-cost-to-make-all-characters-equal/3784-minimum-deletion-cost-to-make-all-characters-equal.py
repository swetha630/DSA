class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        hm={}
        for i in range(len(s)):
            hm[s[i]]=hm.get(s[i],0)+cost[i]
        l=[val for k,val in hm.items()]
        ls=sum(l)
        mc=float('inf')
        for i in l:
            mc=min(mc,ls-i)
        return mc