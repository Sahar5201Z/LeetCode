"""class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        number=x
        digit=0
        while x!= 0:
            digit = (digit*10) + x%10
            x = x // 10
            print(digit)

        if(number==digit):
            return True""" 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        
        arrX= self.int_to_array(x)
        for i in range(len(arrX)//2):
            if(arrX[i]!=arrX[len(arrX)-i-1]):
                return False
        return True

    def int_to_array(self,num:int)-> list[int]:
        return list(map(int, str(num))) 
    
