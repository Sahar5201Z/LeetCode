class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        pascal_list = [[1], [1, 1]]

        for i in range(1,rowIndex):
            pascal=[1]
            for j in range(0,i):
                pascal.append(pascal_list[i][j] + pascal_list[i][j+1])
            
            pascal.append(1)
            pascal_list.append(pascal[:])
        
        return pascal_list[rowIndex][:]