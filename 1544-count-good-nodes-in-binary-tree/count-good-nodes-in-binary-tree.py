# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_val):
            if not node:
                return 0
            max_val = max(max_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            return left + right + (1 if node.val >= max_val else 0 )
        return dfs(root, float('-inf'))


        
        



            

        