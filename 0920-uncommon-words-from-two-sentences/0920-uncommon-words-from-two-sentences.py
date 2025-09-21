from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        freq=Counter(s1+s2)
        res=[word for word,count in freq.items() if count==1]
        return res

        