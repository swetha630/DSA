class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=len(s)
        res=[[] for _ in range(numRows)]
        if numRows==1:
            return s
        i=0
        while i<l:
            for d in range(numRows):
                if i<l:
                    res[d].append(s[i])
                    i+=1
            for u in range(numRows-2,0,-1):
                if i<l:
                    res[u].append(s[i])
                    i+=1
        ans=""
        for r in res:
            ans+=''.join(r)
        return ans

        