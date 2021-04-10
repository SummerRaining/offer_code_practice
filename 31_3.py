# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result,layer = [],[]
        stack = [[],[]]
        flag = 0
        if root == None:
            return result
        stack[0].append(root)
        while len(stack[0])!=0 or len(stack[1])!=0:
            a = stack[flag][-1]
            stack[flag].pop()
            layer.append(a.val)
            if flag ==0:
                if a.left != None:
                    stack[1-flag].append(a.left)
                if a.right != None:
                    stack[1-flag].append(a.right)
            else:
                if a.right != None:
                    stack[1-flag].append(a.right)
                if a.left != None:
                    stack[1-flag].append(a.left)

            if len(stack[flag])==0:
                result.append(layer)
                flag = 1-flag
                layer = []
        return result


