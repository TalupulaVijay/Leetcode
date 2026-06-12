class Solution:
    def romanToInt(self, s: str) -> int:
        fre={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        p=0
        for i in reversed(s):
            value=fre[i]
            if value<p:
                total-=value
            else:
                total+=value
                p=value
        return total
        