class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=float('-inf')
        sm=float('-inf')
        for i,val in enumerate(nums):
            if val>mx:
                mx=val 
                mi=i
        for i,val in enumerate(nums):
            if (val>sm and i!=mi):
                sm=val
        return (mx-1)*(sm-1)
