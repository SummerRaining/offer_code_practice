class Solution:
    def isNumber(self, s: str) -> bool:
        #A[.[B]][e|EC]匹配模式，.B[e|EC]
        if s=='':
            return False
        s = list(s)+['\0']
        index = 0
        #检查空串
        index = self.check_black(s,index)
        flag,index = self.unsign_int(s,index)
        if s[index] == '.':
            tmp,index = self.check_int(s,index+1) 
            flag = tmp or flag
        if flag==True:
            if s[index] in ['e','E']:
                tmp,index = self.unsign_int(s,index+1)
                flag = tmp and flag
        #检查空串
        index = self.check_black(s,index)
        return s[index]=='\0' and flag

    def check_black(self,s,index):
        while s[index]==' ':
            index += 1
        return index
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
        return self.check_int(s,index)