from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        normalized = [tuple(sorted(d)) for d in dominoes]
        freq = Counter(normalized)
        result = 0
        for count in freq.values():
            result += count * (count - 1) // 2
        return result
