class Solution(object):
    def countBits(self, n):
        res=[]
        for i in range(0,n+1):
            b=bin(i)[2:]
            c=b.count('1')
            res.append(c)
        return res    

        
        