class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        a=""
        for i in range(k):
            a+=s[i]+" "
        return a.strip()


        