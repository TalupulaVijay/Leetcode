class Solution(object):
    def productExceptSelf(self, nums):
        pro = 1
        zero_count = nums.count(0)

        
        if zero_count > 1:
            return [0] * len(nums)

        
        for num in nums:
            if num != 0:
                pro *= num

        res = []
        for num in nums:
            if zero_count == 0:
                res.append(pro // num)
            elif num == 0:
                res.append(pro)
            else:
                res.append(0)
        return res     
        