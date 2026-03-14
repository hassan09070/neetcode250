# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root: Optional[TreeNode]):

            if root:
                if not root.left and not root.right:
                    return [root.val]

                left = inorderTraversal(root.left) if root.left != None else []
                value = root.val
                right = inorderTraversal(root.right) if root.right != None else []

                return left + [value]+ right
            else:
                return []
        
        return inorderTraversal(root)[k-1]