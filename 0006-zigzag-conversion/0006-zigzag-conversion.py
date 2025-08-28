class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        cr,step=0,1
        
        for ch in s:
            rows[cr]+=ch
            if cr==0:
                step=1
            elif cr==numRows-1:
                step=-1
            cr+=step
        return "".join(rows)               
               

        