import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        s=1
        srt=int(math.sqrt(num))
        for i in range(2,srt+1):
            if num%i==0:
                s+=i 
                if i!=num//i:
                    s+=num//i 
        return s==num
