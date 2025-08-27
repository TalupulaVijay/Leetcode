class Solution(object):
    def isStrictlyPalindromic(self, n):
        b=bin(n)
        if b==b[::-1]:
            return True
        else:
            return False   