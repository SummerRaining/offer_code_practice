class Solution:
    def fib(self, n: int) -> int:
        if n ==0:
            return 0
        first = 0
        seconde = 1
        index = 1
        while index<n:
            index += 1
            tmp =  (first+seconde)%(1000000007)
            first = seconde
            seconde = tmp
        return seconde