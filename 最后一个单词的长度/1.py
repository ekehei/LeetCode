class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                length+=1
                if s[i-1]==' ':
                    return length
            if i==0:
                return length