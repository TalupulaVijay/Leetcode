class Solution(object):
    def reverseBits(self, n):
        b=bin(n)[2:].zfill(32)
        c=b[::-1]
        return int(c,2)