class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        mx=nums[0]
        n=len(nums)
        ans=0
        for i in range(k,n):
            mx=max(nums[i-k],mx)
            ans=max(ans,mx+nums[i])
        return ans