class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        path=[]

        if len(path)==n:
            print(path)
            return

        for i in n:
            path.append(i)
            permute(n,path)
            path.pop(i)