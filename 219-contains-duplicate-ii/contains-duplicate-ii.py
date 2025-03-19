class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp and abs(mp[nums[i]]-i)<=k:
                return True
            mp[nums[i]]=i
        return False
            
        