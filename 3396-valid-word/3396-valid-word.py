class Solution(object):
    def isValid(self, word):
        word=word.lower()
        if len(word)<3:
            return False
        v=0
        c=0        
        for i in word: 
            if not i.isalnum():
                return False 
            if i.isalpha():
                if i in "aeiou":
                    v+=1
                else:
                    c+=1
        return c>=1 and v>=1                 



        