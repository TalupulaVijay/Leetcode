class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]*len(nums)
        l=0
        for i in range(len(nums)):
            ls[i]=l
            l=l+nums[i]
        rs=[0]*len(nums)
        r=0
        for j in range(len(nums)-1,-1,-1) :
            rs[j]=r
            r=r+nums[j]
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=abs(ls[i]-rs[i]   ) 
        return res    


        