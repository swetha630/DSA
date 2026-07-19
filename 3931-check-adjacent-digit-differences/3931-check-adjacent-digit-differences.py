class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(1,len(s)):
            a=int(s[i-1])
            b=int(s[i])
            if abs(a-b)>2:
                return False 
        return True
            