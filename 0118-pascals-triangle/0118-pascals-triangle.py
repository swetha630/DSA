class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def genrow(r):
            ans=1
            ansr=[1]
            for i in range(1,r):
                ans=ans*(r-i)
                ans=ans//(i)
                ansr.append(ans)
            return ansr 
        ans=[]
        for i in range(1,numRows+1):
            ans.append(genrow(i))
        return ans