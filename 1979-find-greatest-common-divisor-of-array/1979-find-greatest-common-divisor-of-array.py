class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=float('inf')
        mx=float('-inf')
        for i in nums:
            if i<mn:
                mn=i 
            if i>mx:
                mx=i 
        while mn:
            mx,mn=mn,mx%mn 
        return mx
        