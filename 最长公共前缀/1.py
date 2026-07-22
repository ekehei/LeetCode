class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        Prefix=strs[0]
        for i in range(1,len(strs)):
            for j in range(min(len(Prefix),len(strs[i]))+1):
                if Prefix[:j]!=strs[i][:j]:
                    a=j
                    break
            Prefix=Prefix[:a]
        return Prefix