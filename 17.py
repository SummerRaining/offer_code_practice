#该题考虑的是大数问题，全部放入到list中，就没有意义了。
#我用大数问题的解法完成

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        self.result = []
        if n<=0:
            return []
        s = ['0' for i in range(n)]
        self.helper(s,0,n)
        return self.result[1:]

    def helper(self,s,index,n):
        if index==n:
            self.result.append(int(''.join(s)))
            return 
        for i in range(10):
            s[index] = str(i)
            self.helper(s,index+1,n)