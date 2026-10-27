# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, comp):
            nonlocal count

            if not root:
                return

            if root.val >= comp:
                count += 1

            comp = max(comp, root.val)
            dfs(root.left, comp)
            dfs(root.right, comp)

        dfs(root, -101)
        return count
