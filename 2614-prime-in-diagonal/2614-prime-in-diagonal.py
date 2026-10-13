class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        l=[]
        n=len(nums)
        for i in range(n):
            l.append(nums[i][i])
            l.append(nums[i][n-1-i])
        lar=0    
        for i in l:
            prime=True
            if i<2:
                prime=False
            else:    
                for j in range(2,int(i**0.5+1)):
                    if (i%j==0):
                        prime=False
                        break
            if(prime):
                lar=max(lar,i)
        return lar                

        