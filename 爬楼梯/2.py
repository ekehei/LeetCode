from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def cs(i):
            if i<=1:
                return 1
            return cs(i-1)+cs(i-2)
        return cs(n)