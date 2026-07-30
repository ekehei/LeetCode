class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i=j=count=0
        m=len(g)
        n=len(s)


        while i<m and j<n:
            while j<n and g[i]>s[j]:
                j+=1
            if j<n:
                count+=1
            i+=1
            j+=1

        return count