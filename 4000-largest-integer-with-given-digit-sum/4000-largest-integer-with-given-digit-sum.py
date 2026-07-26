class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        if(9*n<s):
            return -1 
        val=[]
        for i in range(n):
            dig=min(9,s)
            val.append(str(dig))
            s-=dig 
        return int("".join(val))
        
        







        
        