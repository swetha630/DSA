class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bc=ac=lc=oc=nc=0
        for i in text:
            if i=="b":
                bc+=1
            elif i=="a":
                ac+=1
            elif i=="l":
                lc+=1
            elif i=="o":
                oc+=1
            elif i=="n":
                nc+=1
        sm=min(bc,ac,nc)
        dm=min(lc//2,oc//2)
        return min(sm,dm)
        