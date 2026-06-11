class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_proof=0
        while r!=len(prices):
            if prices[l]<prices[r]:
                proof=prices[r]-prices[l]
                max_proof=max(max_proof,proof)
            else:
                l=r
            r+=1
        return max_proof
        