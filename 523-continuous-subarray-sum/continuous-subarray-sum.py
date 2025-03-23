class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        mp={0:-1}
        total_sum=0
        for i in range(n):
            total_sum+=nums[i]
            remainder=total_sum%k
            if remainder in mp:
                if i-mp[remainder]>=2:
                    return True
                
            else:
                mp[remainder]=i
        return False
        