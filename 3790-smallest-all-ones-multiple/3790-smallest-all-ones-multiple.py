class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        rem=1%k 
        c=1
        s=set()
        while rem!=0:
            rem=(rem*10+1)%k
            c+=1
            if rem in s:
                return -1
            s.add(rem)
        return c