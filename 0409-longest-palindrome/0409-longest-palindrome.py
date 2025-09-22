class Solution:
    def longestPalindrome(self, s: str) -> int:
        l=0
        char_set=set()
        for c in s:
            if c in char_set:
                char_set.remove(c)
                l+=2
            else:
                char_set.add(c)
        if char_set:
            l+=1
        return l                


        