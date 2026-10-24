# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        count = 0
        lvlNodes = 1
        sublist = []
        while len(q) > 0:
            node = q.popleft()
            nodeLeft = node.left
            nodeRight = node.right
            sublist.append(node.val)

            if nodeLeft:
                q.append(nodeLeft)

            if nodeRight:
                q.append(nodeRight)

            count += 1
            if count == lvlNodes:
                count = 0
                lvlNodes = len(q)
                res.append(sublist)
                sublist = []

        return res
