class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        for i in range(len(nums)):
            n=nums[i]
            c=0
            for j in range(len(nums)):
                if n>nums[j]:
                    c+=1
            res[i]=c
        return res           

        