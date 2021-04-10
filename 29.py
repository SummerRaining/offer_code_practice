class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        if len(matrix)==0:
            return []
        rows,cols = len(matrix),len(matrix[0])
        self.result = []
        for i in range(int((min(rows,cols)+1)/2)):
            self.helper(matrix,i,rows,cols)
        return self.result

    def helper(self,matrix,index,rows,cols):
        rstart,cstart = index,index
        rend,cend = rows-index-1,cols-index-1
        for i in range(cstart,cend+1):
            self.result.append(matrix[rstart][i])
        if rend >rstart:
            for j in range(rstart+1,rend+1):
                self.result.append(matrix[j][cend])
        if rend>rstart and cend>cstart:
            for i in range(cend-1,cstart-1,-1):
                self.result.append(matrix[rend][i])
        if rend>rstart+1 and cend>cstart:
            for j in range(rend-1,rstart,-1):
                self.result.append(matrix[j][cstart])