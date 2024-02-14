class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        stack=[]
#dictionery key, value
        parenthesMap={')': '(', ']': '[', '}': '{'}
        for paranthes in s:
            if paranthes in parenthesMap.values():
                stack.append(paranthes)
                print(paranthes + 'map_value')
            elif paranthes in parenthesMap.keys():
                top_element = stack.pop() if stack else '#'
                print(paranthes + 'map_keys')
        
                if parenthesMap[paranthes]!=top_element:
                    print(parenthesMap[paranthes] + 'resss')
                    return False
            else:
                print('ressswhy')
                # Invalid character in the input string
                return False
        if stack:
            print('ressswhy222')
            return False
        return True
        