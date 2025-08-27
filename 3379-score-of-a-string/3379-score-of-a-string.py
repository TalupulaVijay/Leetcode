class Solution(object):
    def scoreOfString(self, s):
        res=[]
        for i in s:
            res.append(ord(i)) 
        a=0 
        for i in range(len(res)-1):
            a+=(abs(res[i]-res[i+1]))
        return a   

           
        
                

        
        