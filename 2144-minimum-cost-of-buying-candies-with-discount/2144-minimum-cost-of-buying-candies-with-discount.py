class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        c=sorted(cost)
        c=c[::-1]
        ans=0
        for i in range(2,len(cost),3):
            ans+=c[i]
        return sum(c)-ans

        