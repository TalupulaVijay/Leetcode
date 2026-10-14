class Solution:
    def countPrimes(self, n: int) -> int:
        c=0
        for i in range(2,n):   
            prime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    prime=False
                    break
            if prime:
                c+=1
        return c                
         
            