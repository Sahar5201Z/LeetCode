class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s_withoutSpace= s.replace(" ", "").lower()
        s_withoutSpace = ''.join(filter(str.isalnum, s)).lower()
        s_array= list(s_withoutSpace)
        i=0
        print(s_array)
        while i<len(s_array)/2:
            if s_array[i]!=s_array[len(s_array)-i-1] :
                return False
            else :
                i+=1
        return True

        