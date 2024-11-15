class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        water =0
        while i<j:
             # Calculate the water area between the two pointers
            h=min(height[i],height[j])
            w=j-i
            area=h*w
            water =max(water,area)
            # Move the pointers towards larger heights

            if height[i]<height[j]:
                while i<j and height[i]<=h:
                    i+=1
            else:
                while i<j and height[j]<=h:
                    j-=1
        return water


          
            
           