from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        l = 0
        of = False
        for f in c.values():
            if f % 2 == 0:
                l += f
            else:
                l += f - 1
                of = True
        if of:
            l += 1
        return l

        