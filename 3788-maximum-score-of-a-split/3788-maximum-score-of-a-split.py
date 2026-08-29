from typing import List
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * n
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + nums[i]
        sm = [0] * n
        sm[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            sm[i] = min(nums[i], sm[i+1])
        ms = float('-inf')
        for i in range(n-1): 
            ms = max(ms, ps[i] - sm[i+1])
        return ms

    