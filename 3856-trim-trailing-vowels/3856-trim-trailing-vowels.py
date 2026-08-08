class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        ss="aeiou"
        for i in range(len(s)-1,-1,-1):
            if s[i] not in ss:
                break 
        if i==0 and s[i] in ss:
            return ""
        else:
            return s[:i+1]


        

        