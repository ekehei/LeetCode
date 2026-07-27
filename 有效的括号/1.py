class Solution:
    def isValid(self, s: str) -> bool:
        left=[]
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for x in s:
            if  x in '{[(':
                left.append(x)
            else:
                if not left or mapping[x]!=left[-1]:
                    return False
                left.pop()
        return not left