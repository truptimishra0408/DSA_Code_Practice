from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        
        max_c = max(candies)
        
        result = [False] * n
        
        for i in range(n):
            if candies[i] + extraCandies >= max_c:
                result[i] = True
        
        return result
