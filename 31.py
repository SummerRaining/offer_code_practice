class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        stack = []
        p1,p2 = 0,0
        while p2<len(popped):
            while (len(stack)==0 or stack[-1] != popped[p2]) and p1<len(pushed):
                stack.append(pushed[p1])
                p1 += 1
            while len(stack) != 0 and p2<len(popped) and popped[p2] == stack[-1]:
                stack.pop()
                p2 += 1
            if p1==len(pushed) and p2<len(popped):
                return False
        return True
