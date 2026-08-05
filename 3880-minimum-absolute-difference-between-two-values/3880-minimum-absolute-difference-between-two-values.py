class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mn=float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==1 and nums[j]==2:
                    mn=min(mn,abs(i-j))
        if mn!=float('inf'):
            return mn 
        else:
            return -1