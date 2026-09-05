class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        si=-1
        pfm=[0]*n 
        sfm=[0]*n
        pfm[0]=nums[0]
        sfm[-1]=nums[-1]
        for i in range(1,n):
            pfm[i]=max(pfm[i-1],nums[i])
        for i in range(n-2,-1,-1):
            sfm[i]=min(sfm[i+1],nums[i])
        for i in range(n):
            if pfm[i]-sfm[i]<=k:
                si=i 
                break 
        return si

