class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in jewels:
            for j in range(len(stones)):
                if i==stones[j]:
                    c+=1
                    
        return c        
        