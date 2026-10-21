# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root, p, q):
            if not root:
                return [False, None]

            left, leftNode = dfs(root.left, p, q)
            right, rightNode = dfs(root.right, p, q)
        
            curr = True if root == p or root == q else False

            if leftNode is not None:
                return [True, leftNode]

            if rightNode is not None:
                return [True, rightNode]
        
            if (left and right) or (left and curr) or (right and curr):
                return [True, root]

            if left or right:
                return [True, None]

            return [curr, None]

        curr, node = dfs(root, p, q)
        return node
