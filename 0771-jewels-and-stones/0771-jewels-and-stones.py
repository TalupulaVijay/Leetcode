class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            c=stones.count(i)
            count+=c
        return count    

        