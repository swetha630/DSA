class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        fh=list(s[:n//2])
        fh.sort()
        mc=""
        if n%2!=0:
            mc=s[n//2]
        sh=fh[::-1]
        return "".join(fh)+mc+"".join(sh)
        