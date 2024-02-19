class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        result = 0
        for char in columnTitle:
            # Convert character to its corresponding numerical value
            value = ord(char) - ord('A') + 1
            # Update the result by multiplying the current result by 26 (the number of letters in the alphabet) and adding the numerical value of the current character
            result = result * 26 + value
        return result