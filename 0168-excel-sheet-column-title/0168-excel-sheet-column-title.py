class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjusting to 0-based indexing
            digit = columnNumber % 26  # Extract the rightmost digit
            result = chr(digit + ord('A')) + result  # Convert the digit to a letter and prepend it to the result
            columnNumber //= 26  # Move to the next digit
        return result