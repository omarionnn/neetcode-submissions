# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, max_so_far):
            nonlocal res
            if not node:
                return

            # If the current node is >= the maximum value seen on this path
            if node.val >= max_so_far:
                res += 1
                # Update the running maximum for the rest of this path
                max_so_far = node.val

            # Pass the running maximum down to the left and right subtrees
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)

        # Start the DFS with the root's own value as the initial maximum
        dfs(root, root.val)
        return res
        