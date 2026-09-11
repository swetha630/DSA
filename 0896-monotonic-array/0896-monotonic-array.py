class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=sorted(nums,reverse=False)
        d=sorted(nums,reverse=True)
        if nums==a or nums==d:
            return True 
        else:
            return False