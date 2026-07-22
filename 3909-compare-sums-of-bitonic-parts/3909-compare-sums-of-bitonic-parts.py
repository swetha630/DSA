class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        ap=dp=0
        idx=-1
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                idx=i 
        ap=sum(nums[:idx+1])
        dp=sum(nums[idx:])
        if ap==dp:
            return -1
        elif ap>dp:
            return 0
        else:
            return 1

            
