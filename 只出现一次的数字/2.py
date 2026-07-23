class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        flag=0
        for x in nums:
            flag^=x
        return flag