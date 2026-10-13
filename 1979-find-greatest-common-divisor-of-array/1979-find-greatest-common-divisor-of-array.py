class Solution:
    def findGCD(self, nums: list[int]) -> int:
        s=min(nums)
        l=max(nums)

        for i in range(l+1,0,-1):
            if s%i==0 and l%i==0:
                return i 
                break

        