# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)


        while q:
            length = len(q)
           
            for i in range(len(q)):
                
                item = q.popleft()
                if i == length - 1:
                    res.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)

          

        return res
        
        