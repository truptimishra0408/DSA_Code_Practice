class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        i=0
        j=0
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1
        
        