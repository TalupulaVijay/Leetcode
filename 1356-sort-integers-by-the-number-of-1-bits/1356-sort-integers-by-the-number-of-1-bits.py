class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        freq={}
        for i in arr:
            freq[i]=bin(i).count("1")
        keys=list(arr)
        n=len(keys) 
        for i in range(n):
            for j in range(0,n-i-1):
                if freq[keys[j]]>freq[keys[j+1]] or  (freq[keys[j]] == freq[keys[j + 1]] and
                     keys[j] > keys[j + 1]):
                    keys[j],keys[j+1]=keys[j+1],keys[j]
        
        return keys
                           



        