class Solution(object):
    def maxProfit(self, prices):
        l,r=0,1
        m=0
        while r!=len(prices):
            if prices[l]<=prices[r]:
                d=prices[r]-prices[l]
                m=max(m,d)
            else:
                l=r
            r+=1        
        return m        

        