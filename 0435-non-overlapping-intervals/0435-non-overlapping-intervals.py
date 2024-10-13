class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort the intervals based on their start time
        intervals.sort()
        n = len(intervals)

        count = 0
        i, j = 0, 1

        while j < n:
            curr_interval = intervals[i]
            next_interval = intervals[j]

            curr_start, curr_end = curr_interval
            next_start, next_end = next_interval

            if curr_end <= next_start:  # SAFE
                i = j
                j += 1
            elif curr_end <= next_end:
                # GREEDY: Remove next interval
                j += 1
                count += 1
            else:  # curr_end > next_end
                # GREEDY: Remove current interval
                i = j
                j += 1
                count += 1

        return count
