class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nl=[0]
        n=len(gain)
        for i in range(n):
            val=nl[-1]+gain[i]
            nl.append(val)
        return max(nl)

        