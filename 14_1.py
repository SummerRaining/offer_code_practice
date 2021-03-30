class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        arr = [0 for i in range(n+1)]
        arr[1] = 1
        arr[2] = 2
        arr[3] = 3
        arr[4] = 4
        for length in range(5,n+1):
            tmp = 0
            for j in range(1,int(length/2)+1):
                product = arr[j]*arr[length-j]
                if tmp<product:
                    tmp = product
            arr[length] = tmp
        return arr[n]%1000000007

