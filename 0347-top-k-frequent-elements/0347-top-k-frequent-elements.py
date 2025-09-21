from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=Counter(nums)
        sor=sorted(freq.items(), key=lambda x: x[1],reverse=True )
        res=[item for item,count in sor[:k]]  
        return res   

        