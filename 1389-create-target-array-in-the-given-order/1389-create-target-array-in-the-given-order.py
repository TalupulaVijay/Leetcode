class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            a=nums[i]
            ind=index[i]
            res.insert(ind,a)
        return res    
        