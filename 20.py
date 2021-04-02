class Solution:
    def isNumber(self, s: str) -> bool:
        #A[.[B]][e|EC]匹配模式，.B[e|EC]
        if s=='':
            return False
        s = list(s)+['\0']
        index = 0
        flag,index = self.unsign_int(s,index)
        if s[index] == '.':
            flag = flag and self.check_int(s,index+1)
        if flag==True:
            if s[index] in ['e','E']:
                flag = self.check_int(s,index+1)
        #检查空串
        return s[index]=='\0' and flag

    def check_int(self,s,index):
        if index >=len(s):
            return False,index
        l = index
        while s[l]<='9' and s[l]>='0':
            l+=1
        return l>index,l

    def unsign_int(self,s,index):
        if s[index] in ['+','-']:
            index = index+1
        return self.check_int(s,index+1)