class Solution:
    def isMatch(self, s: str, p: str):
        if s=='' and p=='':
            return True
        s = list(s)+['\0']
        p = list(p)+['\0']  #需要最后一个值表示结尾。
        self.log = {}       #回溯法，会产生很多次的重复调用。对于子问题重复计算。
        self.log[(len(s)-1,len(p)-1)] = True 
        return self.helper(s,p,0,0)

    def helper(self,s,p,sindex,pindex):
        if (sindex,pindex) in self.log:
            return self.log[(sindex,pindex)]
        if s[sindex]=='\0' and p[pindex]=='\0':
            return True
        if s[sindex]!='\0' and p[pindex]=='\0':
            return False
        result = False
        if p[pindex+1]=='*':
            if s[sindex]==p[pindex] or (p[pindex]=='.' and s[sindex]!='\0'):
                result = self.helper(s,p,sindex+1,pindex) or\
                    self.helper(s,p,sindex+1,pindex+2) or\
                    self.helper(s,p,sindex,pindex+2)
            else:
                result = self.helper(s,p,sindex,pindex+2)
        else:
            if s[sindex]==p[pindex] or (p[pindex]=='.' and s[sindex]!='\0'):
                result = self.helper(s,p,sindex+1,pindex+1)
        self.log[(sindex,pindex)] = result
        return result

s = "aaab"
p = "a*a*a*c"
s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
print(Solution().isMatch(s,p))