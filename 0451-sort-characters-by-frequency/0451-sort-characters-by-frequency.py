from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        sd=Counter(s)
        rd=sorted(sd.items(), key=lambda x:-x[1])
        res=''.join(char*count for char,count in rd)
        return res

        