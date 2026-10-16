class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1

        v=0
        for key, value in freq.items():
            if key==value:
                v=max(key,v)
            
        return v if v else -1   

        