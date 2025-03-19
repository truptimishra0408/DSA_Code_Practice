class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        st=set()
        for x in nums:
            if x in st:
                st.remove(x)
            else:
                st.add(x)
        return len(st)==0
    

        