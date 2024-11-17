class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current=0
        max_gain=current
        for alt in gain:
            current+=alt
            max_gain=max(max_gain,current)
        return max_gain
        