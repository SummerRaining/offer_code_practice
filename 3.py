class Solution:
    def replaceSpace(self, s: str) -> str:
        block_num = 0
        for i in s:
            if i==' ':
                block_num += 1
        new_len = block_num*2+len(s)
        length = len(s)
        a,b = length-1,new_len-1
        s = list(s+' '*2*block_num)
        while b>=0:
            if s[a]!=' ':
                s[b] = s[a]
                b -= 1
                a -= 1
            else:
                s[b] = '0'
                s[b-1] = '2'
                s[b-2] = '%'
                b = b-3
                a = a-1
        return ''.join(s)

