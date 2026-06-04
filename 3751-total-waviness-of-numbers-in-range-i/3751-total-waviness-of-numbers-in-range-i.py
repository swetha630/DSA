class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        c=0
        for i in range(num1,num2+1):
            s=str(i)
            for i in range(1,len(s)-1):
                if ((s[i-1]<s[i] and s[i+1]<s[i]) or (s[i-1]>s[i] and s[i+1]>s[i])) :
                    c+=1 
        return c


        