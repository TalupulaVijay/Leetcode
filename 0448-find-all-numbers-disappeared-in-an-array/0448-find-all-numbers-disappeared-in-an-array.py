class Solution(object):
    def findDisappearedNumbers(self, nums):
        numset=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in numset:
                res.append(i)
        return res        
                
        