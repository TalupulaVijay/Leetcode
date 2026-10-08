class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        l=[]
        for num in nums:
            s=""
            while num!=0:
                rem=num%10
                s+=str(rem)
                num//=10  
            s=s[::-1]
            for i in s:
                l.append(int(i))
            
        return l    

        