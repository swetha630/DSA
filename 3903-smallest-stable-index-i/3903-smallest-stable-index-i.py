class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            if i == 0:
                mx = nums[0]
            else:
                mx = max(nums[:i + 1])
            mi = min(nums[i:])
            if mx - mi <= k:
                ans = min(ans, i)
        return ans if ans != n else -1

