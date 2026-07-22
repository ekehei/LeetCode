class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix=strs[0]
        for i in range(1,len(strs)):
            prefix=self.lcp(prefix,strs[i])
            if not strs:
                break
        return prefix

        
    def lcp(self,str1,str2):
        length=min(len(str1),len(str2))
        index=0
        while index<length and str1[index]==str2[index]:
            index+=1
        return str1[:index]