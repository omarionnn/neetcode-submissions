# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftM = dfs(root.left)
            rightM = dfs(root.right)
            leftM = max(0, leftM)
            rightM = max(0, rightM)

            res = max(res, root.val + leftM + rightM)

            return root.val + max(leftM, rightM)

        dfs(root)
        return res
        