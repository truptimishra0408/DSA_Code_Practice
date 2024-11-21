class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        count=0
        row_map={}
        for row in grid:
            row_tuple=tuple(row)
            if row_tuple in row_map:
                row_map[row_tuple]+=1
            else:
                row_map[row_tuple]=1
        for c in range(n):
            column=tuple(grid[r][c] for r in range(n))
            if column in row_map:
                count+=row_map[column]
        return count
            


        