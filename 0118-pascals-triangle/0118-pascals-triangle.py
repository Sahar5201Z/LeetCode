class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[1]
        pascal_list=[[1]]
        if(numRows<2):
            return pascal_list
        pascal.append(1)
        pascal_list.append(pascal[:])

        for i in range(1,numRows-1):
            pascal=[1]
            for j in range(0,i):
                pascal.append(pascal_list[i][j] + pascal_list[i][j+1])
                print("i", i,"j",j) 
            pascal.append(1)
            pascal_list.append(pascal[:])
        return pascal_list

        #for row in pascal_list:
        #    print(row)
        
        #print(pascal_list[0][0])
