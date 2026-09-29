# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        q = [root]
        if root is None:
            return res
        while len(q) != 0:
            row = []
            size = len(q)
            for i in range(size):
                current = q.pop(0)
                row.append(current.val)
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
            res.append(row)
        return res