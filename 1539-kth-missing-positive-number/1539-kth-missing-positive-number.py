class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        
        l=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                l.append(i)
        return l[k-1]       
                
               