class Solution(object):
    def arrangeCoins(self, n):
        c=0
        i=1
        while c+i<=n:
            c+=i
            i+=1
        return i-1    


        


        