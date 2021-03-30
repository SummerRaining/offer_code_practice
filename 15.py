class Solution:
    def hammingWeight(self, n: int) -> int:
        flag = 1
        index = 1
        count = 0
        while index<=32:
            if flag&n:
                count += 1
            flag = flag << 1
            index += 1
        return count

