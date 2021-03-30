class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0 for c in range(n)] for r in range(m)]
        return self.helper(m,n,0,0,k,visited)

    def helper(self,m,n,r,c,k,visited):
        count = 0
        if self.check(m,n,r,c,k,visited):
            visited[r][c] = 1
            count = 1+self.helper(m,n,r-1,c,k,visited)\
                    +self.helper(m,n,r+1,c,k,visited)\
                    +self.helper(m,n,r,c-1,k,visited)\
                    +self.helper(m,n,r,c+1,k,visited)
        return count

    def check(self,m,n,r,c,k,visited):
        if r>=0 and r<m  and c>=0 and c<n and visited[r][c] == 0:
            result = 0
            while r:
                result += r%10
                r = int(r/10)
            while c:
                result += c%10
                c = int(c/10)
            if result <=k:
                return True
        return False