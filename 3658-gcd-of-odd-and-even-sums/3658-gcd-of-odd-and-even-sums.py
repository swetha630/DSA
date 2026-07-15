class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        ov=n*n 
        en=n*(n+1)
        while en:
            ov,en=en,ov%en 
        return ov