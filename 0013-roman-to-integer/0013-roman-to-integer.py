class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        i=0
        while i<len(s):
            firstInt = self.charToInt(s[i])
            if((i+1)<len(s) and firstInt<self.charToInt(s[i+1])):
                #secondInt = self.charToInt(s[i+1])
                firstInt=self.charToInt(s[i+1])-firstInt
                i=i+1
                  
            count+=firstInt
            i=i+1
            
        return count
    
    def charToInt(self, s: str) -> int:
        switch_dict = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
            }
        return switch_dict.get(s, -1) 


    
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans