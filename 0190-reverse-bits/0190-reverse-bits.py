class Solution:
    def reverseBits(self, n: int) -> int:

        binary_representation = bin(n)[2:]
    
        # Pad the binary representation with leading zeros if necessary
        binary_representation = binary_representation.zfill(32)

#########Transfer the string to int and then make a list of integer
        result_array=list(map(int, str(binary_representation)))
        print (result_array)

        i=0
        while i< len(result_array)//2:
            temp =result_array[i]
            result_array[i]=result_array[len(result_array)-i-1]
            result_array[len(result_array)-i-1]=temp
            i+=1
        print (result_array)
        #########Transfer the array to string and then the string to int
        reversed_integer = int(''.join(map(str, result_array)), 2)
        return reversed_integer

           
        

        