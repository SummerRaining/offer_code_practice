class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        if rows==0:
            return False
        cols = len(board[0])
        visited = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                haspath = self.helper(board,visited,r,c,rows,cols,word,0)
                if haspath:
                    return True
        return False

    def helper(self,board,visited,r,c,rows,cols,word,pidx):
        if len(word)==pidx:
            return True
        haspath = False
        if (r<rows) and (c<cols) and (r>=0) and (c>=0) and visited[r][c]==0 \
            and board[r][c]==word[pidx]:
            pidx += 1
            visited[r][c] = 1
            haspath = self.helper(board,visited,r+1,c,rows,cols,word,pidx) or \
                        self.helper(board,visited,r-1,c,rows,cols,word,pidx) or \
                        self.helper(board,visited,r,c+1,rows,cols,word,pidx) or \
                        self.helper(board,visited,r,c-1,rows,cols,word,pidx)
            if haspath == False:
                pidx -= 1
                visited[r][c] = 0
        return haspath