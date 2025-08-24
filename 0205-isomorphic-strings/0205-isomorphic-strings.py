class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for ch1,ch2 in zip(s,t):
            if ch1 in st:
                if st[ch1]!=ch2:
                    return False
            else:
                st[ch1]=ch2


            if ch2 in ts:
                if ts[ch2]!=ch1:
                    return False
            else:        
                ts[ch2]=ch1
        return True                        
        
        