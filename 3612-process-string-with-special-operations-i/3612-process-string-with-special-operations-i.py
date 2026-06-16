class Solution:
    def processStr(self, s: str) -> str:
        res=""
        for i in s:
            if i.isalpha():
                res+=i 
            if i=="*":
                if res:
                    res=res[:-1]
            if i=="#":
                res+=res
            if i=="%":
                res=res[::-1]
        return res
        