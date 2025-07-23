# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        def coll_leaf_val(root, leaf_val):
            if not root:
                return
            if not root.left and not root.right:
                leaf_val.append(root.val)
            coll_leaf_val(root.left, leaf_val)
            coll_leaf_val(root.right, leaf_val) 
        leaf1 = []
        leaf2 = []
        coll_leaf_val(root1, leaf1)
        coll_leaf_val(root2, leaf2)

        return leaf1 == leaf2


        
        


        
        