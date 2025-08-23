class Solution(object):
    def isPerfectSquare(self, num):
        if num<=2:
            return True
        low=2
        high=num//2
        while low<=high:
            mid=(low+high)//2 
            s=mid*mid
            if s==num:
                return True
            elif s<num:
                low=mid+1
            else:
                high=mid-1
        return False          

        