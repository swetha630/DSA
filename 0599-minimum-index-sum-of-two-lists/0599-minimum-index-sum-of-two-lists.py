class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm={word:i for i,word in enumerate(list1)}
        mn=float('inf')
        l=[]
        for j,w in enumerate(list2):
            if w in hm:
                s=hm[w]+j
                if s<mn:
                    mn=s 
                    l=[w]
                elif s==mn:
                    l.append(w)
        return l