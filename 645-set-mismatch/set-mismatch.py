class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dup=-1
        missing=-1
        for i in range(n):
            num=abs(nums[i])
            if nums[num-1]<0:
                dup=num
            else:
                nums[num-1]*=-1
        for i in range(n):
            if nums[i]>0:
                missing=i+1
                break
        return [dup,missing]
        