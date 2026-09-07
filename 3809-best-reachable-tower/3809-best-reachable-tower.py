class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        res=[]
        mcord=[float('inf'),float('inf')]
        mq=float('-inf')
        for x,y,q in towers:
            dist=abs(x-center[0])+abs(y-center[1])
            if dist<=radius:
                if q>mq:
                    mcord=[x,y]
                    mq=q 
                if q==mq:
                    mcord=min(mcord,[x,y])
        if mcord!=[float('inf'),float('inf')]:
            return mcord 
        else:
            return [-1,-1]
                

        