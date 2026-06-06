class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if i>=1:
                ls=sum(nums[:i])
            else:
                ls=0
            if i<len(nums)-1:
                rs=sum(nums[i+1:])
            else:
                rs=0
            res.append(abs(ls-rs))
        return res
        