class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for value in freq.values():
            c=0
            for j in range(1,value+1):
                if value%j==0:
                    c+=1
            if c==2:
                return True  
        return False
        