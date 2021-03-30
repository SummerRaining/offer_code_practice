class Solution:
    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        first = 1
        seconde = 1
        index = 1
        while index<n:
            index += 1
            tmp = (first+seconde)%(1000000007)
            first = seconde
            seconde = tmp
        return seconde


