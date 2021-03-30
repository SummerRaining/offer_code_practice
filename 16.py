class Solution:
    def myPow(self, x: float, n: int) -> float:
        episilon = 0.00000000001
        if x<episilon and x>-episilon and n<0:
            return 0.0
        s = 1 if n>0 else -1
        result = self.helper(x,n*s)
        if s==1:
            return result
        return 1/result

    def helper(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        result = self.helper(x,n>>1)
        if n&1:
            return result*result*x
        else:
            return result*result
