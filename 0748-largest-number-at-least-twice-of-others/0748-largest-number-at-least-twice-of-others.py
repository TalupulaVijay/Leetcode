class Solution(object):
    def dominantIndex(self, nums):
        m=max(nums)
        ind=nums.index(m)
        for i in nums:
            if i!=m and m<2*i:
                return -1
        return ind        
        