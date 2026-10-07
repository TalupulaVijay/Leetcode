class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            l.append(c)
        return l


        