class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        c=0
        s=0
        for i in range(1,(len(salary))-1):
            c+=1
            s+=salary[i]
        return s/c    
        