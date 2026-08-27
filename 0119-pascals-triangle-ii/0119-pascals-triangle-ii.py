class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def genrow(r):
            ans=1
            ansr=[1]
            for i in range(1,r):
                ans=ans*(r-i)
                ans=ans//(i)
                ansr.append(ans)
            return ansr 
        return genrow(rowIndex+1)