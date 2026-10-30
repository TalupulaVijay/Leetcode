class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums1=[0]*len(nums)
        for i in range(len(nums)):
            nums1[i]=nums[i]
        nums1=nums1+nums
        return nums1           


        