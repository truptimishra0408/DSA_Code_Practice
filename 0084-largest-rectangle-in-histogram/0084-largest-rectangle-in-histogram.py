from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Calculate left index (NSL)
        leftindex = []
        stack = []
        pseudo = -1
        for i in range(n):
            if len(stack) == 0:
                leftindex.append(pseudo)
            elif len(stack) > 0 and stack[-1][0] < heights[i]:
                leftindex.append(stack[-1][1])
            elif len(stack) > 0 and stack[-1][0] >= heights[i]:
                while len(stack) > 0 and stack[-1][0] >= heights[i]:
                    stack.pop()
                if len(stack) == 0:
                    leftindex.append(pseudo)
                else:
                    leftindex.append(stack[-1][1])
            stack.append([heights[i], i])
        
        # Calculate right index (NSR)
        rightindex = []
        stack = []
        pseudor = n
        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                rightindex.append(pseudor)
            elif len(stack) > 0 and stack[-1][0] < heights[i]:
                rightindex.append(stack[-1][1])
            elif len(stack) > 0 and stack[-1][0] >= heights[i]:
                while len(stack) > 0 and stack[-1][0] >= heights[i]:
                    stack.pop()
                if len(stack) == 0:
                    rightindex.append(pseudor)
                else:
                    rightindex.append(stack[-1][1])
            stack.append([heights[i], i])
        
        rightindex.reverse()  # reverse to get correct order
        
        # Calculate the maximum area
        areas = []
        for i in range(n):
            width = rightindex[i] - leftindex[i] - 1
            areas.append(width * heights[i])
        
        return max(areas)
