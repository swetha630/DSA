class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        val=int(r**0.5)
        c=0
        if k==1:
            return r-l+1
        for i in range(val+1):
            if l<=pow(i,k)<=r:
                c+=1
        return c