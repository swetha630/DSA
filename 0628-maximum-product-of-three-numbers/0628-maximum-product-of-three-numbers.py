class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        p=nums[-1]*nums[-2]*nums[-3]
        p1=nums[0]*nums[1]*nums[l-1]
        return max(p,p1)