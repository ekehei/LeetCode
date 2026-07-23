class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        st=set()
        for x in nums:
            if x in st:
                return True
            st.add(x)
        return False