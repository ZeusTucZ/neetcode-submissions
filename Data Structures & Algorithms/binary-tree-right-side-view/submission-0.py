# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        val = None

        while len(q) > 0:

            for i in range(len(q)):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    val = node.val

            if val:
                res.append(val)
            val = None

        return res
                