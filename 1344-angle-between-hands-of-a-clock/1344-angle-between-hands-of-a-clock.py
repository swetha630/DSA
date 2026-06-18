class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 6
        h = (hour % 12) * 30 + minutes * 0.5
        diff = abs(h - m)
        return min(diff, 360 - diff)