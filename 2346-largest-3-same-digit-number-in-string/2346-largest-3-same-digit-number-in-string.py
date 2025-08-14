class Solution(object):
    def largestGoodInteger(self, num):
        max_num=""
        for i in range(len(num)-2):
            s=num[i:i+3]
            if s[0]==s[1]==s[2]:
                if s>max_num:
                    max_num=s
        return max_num      
        
        