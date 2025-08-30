class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        rev=[w[::-1] for w in words]
        return " ".join(rev)
        