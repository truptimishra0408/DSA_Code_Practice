class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        max_value=0
        while i<j:
            pair_sum=nums[i]+nums[j]
            max_value=max(pair_sum,max_value)
            i+=1
            j-=1
        return max_value
        