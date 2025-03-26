class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array=[]
        for row in grid:
            for num in row:
                array.append(num)
        array.sort()
        target=array[len(array)//2]
        result=0
        for num in array:
            if num%x!=target%x:
                return -1
            result+=abs(target-num)//x
        return result
            
        

        