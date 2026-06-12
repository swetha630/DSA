from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = set("qwertyuiop")
        sr = set("asdfghjkl")
        tr = set("zxcvbnm")
        res = []
        for w in words:
            u = set(w.lower()) 
            if u <= fr or u <= sr or u <= tr: 
                res.append(w)
        return res



        