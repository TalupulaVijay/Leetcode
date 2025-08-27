class Solution(object):
    def isPrefixString(self, s, words):
        pre=""
        for word in words:
            pre+=word
            if pre==s:
                return True
            if len(pre)>len(s):
                return False
        return False                   
        
        