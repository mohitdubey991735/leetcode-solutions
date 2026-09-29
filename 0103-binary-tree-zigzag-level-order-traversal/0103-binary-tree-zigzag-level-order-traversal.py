# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        left_to_right = True
        res = []
        q = [root]
        if root is None:
            return res
        while len(q) != 0:
            row = []
            size = len(q)
            for i in range(size):
                current = q.pop(0)
                if left_to_right is True:
                    row.append(current.val)
                else:
                    row.insert(0,current.val)
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
                
            res.append(row)
            left_to_right = not left_to_right
        
        return res

            


