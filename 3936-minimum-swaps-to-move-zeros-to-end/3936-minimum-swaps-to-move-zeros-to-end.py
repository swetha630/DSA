class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        c=0
        l=len(nums)
        for i in nums:
            if i==0:
                c+=1
        p=0
        for i in range(l-c,l):
            if nums[i]!=0:
                p+=1
        if p==0:
            return 0
        return p 