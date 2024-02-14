"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        count = 0
        last_word=words[len(words)-1]
        print("lassstt  "+last_word)
        for j in range(len(last_word)):
            count +=1
            
        return count"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        count=0
        while i>=0:
            if(s[i]==' '):
                i-=1
            if(s[i]!=' ') :
                while s[i]!=' ' and i>=0:
                    count+=1
                    i-=1
                return count
        

        
        