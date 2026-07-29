class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        return len(s)-1-s.rfind(' ')