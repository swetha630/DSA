from collections import defaultdict

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        if n == 1:
            return True
        res = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i].append(nums1[i] - nums1[j])
        ce = co = 0
        for k, v in res.items():   
            e = o = 0
            for j in v:
                if j % 2 == 0:
                    e += 1
                else:
                    o += 1
            if e != 0:
                ce += 1
            if o != 0:
                co += 1
        return co == n or ce == n

        
