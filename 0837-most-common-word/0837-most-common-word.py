class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        paragraph=paragraph.lower()
        words=paragraph.split()
        freq={}
        for i in words:
            if i not in banned:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
        max=0
        max_str=""
        for i,count in freq.items():
            if count>max:
                max=count
                max_str=i
        return max_str                   
        