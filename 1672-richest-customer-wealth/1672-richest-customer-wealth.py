class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            n=0
            for j in range(len(accounts[0])):
                n+=accounts[i][j]
            l.append(n)    
        l.sort()
        return l[-1]        

        