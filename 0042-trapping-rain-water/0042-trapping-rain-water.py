from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        
        if size == 0:
            return 0
        
        # Initialize arrays to store the maximum left and right values
        mxl = [0] * size
        mxr = [0] * size
        
        # Fill the mxl array
        mxl[0] = height[0]
        for i in range(1, size):
            mxl[i] = max(mxl[i-1], height[i])
        
        # Fill the mxr array
        mxr[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            mxr[i] = max(mxr[i+1], height[i])
        
        # Calculate the water trapped at each index
        total_water = 0
        for i in range(size):
            total_water += min(mxl[i], mxr[i]) - height[i]
        
        return total_water
