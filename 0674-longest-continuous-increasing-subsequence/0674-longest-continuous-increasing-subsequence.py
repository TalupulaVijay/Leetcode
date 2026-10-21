class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        max_len=1
        cur_len=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                cur_len+=1
            else:
                cur_len=1
            max_len=max(cur_len,max_len)
        return max_len                

        