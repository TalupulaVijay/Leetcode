class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            temp1=sum(nums[:i])
            temp2=sum(nums[i+1:])
            if temp1==temp2:
                return i 
        return -1        
        