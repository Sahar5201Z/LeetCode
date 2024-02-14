"""class Solution:
    def mySqrt(self, x: int) -> int:
        if(x<2):
            return x
        
        for i in range(x//2+2):
            if(x< (i**2)):
                return i-1
        return None"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left =0
        right=x
        while(left<=right):
            mid=(left+right)//2 
            if(mid*mid<x):
                left=mid+1
            elif mid*mid >x:
                right= mid-1
            else:
                return mid
        return right



        