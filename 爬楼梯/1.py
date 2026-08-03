class Solution:
    def climbStairs(self, n: int) -> int:
        p=q=0
        r=1
        for i in range(1,n+1):
            p=q
            q=r
            r=p+q
        return r