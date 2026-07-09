class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ranges = []
        for num in nums:
            temp = num
            max_d, min_d = float('-inf'), float('inf')
            while temp > 0:
                dig = temp % 10
                max_d = max(max_d, dig)
                min_d = min(min_d, dig)
                temp //= 10
            ranges.append((num, max_d - min_d))
        max_range = max(r for _, r in ranges)
        return sum(num for num, r in ranges if r == max_range)
