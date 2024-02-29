class Solution:
    def hammingWeight(self, n: int) -> int:

        binaray_integer= bin(n)[2:]
        array_binary=list(map(int,binaray_integer))
        total_ones=0
        for i in array_binary: 
            if i==1 :
                total_ones+=1
            
        return total_ones

        