class Solution(object):
    def reverseVowels(self, s):
        vowels=set('aeiouAEIOU')
        s=list(s)
        st=0
        end=len(s)-1
        while st<end:
            if s[st] not in vowels:
                st+=1
            elif s[end] not in vowels:
                end-=1
            else:
                s[st],s[end]=s[end],s[st]
                st+=1
                end-=1
        return ''.join(s)        
        
        