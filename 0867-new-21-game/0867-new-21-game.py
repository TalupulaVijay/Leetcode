class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k==0 or n>=k+maxPts:
            return 1.0
        dp=[0.0]*(n+1)
        dp[0]=1.0
        ws=1.0
        res=0.0
        for i in range(1,n+1):
            dp[i]=ws/maxPts
            if i<k:
                ws+=dp[i]
            else:
                res+=dp[i]
            if i-maxPts>=0:
                ws -= dp[i - maxPts]
        return res        

        