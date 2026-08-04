class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            for d in str(i):
                if d==str(digit):
                    c+=1
        return c