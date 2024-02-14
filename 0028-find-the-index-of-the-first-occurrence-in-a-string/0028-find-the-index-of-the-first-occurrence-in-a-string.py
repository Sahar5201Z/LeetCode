class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count=0
        j=0
        i=0
        while i <len(haystack):
                if j<len(needle) and haystack[i]==needle[j]:
                    print(haystack[i]+str(count)+"yesss"+str(i)+str(j))
                    count+=1
                    j+=1
                    i+=1
                    if(count==len(needle)):
                        print(str(len(needle))+str(count)+"ok"+str(i)+str(j))
                        result = i-(len(needle))
                        print(result)
                        return result
                elif j<len(needle) and haystack[i]!=needle[j] :
                    print(haystack[i]+str(count)+"noooo"+str(i)+str(j))
                    i=i-j+1
                    count=0
                    j=0
  
        return -1
                
"""class Solution(object):
    def strStr(self, haystack, needle):
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                return i
        # if we exit the loop, return -1        
        return -1"""