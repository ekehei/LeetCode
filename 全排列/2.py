class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def backtrack(first=0):
            if first==n:
                res.append(nums[:])
            for i in range(first,n):
                nums[i],nums[first]=nums[first],nums[i]
                backtrack(first+1)
                nums[i],nums[first]=nums[first],nums[i]


        n=len(nums)
        res=[]
        backtrack()
        return res