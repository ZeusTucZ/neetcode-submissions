# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(curr):
            if curr == None:
                return

            curr.left, curr.right = curr.right, curr.left

            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return root