class Solution:
    def longestSubarray(self, nums):
        zero_count = 0
        longest_window = 0
        i = 0

        for j in range(len(nums)):
            zero_count += (nums[j] == 0)

            # Shrink the window until the zero count comes under the limit.
            while zero_count > 1:
                zero_count -= (nums[i] == 0)
                i += 1

            longest_window = max(longest_window, j - i)

        return longest_window
