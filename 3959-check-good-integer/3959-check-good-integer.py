class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ss=0
        ds=0
        while n:
            dig=n%10
            ds+=dig 
            ss+=(dig*dig)
            n=n//10 
        return (ss-ds)>=50