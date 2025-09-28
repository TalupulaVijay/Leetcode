class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            if max_len<right-left+1:
                max_len=right-left+1
        return max_len        

        