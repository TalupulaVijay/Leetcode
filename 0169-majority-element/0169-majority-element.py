
class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        m=max(freq,key=freq.get) 
        return m       

        