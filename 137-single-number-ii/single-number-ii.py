class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in range(32):
            temp=1<<i
            count_one=0
            count_zero=0
            for num in nums:
                if (num & temp)==0:
                    count_zero+=1
                else:
                    count_one+=1
            if count_one%3==1:
                result|=temp
        if result>=2**31:
            result-=2**32
        return result



        