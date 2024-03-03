class Solution:
    def isHappy(self, n: int) -> bool:

        temp_n=n
        
        seen = set()
        while temp_n!=1 and temp_n not in seen:
            seen.add(temp_n)
            sum=0
            while temp_n>=10:
                digit=temp_n%10
                sum+= (digit**2)
                temp_n=temp_n//10
                
            if temp_n<10: 
                    sum+=(temp_n**2)

            print(sum)
            temp_n =sum
        return temp_n==1



               

        