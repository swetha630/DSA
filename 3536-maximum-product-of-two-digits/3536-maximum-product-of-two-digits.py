class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        temp=n
        while n:
            rem=n%10
            n=n//10 
            l.append(rem)
        l.sort()
        return l[-1]*l[-2]