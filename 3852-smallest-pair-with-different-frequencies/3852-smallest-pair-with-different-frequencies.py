class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        di={}
        if len(nums)==1:
            return [-1,-1]
        nums.sort()
        for i in nums:
            di[i]=di.get(i,0)+1
        res=[]
        for k,v in di.items():
            res.append(k)
            prev=v
            break 
        for k,v in di.items():
            if v!=prev:
                res.append(k)
                break 
        if len(res)<2:
            return [-1,-1]
        return res


