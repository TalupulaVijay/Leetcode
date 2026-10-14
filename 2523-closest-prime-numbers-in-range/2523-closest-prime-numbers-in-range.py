class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        def sieve(n):
            prime = [True] * (n + 1)
            prime[0]=prime[1]=False
            p = 2
            while p * p <= n:
                if prime[p]:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
            return prime
        prime=sieve(right+1)
        l=[i for i in range(left,right+1) if prime[i]]
        if len(l)<2:
            return [-1,-1]  
        else: 
            md=inf
            n1=l[0]
            n2=l[1]
            for a,b in zip(l,l[1:]):
                d=b-a
                if d<md:
                    md=d
                    n1=a
                    n2=b
            return [n1,n2]
