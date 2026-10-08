class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l=[0]*len(nums)
        for i in range(len(nums)):
            l[i]=nums[i]
        for num in nums:
            l.append(num)
        return l        


        