class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        m=len(nums)//2 
        ele=nums[m]
        c=0
        for i in nums:
            if i==ele:
                c+=1
        return c==1
