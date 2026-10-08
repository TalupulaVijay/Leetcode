class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        l=[]
        n=len(nums)
        asum=sum(nums)
        d_s=(n*(n+1))//2
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]):
                l.append(nums[i])

        a=d_s-asum+l[0]
        l.append(a)
        return l        



        