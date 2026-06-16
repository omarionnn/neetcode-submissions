class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not subRoot: 
            return True  # An empty tree is always a subtree of any tree
        if not root: 
            return False # A non-empty subRoot cannot be a subtree of an empty root

        # Check if the current tree matching from root is identical to subRoot
        if self.sameTree(root, subRoot):
            return True
        
        # FIXED: Recursively search for subRoot inside the left and right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        """Helper function to check if two trees are completely identical."""
        # If both are empty, they are identical
        if not a and not b:
            return True
        # If one is empty and the other isn't, they are not identical
        if not a or not b:
            return False
            
        # The values must match, and their structural left/right children must match
        if a.val == b.val:
            return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
            
        return False