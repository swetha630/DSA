class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xc=yc=0
        rem=""
        res=""
        for i in s:
            if i==x:
                xc+=1
            elif i==y:
                yc+=1
            else:
                rem+=i 
        while yc:
            res+=y 
            yc-=1
        while xc:
            res+=x
            xc-=1
        res+=rem 
        return res

        
      